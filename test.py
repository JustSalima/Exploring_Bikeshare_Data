import time
import pandas as pd
import numpy as np


# load data file into a dataframe
df = pd.read_csv('chicago.csv')
#print(df.info())
# convert the Start Time column to datetime
#df['Start Time'] = pd.to_datetime(df['Start Time'])

# extract month and day of week from Start Time to create new columns
#df['month'] = df['Start Time'].dt.month
#df['day'] = df['Start Time'].dt.day_name()
#df['hour'] = df['Start Time'].dt.hour
#print(df['month'])
#print(df['day'])
#print(df['hour'])
# filter by month if applicable
#print(df.head())
#print(df['Trip Duration'].max())
#print(df['Trip Duration'].mean())
#print(df['Trip Duration'].sum())
user_types = df['User Type'].value_counts().to_frame()
print('Counts of User Types:\n',user_types[0:2])
