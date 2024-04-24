from abc import ABC, abstractmethod

from src.tools.mongodb import MongoConnection
from tools.redis import RedisClient

class AbstractCrawler(ABC):

    def __init__(self):
        self.redis = RedisClient.get()
        self.mongo = MongoConnection()

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
    
    @abstractmethod
    def crawl(self):
        pass
    
    def get_steps(self, site):
        return self.redis.get(site)

    def save_data(self, data):
        try:
            self.mongo.save_dataframe(data)
        except:
            raise("It was not possible to save the data in MongoDB")
    