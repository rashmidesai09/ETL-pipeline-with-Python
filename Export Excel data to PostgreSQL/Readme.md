# Project 1 :Python ETL Pipeline to load data in excel sheet into database (PostgreSQL)

## Project Goal :
1. Ingest multiple flat files
2. Read data from a network share
3. Load them into Postgres database with Python
4. As a result, the reference data is available for analytics
5. We have an accounts table in the database, but it does not include the level of details required for the reporting. 
   For example, you are preparing an income state for your company and your Accounts table has the base accounts, but it does not include the header or the sub header    that breaks down a category i.e., revenue into Gross Sales, returns and adjustment and discount. 
   This gives you the ability to expand a particular category to see what makes up your revenue or operating expenses. 
6. The data in excel sheet can be easily overwritten and hence we prefer saving the reference data in the data warehouse by leveraging Python ETL pipeline to read         these files and save them into a table.

The database looks like this (note that it has 5 tables)
![5tables](https://user-images.githubusercontent.com/97893144/206890474-21e6276d-4227-45e6-b74c-91037da2ebda.jpg)

The databases will have 7 tables after the running the pythin script. Refer the tables - stg_lkpAccount and stg_lkpSalesTerritory
![aftercode](https://user-images.githubusercontent.com/97893144/206890479-791538f8-7631-4c13-9e29-a4e42b0de685.jpg)

## Steps followed :
1. Load the two excel files from a shared folder. 
   File details - Accounts file and territory mapping. 
2. ETL pipeline will enable you to:
   - Understand OS module to iterate over directories
   - Perform certain checks on files
   - Read files with Pandas and Write data to a database
   - Store data in a database table 
   
 ### Details about Reading Files with OS Module
 
1. Python provides various options to iterate over files in a directory. 
2. We used “listdir()” function from the OS module. This function returns the list of files and subdirectories present in the given       directory. 
3. We then filter the list to get only the files using “os.path.isfile()” function. Also, we can limit our criteria to certain type of files
   for example, we can use Python String “endswith()” method. The “endswith()” method returns True if a string ends with the xlsx suffix. 
4. Once we get hold of the file, we can build a complete file path with “path.join()” method. 
   The join method combines the file path and filename to give us complete path. Our Extract function will be based on this approach.

### The Extract

1. The first step is to read the Excel files as pandas DataFrames. We iterate over the directory and get the files name and use the file name as the table name.
2. Split the filename to grab the name without the extension.
3. Check if file extension is xlsx so that we do not accidently process any other files such as csv or text file in directory.
4. Join the directory and filename with join function from OS dot path. This gives us the complete file path.
5. Once we have the complete file path, read the file in a pandas DataFrame with “read_excel()” and call the load function to which we pass the DataFrame and the file    name without extension.
6. Refer to the def extract() in the python script

### The Load

1. Table name is provided as an argument to this function. 
2. Load data into a SQL database with pandas “to_sql()” function.
3. Loop through and query each table in the Extract, call the next function defined as the load.
4. Follow the truncate and load approach as it is simple and it replace the tables with each run. This is staging environment to pull in new data on a given interval.    From here, data can be transformed and loaded the data into the presentation layer. 
   The python script has def load() to store data in a PostgreSQL database using Pandas.
