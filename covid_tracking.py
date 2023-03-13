# Celine Watcharaapakorn-Smith
# Abibatou Diop
# Bashar Abduljaleel
# 03.05.23
# Group Project on The COVID Tracking https://data.cdc.gov/api/views/9mfq-cb36/rows.csv

import mysql.connector
import csv
import numpy as np
import pandas as pd
import datetime
from sqlalchemy import create_engine
from sqlalchemy import text
import matplotlib.pyplot as plt

# # Reviewing the data # #
online_data = r'https://data.cdc.gov/api/views/9mfq-cb36/rows.csv'
tables = pd.read_csv(online_data)
print(tables.head(10))  # getting first 10 entries of dataframe
print(tables.tail(10))  # getting last 10 entries of dataframe
# how big is this data
tables.shape
print("This data has {} rows and {} columns.".format(tables.shape[0], tables.shape[1]))
# review columns
print(tables.columns)
# review variable types and names
print(tables.dtypes)

# install cryptography
hostname="127.0.0.1"
username="root"
passwd=""
db_name="covidtracking"

# install pymysql and sqlalchemy
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=db_name, user=username, pw=passwd))
# review and download data
tables = pd.read_csv('https://data.cdc.gov/api/views/9mfq-cb36/rows.csv')
tables.rename(columns = {'submission_date':'date'}, inplace=True) #rename for better understanding on data

# connect to db
connection=engine.connect()
# create table
tables.to_sql('covid', con = engine, if_exists = 'append')
# create second table for DISC details
connection.execute(text('CREATE TABLE covid_2 Like covid'))
connection.execute(text('INSERT INTO covid_2 SELECT DISTINCT * FROM covid'))
# drop covid table and rename covid_2 to covid
connection.execute(text('DROP TABLE covid'))
connection.execute(text('ALTER TABLE covid_2 RENAME TO covid'))

# https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html
df = pd.read_sql_table('covid', connection)

# # prepping plots
# https://pandas.pydata.org/docs/reference/plotting.html




plt.show()
connection.close

