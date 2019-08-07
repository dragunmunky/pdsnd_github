import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

df.pd.read_csv('CITY_DATA[city])  

while True:
 city = input('Which city would you like to see data for:  Chicago, New York, or Washington?\n').lower()
 if city in ('chicago', 'new york city', 'washington'):
  return city
 else: print("Sorry, '{city.title()}' is not a valid city name.  Please type 'chicago', 'new york city' or 'washington'.')    

    # TO DO: get user input for month (all, january, february, ... , june)
months = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'}
df['month'] = df['Start Time'].dt.month
             
while True:
 month = input('Which month would you like to see data for?').lower()
 if months in months:
  return month
 else: 
  print("Sorry, '{month.title()}' is not a month name.  Please type 'january', 'february', 'march', 'april', 'may', 'june',    'july', 'august', 'september', 'october', 'november', or 'december'.")  
             
             
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
days = {'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'satuday'}
df = df[df['day_of_week'] == day.title()]
             
while True:
 day = input('Which day of the week would you like to see data for?').lower()
 if day in days:
  return day
 else: 
  print("Sorry, '{day.lower()}' is not a day of the week.  Please type 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',  or 'satuday'.")

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
popular_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
popular_hour = df['dt.weekday_name'].mode()[0]

    # TO DO: display the most common start hour
popular_hour = df['hour'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

popular_start_station = dt['Start Station'].mode(0)
             
print(popular_start_station)               
    # TO DO: display most commonly used end station
popular_end_station = dt['End Station'].mode(0)

print(popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip

popular_start_stop = dt['Start Station' and 'End Station'].mode(0)                    

print(popular_start_stop)
             
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    

    # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print(user_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest_birthyear = min['Birth Year']
    recent_birthdyear = max['Birth Year']
    most_common_birthyear = df['Birth Year'].mode()[0]

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
