# Data Warehousing Project

## Overview
This project focuses on creating a simple data warehouse using SQLite. It includes scripts for creating tables, loading data, and querying the database.

## Project Structure


                   data-warehousing/ 
                                   │
                                   ├── src/ 
                                          │ 
                                          ├── create_tables.py # Table creation script 
                                          │ 
                                          ├── load_data.py # Data loading script 
                                          │ 
                                          ├── query_data.py # Data querying script 
                                   ├── tests/ 
                                            │ 
                                            └── test_queries.py # Unit tests for queries 
                                   ├── requirements.txt # Dependencies 
                                   └── README.md # Project documentation



## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/data-warehousing.git
   cd data-warehousing


2. Install the required packages:

         pip install -r requirements.txt


## Usage

1. Run the script to create tables:

       python src/create_tables.py

2. Load data into the tables (you may need to modify load_data.py to point to your CSV):

          python src/load_data.py

3. Query the data:

      python src/query_data.py


## Testing

  Run the unit tests to ensure the querying works correctly:


       python -m unittest discover -s tests

## License

This project is licensed under the MIT License.
