import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import requests
import json

from src.tools.redis import RedisClient
from tests.test_integration import test_redis_connection

@pytest.fixture(scope= "function")
def setup_data():
    """
    Set up data for testing Redis links.

    Retrieves URLs from Redis using the RedisClient and prepares them for testing.

    Yields:
        list: A list of URLs to be tested.
    """
    list_urls: list = []
    location = 'lisboa'
    redis = RedisClient.get()
    keys = redis.keys()
    for key in keys:
        link = json.loads(redis.get(key))['links']['path']
        url = link + location
        list_urls.append(url)
    yield list_urls

@pytest.mark.dependency(depends=["test_redis_connection"])
def test_responses_Redis_links(setup_data):
    """
    Test the responses of Redis keys links.

    Depends on test_redis_connection function test on tests/test_integration.py

    Args:
        setup_data (fixture): Fixture that provides a list of URLs to test.

    Raises:
        AssertionError: If the response status code is not 200 for any URL.
    """
    for url in setup_data:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
    
        response = requests.get(url, headers=headers)
        print(response)
        assert response.status_code == 200, "Status coode != 200"

