# Web crawler to extract data from property websites using noSQL databases - Redis and MongoDB

This project aims to develop a versatile web crawler for extracting data from property websites, utilizing NoSQL databases such as Redis and MongoDB.

The crawler retrieves specific tasks or inputs from Redis, allowing data extraction processes across multiple sites using a single script. In this project two portuguese sites were scraped: [CASASAPO](https://casa.sapo.pt/) and [Imovirtual](https://www.imovirtual.com/).

Data extraction is performed using the requests library, and the raw data is stored directly in MongoDB for further processing and analysis.

Using the pytest package, integration tests were also implemented with databases and a response test for all the URL links present in keys from Redis

The project is based on [this repo](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/05-redis-mongodb-esse-tal-de-nosql).

<img src="media/demo.gif" width = 1000 />

## Context

By separating the generic Python web crawler from the site-specific details, we can organize the extraction process and avoid making changes to the Python script related to eventual HTML changes in website structures, for example. In cases like that, changing the inputs in Redis keys will be sufficient to keep the script running. It also allows us to scale the process to more websites in a simpler way, by adding their html sctructure to a new Redis key.   

Although this is a very useful approach, it won't always be possible to adapt all the websites to the same crawler structure. In cases like that, a specific solution will always be needed.

## How it works

![](media/diagram.png)

After receiving a specific website key identification, the script retrieves all the inputs from the Redis database in a JSON format. These inputs are responsible for the URL requests and capturing the HTML structure of the target site for extraction. It also receives a query specifying the location in Portugal from which to search for properties. 

The extraction process utilizes the BeautifulSoup package, and through a recursive function, it identifies additional pages for extraction if present.

To establish connections with both Redis and MongoDB, the generic crawler inherits from an abstract class.

After extracting all the raw data, it is stored directly in the MongoDB database for further processing and analysis.

### Project folder structure
```
├── README.md
├── docker-compose.yaml
├── media
│   ├── demo.gif
│   └── diagram.png
├── poetry.lock
├── pyproject.toml
├── redis_keys
│   ├── imovirtual.json
│   └── sapo.json
├── src
│   ├── main.py
│   ├── request
│   │   ├── default_crawler.py
│   │   └── generic_crawler.py
│   └── tools
│       ├── mongodb.py
│       └── redis.py
└── tests
    ├── test_integration.py
    └── test_response.py
```
## How to run this project

All the steps below were created using a bash terminal. To local setup it uses `pyenv` and `poetry`.

It is divided in 3 sequencial steps:

1. Clone the repository locally.
2. Build docker containers and connect to Redis and MongoDB.
3. Configure local setup.

#### 1 - Clone the project locally

1.1 -  Clone the repository:
```bash
git clone https://github.com/lealre/properties-webcrawler.git
```
1.2 -  Enter the folder:
 ```bash
 cd properties-webcrawler
 ```

#### 2 - Build docker containers and connect to Redis and MongoDB

Once inside the folder project, we build the containers for Redis and MongoDB using Docker:
```bash
docker compose up -d
```

Now that we have both databases running, the next step is to connect to them using a GUI. 

**Redis**

The GUI for REDIS used in this project was [Another Redis Desktop Manager](https://github.com/qishibo/AnotherRedisDesktopManager), where you can connect by using: 

`host: 127.0.0.1` 

`port: 6379`

[Redis GUI Free App](https://onexlab-io.medium.com/redis-gui-free-app-e2e6fe67b9de)

After connecting to the GUI, you can create the keys. The name of the keys correspond to the names of JSON files sored in [redis_keys](https://github.com/lealre/properties-webcrawler/tree/main/redis_keys) folder, and their content are their respectives values, where you can copy and paste setting it to JSON format.


**MongoDB**

The GUI for MongoDB used in this project was [Studio 3T Trial](https://studio3t.com/), where you can connect by clicking in connect and passing the link below:

```
mongodb://localhost:27017
```

 #### 3 -  Local Setup

After connecting Redis and MongoDB, we configure the project setup and run it:

3.1 -  Install Python version using pyenv:
```bash
pyenv install 3.11.5
```

3.2 -  Set Python local version:
```bash
pyenv local 3.11.5
```

3.3 -  Create virtual enviroment with poetry:
```bash
poetry env use 3.11.5
``` 
```bash
poetry shell
```

3.4 -  Install dependencies:
```bash
poetry install --no-root
```
```bash
poetry lock --no-update
```

3.5 - Run the project:
```bash
task main
```

To run both integration and response tests:
```bash
task test_integrations # integration test
task test_responses # response requests test to urls in Redis keys
```


## Further tasks

* Since it stores raw data, it is necessary to add a transformation and manipulation step to clean the data;
* There are no verifications to deal with entries that may already be stored in the database;
* Adding more websites can test the versatility of the generic crawler and improve it;
* A frontend interface can be created to return the data in a specific format to the user.