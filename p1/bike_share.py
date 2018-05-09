import time
import pandas as pd
import numpy as np
import calendar


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
    print('Hi! Let\'s explore some US bikeshare data!')
    
    # get user input for city (chicago, new york city, washington).
    city = input("What's the city do you want to explore? Chicago, New York City, or Washington?").lower()
    # if user input wrong format, use whhile to restart
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Oh...! It's seems like you type in invalid inputs. Let's start again! \n"
                     "What's the city do you want to explore? Chicago, New York City, or Washington?").lower()
    #notify the user what he/she was querying
    print("It's seems like you want to explore {}! If it is not the city you want, just restart the program!".format(city.title()))
    
    # get user input for month (all, january, february, ... , june)
    month = input("What's the month do you want to explore? All, January, February, March, April, May, or June?").lower()
    # if user input wrong format, use whhile to restart
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Oh...! It's seems like you type in invalid inputs. Let's start again! \n"
                     "What's the month do you want to explore? All, January, February, March, April, May, or June?").lower()
    #notify the user what he/she was querying
    print("It's seems like you want to explore in {}! If it is not the month you want, just restart the program!".format(month.title()))

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("What's the day of week do you want to explore? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
    # if user input wrong format, use whhile to restart
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Oh...! It's seems like you type in invalid inputs. Let's start again! \n"
                     "What's the day of week do you want to explore? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?").lower()
    #notify the user what he/she was querying
    print("It's seems like you want to explore {}! If it is not the city you want, just restart the program!".format(day.title()))
    print(' '*40)
    print('-'*40)
    print(' '*40)
    print("Just one moment! Your request will be process quickly!")
    print(' '*40)
    print('-'*40)
    print(' '*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    # extract month and day of week and hour from Start Time to create new columns
    #create a month(in number) column
    df['month'] = df['Start Time'].dt.month
    #create a month(in abbreviated name) column
    df['month_name'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    #create a day of week name
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #create a hour name
    df['start_hour'] = df['Start Time'].dt.hour


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

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel.
    Args:
        df - pandas DataFrame containing city data filtered by month and day
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        print out the statistic result for time data
    """

    print('\nCalculating The Top Frequent Times of Travel...\n')
    start_time = time.time()

    # display the table of top 3 common month for travling
    # if user choose "all"
    if month == 'all':
        #create a top 3 dataframe with descending order
        top_month = df['month_name'].value_counts().head(3).reset_index().rename(columns = {'index' :'month','month_name': 'number of users'})
        #reset index from 1 to 3
        top_month.index = np.arange(1, len(top_month) + 1)
        #print out the result
        print("\nWhat's the top 3 popular months for travling?")
        print(" "*40)
        print(top_month)
        print(" "*40)

    # display the top 3 common day of week for travling
    # if user choose "all"
    if day == 'all':
        #create a top 3 dataframe with descending order
        top_day = df['day_of_week'].value_counts().head(3).reset_index().rename(columns = {'index' :'day','day_of_week': 'number of users'})
        #reset index from 1 to 3
        top_day.index = np.arange(1, len(top_day) + 1)
        #print out the result
        print("\nWhat's the top 3 day of weeks for travling?")
        print(" "*40)
        print(top_day)
        print(" "*40)

    # display the top 3 common start hour
    #create a top 3 dataframe with descending order
    top_hour = df['start_hour'].value_counts().head(3).reset_index().rename(columns = {'index' :'Start Hour','start_hour': 'number of users'})
    #reset index from 1 to 3
    top_hour.index = np.arange(1, len(top_hour) + 1)
    #print out the result
    print("\nWhat's the top 3 hour for travling? (in 24-hour clock)")
    print(" "*40)
    print(top_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        df - pandas DataFrame containing city data filtered by month and day
    Returns:
        print out the statistic result for station data
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display top 3 commonly used start station
    #create a top 3 dataframe with descending order
    top_start_station = df['Start Station'].value_counts().reset_index().rename(columns = {'index' :'Start_Station','Start Station': 'number of users'})
    #reset index from 1 to 3
    top_start_station.index = np.arange(1, len(top_start_station) + 1)
    #print out the result
    print("\nWhat's the top 3 popular start station?")
    print(" "*40)
    print(top_start_station.head(3))


    # display top 3 most commonly used end station
    #create a top 3 dataframe with descending order
    top_end_station = df['End Station'].value_counts().reset_index().rename(columns = {'index' :'End_Station','End Station': 'number of users'})
    #reset index from 1 to 3
    top_end_station.index = np.arange(1, len(top_end_station) + 1)
    #print out the result
    print("\nWhat's the top 3 popular end station?")
    print(" "*40)
    print(top_end_station.head(3))

    # display top 3 most frequent combination of start station and end station trip
    # create a top 3 dataframe with descending order
    top_station = df['Start Station'].append(df['End Station']).value_counts().reset_index().rename(columns = {'index' :'Top Station',0: 'number of users'})
    #reset index from 1 to 3
    top_station.index = np.arange(1, len(top_station) + 1)
    #print out the result
    print("\nWhat's the top 3 station?")
    print(" "*40)
    print(top_station.head(3))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        df - pandas DataFrame containing city data filtered by month and day
    Returns:
        print out the statistic result for trip duration data
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time and convert it into hours
    total_travel_time = df['Trip Duration'].sum()//3600


    # display mean travel time and convert it into munites
    trip_mean = round(df['Trip Duration'].mean()/60,2)
    
    # number of traveller
    n_traveller = df['Unnamed: 0'].count()
    #print out the result
    print("Among the city, day and hour you specified,")
    print("\ntotal trip duration are about {} hours. Total number of traveller are {}. Average trip duration are about {} minites.".format(total_travel_time, n_traveller, trip_mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users.
    Args:
        df - pandas DataFrame containing city data filtered by month and day
        (str) name of the city to analyze
    Returns:
        print out the statistic result for users data
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type = df['User Type'].value_counts()
    print("\nThe numbers of users for each type:")
    print(" "*40)
    print(user_type)


    # Display counts of gender
    # if city in Chicago or New York City
    if city in ['chicago' ,'new york city'] :
        gender = df['Gender'].value_counts()
        print(" "*40)
        print("\nThe numbers of users for each gender:")
        print(" "*40)
        print(gender)
    else:
        print("Washington city has no gender data to show!")


    # Display earliest, most recent, and most top 3 common year of birth
    # if city in Chicago or New York City
    
    if city in ['chicago' ,'new york city']:
        # find the earliest birth year
        earliest = df['Birth Year'].min().astype(int)
        # find the most recent birth year
        most_recent = df['Birth Year'].max().astype(int)
        # most top 3 common year of birth and create a dataframe
        most_common = df['Birth Year'].value_counts().head(3).reset_index().astype(int).rename(columns = {'index' :'Birth_Year','Birth Year': 'number of users'})
        #reset index from 1 to 3
        most_common.index = np.arange(1, len(most_common) + 1)
        #print out the result
        print("\nThe top 3 common birth year of users as follows:")
        print(" "*40)
        print(most_common)
        print("\nThe earliest birth year of users was born in {}!".format(earliest))
        print("\nThe most recent birth year of users was born in {}!".format(most_recent))
    else:
        print("Washington city has no birthday data to show!")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()



