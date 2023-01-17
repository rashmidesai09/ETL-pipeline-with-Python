# ETL-pipeline-with-Python

## Project 1 - Export Excel data to PostgreSQL
This is a Python ETL pipeline that ingests multiple flat files, reads data from a network share, and loads it into a Postgres database. The goal of the project is to make reference data available for analytics by adding more detailed information to an existing accounts table in the database. The pipeline reads data from excel sheets and saves it into a table in the data warehouse, providing the ability to expand a particular category to see what makes up revenue or operating expenses. This allows for easy overwriting of data in excel sheets while maintaining a reliable source of reference data in the data warehouse.


## Project 2 - Export data from CSV, JSON to ready-to-load format in csv
The goal of this project is to extract data from bank and market cap information from a JSON file and convert it into a ready-to-load format for data engineers. This includes reading both CSV and JSON file types, using exchange rate data to transform the market cap currency, and finally saving the transformed data in a separate CSV file for easy loading into an RDBMS.

## Project 3 - Export from SQL Server to PostgreSQL
This project uses SQL Server's AdventureWorks database as a source and loads data into a PostgreSQL database using Python. It includes scripts to create a database and user in PostgreSQL, as well as to save credentials in environment variables for security. The project maps tables from the source to the destination environment and uses the Pandas library to extract and load data. The approach followed is the truncate and load, where the tables are replaced with each run, and data can be transformed and loaded into the presentation layer.
