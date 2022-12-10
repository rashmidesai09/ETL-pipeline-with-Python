# Building a basic ETL Pipeline with Python using Python, Pandas, SQLAlchemy, SQL Server and PostgreSQL

## Basic definition of ETL 
![image](https://user-images.githubusercontent.com/97893144/206855340-21c27548-6a13-4a47-a859-3daae8e9ce71.png)

An ETL pipeline is the set of processes used to move data from a source or multiple sources into a database such as a data warehouse. ETL stands for “extract, transform, load,” the three interdependent processes of data integration used to pull data from one database and move it to another. Once loaded, data can be used for reporting, analysis, and deriving actionable business insightscreate the same user in SQL Server environment to keep things consistent. 

There are many different tools and technologies we can use to build an ETL pipeline depending on the business requirement and skillset. In this project,we will use Python and specifically Pandas and SQLAlchemy to extract and load data.

## The Setup
In this project we will use SQL Server’s AdventureWorks database as a source and load data in PostgreSQL with Python. 
Instruction to install - https://www.youtube.com/watch?v=e5mvoKuV3xs and https://www.youtube.com/watch?v=fjYiWXHI7Mo , also refer to the SQL scripts folder for the queries executed in SQL server and PostgreSQL for the initial setup.

### Details of the SQL scripts -
1. Create a database in PostgreSQL to house the incoming tables and data.
2. Create a user in PostgreSQL and grant it connect permissions along with select, insert, update and delete.
3. Create the same user in SQL Server environment to keep things consistent. 

Lastly, save the credentials in environment variables. The goal is to protect the credentials from being exposed in the ETL script.


## The Extract

1. Map each table from the source to destination environment. 
2. Create similar objects with matching data types in both environments. 
3. Connect to both environments and perform mapping for each table and then trigger the pipeline.
4. Extract data from SQL Server’s system schema, loop through the tables and query them. Thus with just few lines of codes, we can query the source and 
   store the data as Pandas dataframe.

Refer to the def extract() in python script

## The Load

1. Load data into a SQL database with pandas “to_sql()” function. 
2. Loop through and query each table in the Extract, call the next function defined as the load. 
3. Follow the truncate and load approach as it is simple and it replace the tables with each run. 
   This is staging environment to pull in new data on a given interval. From here, data can be transformed and loaded the data into the presentation layer. 
   The python scripthas def load() to store data in a PostgreSQL database using Pandas.
   
## Basic Validation
1. The number of rows in source and destination tables verified

### Destination

   <img width="400" alt="image" src="https://user-images.githubusercontent.com/97893144/206856603-edaf97a6-7a87-41f8-9ce7-3b218030af5b.png">

### Source 

   <img width="400" alt="image" src="https://user-images.githubusercontent.com/97893144/206856713-97206caf-3b5b-40ba-9c16-0df1822e84ae.png">

2. Data extracted for first 100 rows from source and destination tables and compared, results in output folder of 
   rashmidesai09/ETL-pipeline-with-Python/Export from    SQL Server to PostgreSQL
