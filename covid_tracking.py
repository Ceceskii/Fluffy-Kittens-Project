# Celine Watcharaapakorn-Smith
# Abibatou Diop
# Bashar Q Abduljaleel
# 03.05.23
# Group Project on The COVID Tracking https://api.covidtracking.com/v1/us/daily.csv

import mysql.connector
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#connect to db
def connect_to_sql():
    conn = mysql.connector.connect(user='root', password='',
                                   host='127.0.0.1', database='CovidTracking')
    return conn

#create table
tables = pd.read_csv('https://api.covidtracking.com/v1/us/daily.csv')

