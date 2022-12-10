#import needed libraries
import msvcrt

from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os


#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
#sql db details
driver = "{SQL Server Native Client 11.0}"
server = "LAPTOP-64O143FA\MSSQLSERVER01"
database = "AdventureWorksDW2019"

#extract data from sql server
def extract():
    try:
        print("Establishing connection")
        connstr = 'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';Trusted_Connection=yes;' +';UID=' + uid + ';PWD=' + pwd
        print(connstr)
        src_conn = pyodbc.connect(connstr)
        if src_conn is not None:
            print("SQL Server Connection established successfully")
        else:
            print("Could not establish connection to SQL Server")
            return

        src_cursor = src_conn.cursor()
        # execute query
        src_cursor.execute(""" select  t.name as table_name
        from sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductSubcategory','DimProductCategory','DimSalesTerritory','FactInternetSales') """)
        src_tables = src_cursor.fetchall()
        for tbl in src_tables:
            #query and load save data to dataframe
            df = pd.read_sql_query(f'select * FROM {tbl[0]}', src_conn)
            #print("Read table completed. Press any key..")
            #msvcrt.getch()
            #print(df)
            #print("trying to Load table. Press any key..")
            #msvcrt.getch()
            load(df, tbl[0])

    except Exception as e:
        print("Data extract error: " + str(e))
    finally:
        src_conn.close()

#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        #engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/AdventureWorksDW2019')
        engine = create_engine(f'postgresql://{uid}:{pwd}@localhost:5432/AdventureWorksDW2019')
        print(engine)
        #"postgresql+pg8000://scott:tiger@localhost/test"
        #if engine is not None:
        #    print("PostGres SQL server Connection established successfully")
        #else:
        #    print("Could not establish connection to PostGres SQL Server")
        #    return
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {tbl}')
        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        # add elapsed time to final print out
        print("Data imported successful")
    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
