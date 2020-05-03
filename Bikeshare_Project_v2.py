#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime as dt
import pandas as pd
import numpy as np
import calendar


# In[ ]:


#Reading in raw data to help user view later
chicago_orig=pd.read_csv("chicago.csv")
newyork_orig=pd.read_csv("new_york_city.csv")
washington_orig=pd.read_csv("washington.csv")


# In[ ]:


chicago = pd.read_csv("chicago.csv")
chicago = chicago.dropna(how='any')
chicago['city']="chicago"
newyork = pd.read_csv("new_york_city.csv")
newyork = newyork.dropna(how='any')
newyork['city']="newyork"
washington = pd.read_csv("washington.csv")
washington = washington.dropna(how='any')
washington['city']="washington"


def get_filters():
    print("Hello! Lets explore some US bikeshare data!")
    check = False
    while check == False:
        city = input("Which city do you want to explore? (chicago, newyork, washington)")
        month = input("Which month do you want to explore(all, 1(jan), 2(feb), 3(mar), 4(apr), 5(may), 6(jun), 7(jul), 8(aug), 9(sep), 10(oct), 11(nov), 12(dec)")
        day = input("Which day do you want to explore(all, 0(mon), 1(tue), 2(wed), 3(thu), 4(fri), 5(sat), 6(sun)")
        if city == "chicago" or city == "newyork" or city == "washington":
            if month == "all" or month == "1" or month == "2" or month == "3" or month == "4" or month == "5" or month == "6" or month == "7" or month == "8" or month == "9" or month == "10" or month == "11" or month == "12":
                if day == "all" or day == "0" or day == "1" or day == "2" or day == "3" or day == "4" or day == "5" or day == "6":
                    check = True
        else:
            print("Please enter from the options in brackets")
            check = False
    print('_'*100)
    return city, month, day
    


# In[ ]:


chicago.head()


# In[ ]:


newyork.head()


# In[ ]:


washington.head()


# In[ ]:


chicago['Start Time'] = pd.to_datetime(chicago['Start Time'])
chicago["year"] = chicago["Start Time"].dt.year
chicago["month"] = chicago["Start Time"].dt.strftime("%B")
chicago["day"] = chicago["Start Time"].dt.strftime("%A")
chicago["hour"] = chicago["Start Time"].dt.strftime("%H")
chicago["combination"] = chicago["Start Station"] + " to " + chicago["End Station"]
chicago.head()                                      


# In[ ]:


newyork['Start Time'] = pd.to_datetime(newyork['Start Time'])
newyork["year"] = newyork["Start Time"].dt.year
newyork["month"] = newyork["Start Time"].dt.strftime("%B")
newyork["day"] = newyork["Start Time"].dt.strftime("%A")
newyork["hour"] = newyork["Start Time"].dt.strftime("%H")
newyork["combination"] = newyork["Start Station"] + " to " + newyork["End Station"]
newyork.head()


# In[ ]:


washington['Start Time'] = pd.to_datetime(washington['Start Time'])
washington["year"] = washington["Start Time"].dt.year
washington["month"] = washington["Start Time"].dt.strftime("%H")
washington["day"] = washington["Start Time"].dt.strftime("%H")
washington["hour"] = washington["Start Time"].dt.strftime("%H")
washington["combination"] = washington["Start Station"] + " to " + washington["End Station"]
washington.head()


# In[ ]:


chicago.count()
chicago["Birth Year"] = chicago["Birth Year"].astype(int)
chicago.head()


# In[ ]:


newyork.count()


# In[ ]:


washington.count()


# In[ ]:


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
    if city == "chicago":
        df = chicago
    elif city == "newyork":
        df = newyork
    else:
        df = washington
        
    if month == "all":
        df = df
    else:
        df = df[(df["month"] == int(month))]
        
    if day == "all":
        df = df
    else:
        df = df[(df["day"] == int(day))]
          
    return df


# In[ ]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month of travel is "+str(common_month))
          
    # display the most common day of week
    common_day = df['day'].mode()[0]
    print("The most common day of travel is "+str(common_day))

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour of travel is "+str(common_hour))
    
  
    print('_'*100)


# In[ ]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
  

    # display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print("The most common start station is "+str(common_startstation))

    # display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print("The most common end station is "+str(common_endstation))

    # display most frequent combination of start station and end station trip
    combination_endstation = df['combination'].mode()[0]
    print("The most common combination of start and end station is "+str(combination_endstation))

    
    print('_'*100)


# In[ ]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    

    # display total travel time
    Total = df['Trip Duration'].sum()
    print ("Total time travelled is ", str(Total))
    # display mean travel time
    average = df['Trip Duration'].mean()
    average = round(average,2)
    print ("Average time travelled is ", str(average))

    
    print('_'*100)


# In[ ]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print ("The counts of user types:")
    print(user_counts)
    
    # Display counts of gender
    if df.city.unique()==['chicago'] or df.city.unique()==['newyork']:
        gender_counts = df['Gender'].value_counts()
        print("\nThe counts of gender types:")
        print(gender_counts)
    else:
        print ("Gender not available for chosen city")
    
    # Display earliest, most recent, and most common year of birth
    if df.city.unique()==['chicago'] or df.city.unique()==['newyork']:
        common_birth=df['Birth Year'].mode()[0]
        birth_max = df['Birth Year'].max()
        birth_min = df['Birth Year'].min()
        print ("\nThe most recent year of birth is "+str(birth_max))
        print ("The earliest year of birth is "+str(birth_min))
        print ("The most common year of birth is "+str(common_birth))
    else:
        print ("Birth Year not available for chosen city")
        
    print('_'*100)


# In[ ]:


def raw_data(df):
    check = False
    index = 0
    while check == False:
        viewdata = input("Do you want to view five lines of raw data? Enter yes or no.")
        index += 5
        if viewdata == "yes":
            if df.city.unique()==['chicago']:
                print(chicago_orig.head(index))
            elif df.city.unique()==['newyork']:
                print(newyork_orig.head(index))
            else:
                print(washington_orig.head(index))
        else:
            check = True
    print('_'*100)


# In[ ]:


def main():
    while True:
        city, month, day = get_filters()
 
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


# In[ ]:


if __name__ == "__main__":
	main()

