import time
import pandas as pd
import numpy as np

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)
df['Start Time'] = pd.to_datetime(df['Start Time'])


# display the most common month
df['month'] = df['Start Time'].dt.month
popular_month = df['month'].mode()[0]
print('Most Frequent Month:', popular_month)


# display the most common day of week
df['dow'] = df['Start Time'].dt.day_name()
popular_dow = df['dow'].mode()[0]

print('Most Frequent Day of Week:', popular_dow)
# display the most common start hour


# convert the Start Time column to datetime


# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode()[0]

print('Most Frequent Start Hour:', popular_hour)
