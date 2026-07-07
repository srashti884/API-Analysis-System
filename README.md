# API Analysis System - ETL Pipeline Using Python & MySQL
Project Overview
The API Analysis System is an End-to-End ETL (Extract, Transform, Load) pipeline developed using Python. The project extracts data from multiple REST APIs, stores the raw data in JSON format, transforms it into CSV, XML, and Parquet formats, and loads the processed data into a MySQL database.
This project demonstrates practical Data Engineering concepts including API integration, data transformation, data storage, and database loading.

APIs Used
Categories API

Categories API: https://api.escuelajs.co/api/v1/categories 
Users API: https://api.escuelajs.co/api/v1/users 
Products API: https://api.escuelajs.co/api/v1/products 

Project Architecture

REST APIs
                     |
      --------------------------------
      |              |               |
 Categories       Users         Products
      |              |               |
      --------------------------------
                     |
                     V
                JSON Files
                     |
        -------------------------
        |           |           |
       CSV         XML      Parquet
                     |
                     V
              MySQL Database
                     |
        -------------------------
        |          |           |
    Categories    Users    Products

Technology Stack
Programming Language

Python

Libraries

Requests
Pandas
SQLAlchemy
PyMySQL
DicttoXML
PyArrow

Database

MySQL

Tools

VS Code
MySQL Workbench
Git
GitHub

Project Structure
API-Analysis-System
│
├── extract.py
├── json_to_csv.py
├── json_to_xml.py
├── json_to_parque.py
├── load_mysql.py
├── test_mysql.py
│
├── data
│   ├── json
│   │   ├── categories.json
│   │   ├── users.json
│   │   └── products.json
│   │
│   ├── csv
│   │   ├── categories.csv
│   │   ├── users.csv
│   │   └── products.csv
│   │
│   ├── xml
│   │   ├── categories.xml
│   │   ├── users.xml
│   │   └── products.xml
│   │
│   └── parquet
│       ├── categories.parquet
│       ├── users.parquet
│       └── products.parquet
│
└── README.md

-------------------------------------------------------------------------------------------------------------
ETL Workflow
**Step 1: Extract**

Connected to REST APIs using the Requests library.
Retrieved Categories, Users, and Products data.
Stored raw responses as JSON files.

**Step 2: Transform**

Converted JSON data into CSV format using Pandas.
Converted JSON data into XML format using DicttoXML.
Converted JSON data into Parquet format using PyArrow.

**Step 3: Load**

Loaded CSV data into MySQL tables using SQLAlchemy and PyMySQL.
Automatically created database tables.

=========================================================================================================================
Database Setup
Create Database
Database Setup
Create a MySQL database named api_analysis.
Execute the SQL command:
CREATE DATABASE api_analysis;
Verify that the database has been created successfully:
SHOW DATABASES;

Load Data into MySQL
Run the load_mysql.py script to transfer the CSV files into MySQL tables.
Command:
python load_mysql.py
The following tables will be created automatically:
• categories
• users
• products

Validation Queries
Use the following queries to validate the data loading process.
View all tables:
USE api_analysis;
SHOW TABLES;
Check the number of records in each table:
SELECT COUNT(*) FROM categories;
SELECT COUNT(*) FROM users;
SELECT COUNT(*) FROM products;
View sample records:
SELECT * FROM categories;
SELECT * FROM users LIMIT 5;
SELECT * FROM products LIMIT 10;

Installation
Clone the repository:
git clone https://github.com/srashti884/API-Analysis-System.git
Navigate to the project directory:
cd API-Analysis-System
Install the required Python libraries:
pip install -r requirements.txt

How to Run the Project
Step 1: Extract Data from APIs
python extract.py
This script fetches data from the Categories, Users, and Products APIs and stores the responses as JSON files.
Step 2: Convert JSON to CSV
python json_to_csv.py
This script converts JSON files into CSV format.
Step 3: Convert JSON to XML
python json_to_xml.py
This script converts JSON files into XML format.
Step 4: Convert JSON to Parquet
python json_to_parque.py
This script converts JSON files into Parquet format.
Step 5: Load Data into MySQL
python load_mysql.py
This script loads the transformed CSV data into MySQL tables.

Key Features
• Extracts data from multiple REST APIs
• Stores raw API responses in JSON format
• Converts JSON data into CSV format
• Converts JSON data into XML format
• Converts JSON data into Parquet format
• Loads transformed data into MySQL
• Automatically creates database tables
• Implements an end-to-end ETL pipeline using Python
• Version controlled using Git and GitHub

Challenges Faced
• API response handling and data normalization
• Installation and configuration of Python libraries
• MySQL database authentication and connectivity
• Data transformation across multiple file formats
• Managing an end-to-end ETL workflow

Future Enhancements
• Add logging functionality
• Implement exception handling and retry mechanisms
• Integrate Apache Airflow for workflow scheduling
• Support PostgreSQL and Oracle databases
• Containerize the application using Docker
• Add automated testing and monitoring
=======================================================================================================
Author
Srashti Shrivastava
Software Engineer | Data Engineering Enthusiast
GitHub: https://github.com/srashti884

Project Summary
Developed an end-to-end ETL pipeline using Python that extracts data from multiple REST APIs, stores raw responses in JSON format, transforms the data into CSV, XML, and Parquet formats, and loads it into a MySQL database using SQLAlchemy and PyMySQL. The project demonstrates practical Data Engineering concepts including data extraction, transformation, storage, and database ingestion.






    
