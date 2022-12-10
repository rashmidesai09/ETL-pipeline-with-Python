-- create DB "AdventureWorksDW2019"
CREATE DATABASE "AdventureWorksDW2019"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_India.1252'
    LC_CTYPE = 'English_India.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
    
    
   
    
--create etl user
CREATE USER etl WITH PASSWORD 'demopass';
--grant connect
GRANT CONNECT ON DATABASE "AdventureWorksDW2019" TO etl;
--grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO etl;
