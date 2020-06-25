import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Choose the city for which you want to see data - Chicago, New York or Washington:  ').title()
        if city not in ('Chicago', 'New York', 'Washington'):
            print('Sorry, I did not understand what you entered.')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Data is available from January through June.  Enter the month name for which you want to see data. For all months, enter All.  ').title()
        if month not in ('January','February', 'March', 'April', 'May', 'June', 'All'):
            print('Sorry, I did not understand what you entered.')
        else:
            break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of the week that you want to see data.  For all days, enter All.  ').title()
        if day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
            print('Sorry, I did not understand what you entered.')
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:  ', popular_month)


    # display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most Frequent Day of Week:  ', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:  ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:  ', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most Common End Station:  ', popular_end)

    # display most frequent combination of start station and end station trip

    popular_station_combo = (df['Start Station'] + ' | ' + df['End Station']).mode()[0]
    print('Most Frequent Combination of Start and End Stations:  ', popular_station_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total Travel Time:  ', total_duration)



    # display mean travel time
    avg_duration = df['Trip Duration'].mean()
    print('Average Travel Time:  ', avg_duration)

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts().to_frame()
    print('Counts of User Types:  ',user_types[0:2])

    # Check if Gender column exists
    if 'Gender' in df:

        #Display counts of gender
        genders = df['Gender'].value_counts().to_frame()
        print('\nCounts for Each Gender:  ',genders[0:2])

    # Check if Gender column exists
    if 'Birth Year' in df:

        # Display earliest, most recent, and most common year of birth
        earliest_yr = df['Birth Year'].min()
        latest_yr = df['Birth Year'].max()
        most_common_yr = df['Birth Year'].mode()[0]

        print('\nEarliest Birth Year:  ', int(earliest_yr))
        print('Most Recent Birth Year:  ', int(latest_yr))
        print('Most Common Birth Year:  ', int(most_common_yr))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def view_raw_data(df):
    """Displays raw data 5 rows at a time."""
    start = 0
    end = 5
    view_data = input('\nWould you to view the raw data? Enter yes or no.\n').lower()
    while view_data == 'yes':
        print(df.iloc[start:end])
        start += 5
        end +=5
        view_data = input('\nWould you to view the next 5 rows? Enter yes or no.\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
