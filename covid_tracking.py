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
#https://api.covidtracking.com/v1/us/daily.csv
#https://data.cdc.gov/api/views/9mfq-cb36/rows.csv
online_data = r'https://api.covidtracking.com/v1/us/daily.csv'
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
db_name="FluffyTrack"

# install pymysql and sqlalchemy
engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host=hostname, db=db_name, user=username, pw=passwd))
# review and download data
tables = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')
#tables = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')
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

#df = pd.read_sql_table('covid', connection)

months = ('Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020', 'Dec 2020', 'Jan 2021', 'Feb 2021', 'March 2021')
patients_cat = {
    'Hospitalized': (32.221, 784.533, 2561.872, 4038.095, 5535.849, 7723.933, 8799.572, 10414.102, 12283.586, 16262.903, 20134.520, 20714.612, 5405.727),
    'Deaths': (20.739, 881.423, 2587.987, 335.6899, 4071.555, 5012.258, 5648.154, 6528.270, 7206.395, 9269.261, 11931.561, 13240.568, 3571.866),
}

x = np.arange(len(months))  # the label locations
width = 0.45  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in patients_cat.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=2)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Number of Patients')
ax.set_title('Hospitalized & Death: The end of Pandemic CoV19')
ax.set_xticks(x + width, months)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(10, 21000)
plt.show()

connection.close
