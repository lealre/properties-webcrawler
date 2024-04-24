# Web crawler to extract data from property websites using noSQL databases - Redis and MongoDB

This project aims to develop a versatile web crawler for extracting data from property websites, utilizing NoSQL databases such as Redis and MongoDB.

The crawler retrieves specific tasks or inputs from Redis, allowing data extraction processes across multiple sites using a single script. In this project two portuguese sites were scraped: [CASASAPO](https://casa.sapo.pt/) and [Imovirtual](https://www.imovirtual.com/).

Data extraction is performed using the requests library, and the raw data is stored directly in MongoDB for further processing and analysis.

The project is very based on [this repo](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/05-redis-mongodb-esse-tal-de-nosql).

<!-- ## Context

By separating the generic python web crawler and the sites specificities, we can transform on  just one script instead of one for for ecah site, and  -->
