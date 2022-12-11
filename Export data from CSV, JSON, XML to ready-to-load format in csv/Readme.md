# Export data from CSV, JSON to ready-to-load format in csv

## Project 1 
## Project Goal
1. Read CSV and JSON file types.
2. Extract data from bank and market cap data from the JSON file bank_market_cap.json.
3. Transform the market cap currency using the exchange rate data
4. Save the transformed data in a ready-to-load format which data engineers can use to load into an RDBMS. This can be done into a separate CSV.

Steps followed -
## Import all the necessary libraries
import glob  # this module helps in selecting files 
import pandas as pd   # this module helps in processing the csv file
from datetime import datetime  

## Extract

Define the extract function that finds JSON file bank_market_cap_1.json and calls the function created above to extract data from them. Store the data in a pandas dataframe

## Transform

Using exchange_rate and the exchange_rates.csv file find the exchange rate of USD to GBP. Write a transform function that

Changes the Market Cap (US$ Billion) column from USD to GBP
Rounds the Market Cap (US$ Billion)` column to 3 decimal places
Rename Market Cap (US$ Billion) to Market Cap (GBP$ Billion)

## Load

Create a function that takes a dataframe and load it to a csv named bank_market_cap_gbp.csv. Make sure to set index to False.

## Logging Function
Write the logging function log to log your data

## Running the ETL Process
Log the process accordingly using the following "ETL Job Started" and "Extract phase Started"
