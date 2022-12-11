#import needed libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os

#get password from environmnet var
pwd = os.environ['PGPASS']
uid = os.environ['PGUID']
server = 'localhost'
port = '5432'
db = "AdventureWorksDW2019"
dir = r'C:\Users\XXXX\PycharmProjects\pythonProject2'


#extract data from sql server
def extract():
    try:
        # starting directory
        directory = dir
        print(directory)
        # iterate over files in the directory
        for filename in os.listdir(directory):
            #get filename without ext
            file_wo_ext = os.path.splitext(filename)[0]
            print(file_wo_ext)
            # only process excel files
            if filename.endswith(".xlsx"):
                f = os.path.join(directory, filename)
                print(f)
                # checking if it is a file
                if os.path.isfile(f):
                    df = pd.read_excel(f)
                    print(df.head(5))
                    # call to load
                    load(df, file_wo_ext)
    except Exception as e:
        print("Data extract error: " + str(e))



#load data to postgres
def load(df, tbl):
    try:
        rows_imported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@localhost:5432/AdventureWorksDW2019')
        print(engine)
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
    df = extract()
except Exception as e:
    print("Error while extracting data: " + str(e))
