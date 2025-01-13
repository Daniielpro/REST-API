# Calculator REST API

This project is a simple REST API that allows you to perform basic math operations, such as addition and subtraction, using Flask in Python.

## Requirements

- Python 3.6 or higher
- pip (Python package manager)

## Project Structure

```plaintext
REST API/
│
├── flask_rest_server.py # REST server that handles operations
├── rest_client.py # Client that makes requests to the server
└── README.md # Project documentation
```

## Instructions for Using the Project
1. Clone the Repository

To clone this repository, use the following command:

 ```bash
 git clone https://github.com/Daniielpro/REST-API.git

 ```

2. Install the necessary dependencies:
Initialize and download the dependencies Required dependencies:
 
 ```bash
 pip install Flask requests
 ```

3. Run the Server
Start the REST API server:
 
 ```bash
  python flask_rest_server.py
  ```

4. Run the client
Start the REST AOI client:
 
 ```bash
  python rest_client.py
  ```

## How to Make Queries
Interact with the API
You can use tools like curl, Postman, to make queries.

Query Example:

 curl -X POST http://127.0.0.1:8000/add -H "Content-Type: application/json" -d '{"a": 5, "b": 3}'

Expected response:
 {
 "result": 8
 }

## Author
EDWIN PROAÑO
GitHub: Daniielpro10
