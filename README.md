# Aplázame technical test
____
### Requirements

In order to run the application:
- Docker  
- Docker compose

To execute tests:
- python 3.9.10  
- all the required libraries across the different requirements.txt files

The first execution the server must be initialized. In order to create the required database:
1. Connect to the DB container through the port 3306 or straight from the Docker command line
2. Execute the following commands:  
   `mariadb -uroot -p${MYSQL_ROOT_PASSWORD}`  
   `create database if not exists apzm;`

____
### Run

#### Tests
From the project directory  
`python3 -m base/tests/test.py`  
`python3 -m predict/tests/test.py`  
`python3 -m registry/tests/test.py`
#### Service
From the project directory  
`docker-compose up`

___
###API Requests
#### New Prediction
- url: http://0.0.0.0:5005/model/asnef/predict/${client_id} 
- method: POST  
- payload:  
`{
"experian-score":2000,
"experian-score_probability_default":0.01,
"experian-score_percentile":80.0,
"experian-mark":"B"
}
`
- response:  
`{
    "asnef-score": 6
}
`
#### Get all predictions for client id
- url: http://0.0.0.0:5005/asnef/register/${client_id} 
- method: GET
- response:  
`{
    "registry": [
        {
            "registered_at": "2022-02-09 12:00:35",
            "asnef_score": 6
        },
        {
            "registered_at": "2022-02-09 11:22:43",
            "asnef_score": 6
        }
    ]
}
`

___
### Design overview
The service is built from 4 different Docker Images:
- [Maria DB](db) database
- 3 Flask Services:
  - [Base API](base) - Used as an interface that checks, validates and routes the requests
  - [Predict API](predict) - Applies the model to the already validated parameters 
  - [Registry API](registry) - Connects to the Database to update/retrieve records

All the services and configuration can be found in [the docker-compose file.](docker-compose.yaml)
