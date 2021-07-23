#!/usr/bin/env python
# coding: utf-8

# In[4]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    city = input('\nwhich city do you like to see data for it : Chicago, New York, or Washington? ').lower()
    if city in CITY_DATA.keys():
        print(f'You have chosen: {city}')
        
    else:
        while city not in CITY_DATA.keys():
            print('\nSorry we were not able to get the name of the city to analyze data')
            city = input('please write full name of city to see data for it : Chicago, New York, or Washington? ').lower()
    
    months = ['january', 'february', 'march', 'april', 'may', 'june','all'] 
    month = input(f'\nplease choose the month or (all)for not filtering by month:{months}').lower()
    if month  in months:
        print(f'You have chosen: {month}')
        
    else:
        while month not in months:
            print('\nSorry we were not able to get the name of the month to analyze data')
            month= input('please rewrite full name of the month or all for not filtering by month ').lower()
        
    days= ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    day=input(f'\nplease choose the day or (all) for not filtering by day:\n {days} ').lower()
    if day in days :
        print(f'You have chosen: {day}')
       
    else:
        while day not in days :
            print('\nSorry we were not able to get the name of the day to analyze data')
            day= input('please choose the particular day or (all) for not filtering by day ').lower()
            

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
    df['End Time'] = pd.to_datetime(df['End Time'])
    

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = df['month'].mode()[0]
    print(f'The most common month is: {months[month-1]}')


    # display the most common day of week
    common_day=df['day_of_week'].value_counts().idxmax()
    print(f'the most common day is : {common_day}')
    

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour=df['hour'].value_counts().idxmax()
    print(f'the most common start hour is : {common_hour}')
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].value_counts().idxmax()
    print(f'the most commonly used start station: {start_station}')
    


    # display most commonly used end station
    end_station=df['End Station'].value_counts().idxmax()
    print(f'the most commonly used start station: {end_station}')
    
    

    # display most frequent combination of start station and end station trip
    start_end_station=df['Start Station'] + '=====>' + df['End Station']
    print(f"the most common trip: {start_end_station.value_counts().idxmax()}")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 




def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    df['travel time']=df['End Time']-df['Start Time']
    total_travel_duration=df['travel time'].sum()
    
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds 
    minutes = total_travel_duration.seconds 
    seconds = total_travel_duration.seconds
    print(f'Total travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')

    # display mean travel time
    total_travel_duration=df['travel time'].mean()
    
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds 
    minutes = total_travel_duration.seconds 
    seconds = total_travel_duration.seconds
    print(f'mean for travel time is: {days} days {hours} hours {minutes} minutes {seconds} seconds')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print(user_types)
      
    # Display counts of gender
    if'Gender' in (df.columns):
        counts_gender=df['Gender'].value_counts()
        print(f"\n\n {counts_gender}")
    else:
        print('Gender: data is not avalibal!')


    # Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in (df.columns):
        earliest_year=int(df['Birth Year'].min())
        recent_year=int(df['Birth Year'].max())
        common_year=int(df['Birth Year'].value_counts().idxmax())
        print(f"\n\nearliest birth year is: {earliest_year}\nrecent birth year is: {recent_year} \nmost common year is: {common_year}")
    else:
         print('Birth Year: data is not avalibal!')
            
            
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def display_raw_data(df):
    """Ask to display 5 raw data on bikeshare  """
    raw = input('\nWould you like to display 5 raw data? Enter yes or no\n').lower()
    choise=['yes','y','ye']
    count = 0
    while raw in choise:
        print(df.iloc[count: count+5])
        count += 5
        ask = input('Would you like to see Next 5 raws yes or no?').lower()
        choise=['yes','y','ye']
        if ask.lower() not in  choise :
            break

def main():
    choise=['yes','y','ye']
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
       

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() not in  choise:
            break


if __name__ == "__main__":
	main()



# In[ ]:





# In[ ]:





# In[ ]:




