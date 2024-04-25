import sys
import os
# Add the root directory of your project to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dotenv import load_dotenv
load_dotenv(".env")

from request.generic_crawler import GenericCrawler

df_sapo = GenericCrawler(site= 'sapo').crawl('minde')
print(df_sapo)

df_imo = GenericCrawler(site = 'imovirtual').crawl('evora')
print(df_imo)
