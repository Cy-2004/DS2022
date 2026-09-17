# Working with APIs

An API is a web-based standard for computers to communicate with one another. They are useful in data science as a way of retrieving remote data, or publishing data and making it available to others.

Fork and clone this repository to build your own API using a VS Code Devcontainer - https://github.com/uvasds-systems/fastapi-devcontainer/ 

## Methods

- **GET** - fetch or retrieve data
- **POST** - send or submit data

## Endpoints

Endpoints are the various URL paths of an API. Each one represents a different data collection or type of interaction with the API.

For instance, a company that sells bicycles might have the following endpoints (with their methods):

- `/customers` [GET] - a way of fetching a list of its customers
- `/customers/{ID}` [GET] - a way of fetching a single customer record
- `/customers` [POST] - a way of creating a new customer record
- `/catalog` [GET] - a way of fetching a list of all products
- `/catalog/{ID}` [GET] - a way of fetching a single catalog item
- `/catalog` [POST] - a way of creating a new product record

## Payloads

Payloads are typically a collection of data in JSON format, though sometimes a payload might be a file. Payloads can be submitted or received. Here is a simple example:

```
{
  "Index":1412,
  "Customer Id":"9f8DB43FFeC1Da4",
  "First Name":"Stuart",
  "Last Name":"Ballard",
  "Company":"Fox, Ballard and Patton",
  "City":"South Randall",
  "Email":"vaughankirk@hunter-chavez.com",
  "Subscription Date":"2020-05-21",
}
```

## API Data

APIs typically expose data from another system, such as storage, a database, or another service.

### Pandas

However, students familiar with Python will recognize that the Pandas library can query CSV files in much the same way as a database. So we can use Pandas to "query" a flat text file
as if it were a database by passing in our query and letting Pandas find that record for us. With a relational database, we would use SQL to perform this query.

Consider the following example, which passes a row index into a function to retrieve that record using Pandas.

[Sample Data](customers.csv) - fetch the 10k customer record CSV file.

```
import pandas as pd

def get_customer_by_index(idx):
  df = pd.read_csv("customers.csv")
  customer = df.iloc[idx]
  return customer.to_dict()

get_customer_by_index(1372)
```

```
{'Index': 1373, 'Customer Id': '3AD32Dab554fcaD', 'First Name': 'Kyle', 'Last Name': 'Jefferson', 'Company': 'Farley-Mcgrath', 'City': 'Lorettatown', 'Country': 'Australia', 'Phone 1': '435-303-9388x292', 'Phone 2': '(703)354-0004x2229', 'Email': 'natalie51@reid.com', 'Subscription Date': '2021-07-13', 'Website': 'http://cole-melton.com/'}
```

### POSTing data

It may also be helpful to see what you get when you POST data to a FastAPI. Consider this snippet of FastAPI code, which takes the JSON payload submitted in the body of the request and returns it back to the user:

```
from fastapi import Request, FastAPI

api = FastAPI()

@api.post("/get_body")
async def get_body(request: Request):
    return await request.json()
```
```
curl -X 'POST' \
  'http://127.0.0.1:8000/get_body' \
  -H 'accept: application/json' \
  -d '{"first_field": 2022, "second_field": "Systems I: Intro to Computing", "third_field":"SDS"}'
```

Here is a snippet for FastAPI with all of the above methods and endpoints:

```
#!/usr/bin/env python3

from fastapi import Request, FastAPI
from typing import Optional
from pydantic import BaseModel
import pandas as pd
import json
import os

api = FastAPI()

@api.get("/")  # zone apex
def zone_apex():
    return {"Hello": "Hello API"}

@api.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"sum": a + b}

@api.get("/customer/{idx}")
def get_customer(idx: int):
    # Read the data from the CSV file
    df = pd.read_csv("../customers.csv")
    # Filter the data based on the index
    customer = df.iloc[idx]
    return customer.to_dict()

@api.post("/get_body")
async def get_body(request: Request):
    return await request.json()

@api.post("/mapit")
async def map_request(request: Request):
    response = await request.json()
    geo = response.get("geo")
    url = "https://maps.google.com/?q={geo}".format(geo=geo)
    return {"gmaps_url": url}
```
