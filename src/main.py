import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv(".env")

from request.generic_crawler import GenericCrawler

GenericCrawler(site= 'sapo').crawl('tomar')
GenericCrawler(site = 'imovirtual').crawl('aveiro')

