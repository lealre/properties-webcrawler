from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
from typing import Any

from src.request.default_crawler import AbstractCrawler

class GenericCrawler(AbstractCrawler):

    def __init__(self, site: str):
        super().__init__()
        self.site = site
        self.data: list = []

    def crawl(self, location: str):
        self.location = location
        self.configs = json.loads(self.get_steps(self.site))
        if self.configs is None:
            raise("Crawler not configured!")
        df = self.execute_main()
        self.mongo.save_dataframe(df)
        return df
    
    def execute_main(self):
        connector = self.configs["links"]["connector"]
        self.url = f"{self.configs['links']['path']}{self.location.replace(' ', connector)}"
        if self.configs['links']['add_after']:
            self.url = self.url + self.configs['links']['add_after']
        self.get_data(self.url)
        return self.transform(self.data)

    def get_data(self, url: str):
        response = requests.get(url, headers= self.headers)
        if response.status_code > 400:
            raise("Status Code != 200")    
        html = response.text
        self.soup = BeautifulSoup(html, "html.parser")

        print('Extracting data from', url )
        self.extract()

        
        next_page = self.soup.find(self.configs["pages"]["next_page"]["tag"],
                                    class_=self.configs["pages"]["next_page"]["class"])    

        try:
            last_page = self.soup.find(self.configs["pages"]["last_page"]["first"]["tag"]
                                       , class_=self.configs["pages"]["last_page"]["first"]["class"]).find(self.configs["pages"]["last_page"]["second"]["tag"], 
                                                                                                           class_=self.configs["pages"]["last_page"]["second"]["class"])
        except:
            last_page = False

        if next_page and not last_page:
            try: 
                new_url = eval(self.configs["pages"]["new_url"])
            except:
                raise("Error extracting the new URL")
        else:
            return print("All data extracted!")

        self.get_data(new_url)

    def extract(self):
        results = self.soup.find_all(self.configs["search"]["tag"], class_ = self.configs["search"]["class"] )

        for result in results:
            info = {}
            for step in self.configs["info"]:
                value = self.configs["info"][step]
                try:
                    content = eval(value)
                except:
                    content = None
                info[step] = content
            self.data.append(info)

    def transform(self, data: dict[str, Any]) -> pd.DataFrame:
            return pd.DataFrame(data)