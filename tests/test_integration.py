import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest

from src.tools.mongodb import MongoConnection
from src.tools.redis import RedisClient

def test_redis_connection():
    assert RedisClient().get().ping(), "Redis connection test failed"

def test_mongo_connection():
    assert MongoConnection().server_info(), "MongoDB connection test failed"