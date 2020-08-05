import time
import pandas as pd
import numpy as np
from scipy import stats
CITY_DATA = { 'chicago': 'chicago.csv',
'new york city': 'new_york_city.csv',
'washington': 'washington.csv' }

months = {'all','january','february','march','april','may','june'}

days = { 'all', 'sunday','monday','tuesday','wednesday','thursday','friday','saturday'}

def get_filters():
    while True:
        city = input('What city would you like to analyze? Chicago, New York City or Washington?: ').lower()

        if city in (CITY_DATA.keys()):
            print('You selected: ', city)
            break

        else:
            print("Not a valid city, please choose Chicago, New York City or Washington")


    while True:
        month = input('What month would you like to analyze? January, February, March, April or June?: ').lower()

        if month in (months):
            print('You selected: ', month)
            break
        else:
            print("Not a valid month, please choose from January, February, March, April, May or June")


    while True:
        day = input('What day would you like to analyze? Sunday, Monday, etc: ').lower()

        if day in (days):
            print('You selected: ', day)
            break
        else:
            print("Not a valid day, please choose Sunday, Monday,etc: ")



    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name


    df['hour'] = df['Start Time'].dt.hour

    try:
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]
        if day != 'all':
            df = df[df['day_of_the_week'] == day.lower()]

    except ValueError:
        print("Oops!")
        print("value error")
    return df
def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month=stats.mode(df['month'])

    most_common_dow=stats.mode(df['day_of_the_week'])

    most_common_month=stats.mode(df['hour'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()


def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station=stats.mode(df['Start Station'])

    most_common_end_station=stats.mode(df['End Station'])

    most_common_comb_station=stats.mode(df['Start Station']*df['End Station'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

    print("Total travel time:" + str(df["Trip Duration"].sum()))

    avg_travel_time=np.average(df["Trip Duration"])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df:
         gender = df['Gender'].value_counts()
         print("counts of gender = ",gender)

    else:
        print("not available information .")

    if 'Birth_Year' in df:

        earliest_year = df['Birth_Year'].min()
        print("Earliest year ",earliest_year)
        recent_year = df['Birth_Year'].max()
        print('Recent year ',recent_year)
        common_year = df['Birth Year'].mode()[0]
        print('The most common year',common_year)
    else:

        print("not available information .")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


i = 0
while True:

    display_more=input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
    if display_more=='yes':
        five_rows=df.iloc[:i+5]
        print(five_rows)
        i+= 5
    else:
        break


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
