import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from src.tools.mongodb import MongoConnection
from src.tools.redis import RedisClient

@pytest.mark.dependency()
def test_redis_connection():
    """
    Test the connection to Redis.

    Raises:
        AssertionError: If the Redis connection test fails.
    """
    assert RedisClient().get().ping(), "Redis connection test failed"

def test_mongo_connection():
    """
    Test the connection to MongoDB.
    
    Raises:
        AssertionError: If the MongoDB connection test fails.
    """
    assert MongoConnection().server_info(), "MongoDB connection test failed"