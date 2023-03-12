# Celine Watcharaapakorn-Smith
# Abibatou Diop
# Bashar Q Abduljaleel
# 03.05.23
# Group Project on The COVID Tracking https://data.cdc.gov/api/views/9mfq-cb36/rows.csv

import mysql.connector
import csv
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
import datetime
import matplotlib.pyplot as plt

# # Reviewing the data # #
online_data = r'https://data.cdc.gov/api/views/9mfq-cb36/rows.csv'
tables = pd.read_csv(online_data)
print(tables.head(10))  # getting first5 entries of dataframe
print(tables.tail(10))  # getting first5 entries of dataframe

# how big is this data
tables.shape
print("This data has {} rows and {} columns.".format(tables.shape[0], tables.shape[1]))
# review columns
print(tables.columns)
# review variable types and names
print(tables.dtypes)

# connect & create db
def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='',
                                   host='127.0.0.1', database='CovidTracking')
    return conn

####engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{hostname}/{database}")

# # create table 'covid' structure # #
#######def create_tables(cursor):





# # delete columns

