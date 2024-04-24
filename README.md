# Web crawler to extract data from property websites using noSQL databases - Redis and MongoDB

This project aims to develop a versatile web crawler for extracting data from property websites, utilizing NoSQL databases such as Redis and MongoDB.

The crawler retrieves specific tasks or inputs from Redis, allowing data extraction processes across multiple sites using a single script. In this project two portuguese sites were scraped: [CASASAPO](https://casa.sapo.pt/) and [Imovirtual](https://www.imovirtual.com/).

Data extraction is performed using the requests library, and the raw data is stored directly in MongoDB for further processing and analysis.

The project is very based on [this repo](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/05-redis-mongodb-esse-tal-de-nosql).

## Context

By separating the generic Python web crawler from the site-specific details, we can organize the extraction process and avoid making changes to the Python script related to eventual HTML changes in website structures, for example. In cases like that, changing the inputs in Redis keys will be sufficient to keep the script running. It also allows us to scale the process to more websites in a simpler way, by adding their html sctructure to a new Redis key.   

Although this is a very useful approach, it won't always be possible to adapt all the websites to the same crawler structure. In cases like that, a specific solution will always be needed.

## How it works

### Project folder structure

## How to run this project

## Further tasks
