import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ('chicago','new york city','washington') 
    months = ('january','february','march','april','may','june','all')
    days = ('monday','tuesday','wednesday','thursday','friday','saturday','sunday','all')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to explore? (chicago, new york city, or washington): ').lower()
    while city not in(cities):
        print('Please enter a valid city. Try again.')
        city = input('Which city would you like to explore? (chicago, new york city, or washington): ').lower()
    print("\nLet's explore more about {}!\n".format(city))  
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month of bikeshare data would you like to explore? January, february, march, april, may, june or choose 'all': ").lower()
    while month not in(months):
        print('Please enter a valid month. Try again.')
        month = input("Which month of bikeshare data would you like to explore? January, february, march, april, may, june or choose 'all': ").lower()
    print("\nYou selected: {}\n".format(month))
   
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day of the week would you like to explore? Or choose 'all': ").lower()
    while day not in(days):
        print('Please enter a valid day of the week. Try again.')
        day = input("Which day of the week would you like to explore? Or choose 'all': ").lower()
    print("\nYou selected: {}\n".format(day))
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
    file = CITY_DATA.get(city)
    df = pd.read_csv(file, index_col=0, parse_dates=['Start Time','End Time'])
    df['Start Month'] = df['Start Time'].dt.strftime("%B")
    df['Start DoW'] = df['Start Time'].dt.strftime("%A")
    df['Start Hour'] = df['Start Time'].dt.strftime("%H")
    df['Station Combo'] = df['Start Station'] + " to " + df['End Station']
    
    month = month.capitalize()
    day = day.capitalize()
    
    #Filter the dataframe based on the user's selections
    if month != 'All' and day == 'All':
        df = df[df['Start Month']== month]
    elif day != 'All' and month == 'All':
        df = df[df['Start DoW']== day]
    elif day != 'All' and month != 'All':
        df = df[df['Start Month'] == month]
        df = df[df['Start DoW']== day]

    df = pd.DataFrame(df)
    return df

def view_data(df):    
    question = input("Would you like to preview the raw data for the city you choose? Yes/No: ").lower()
    x = 0
    y = 3
    #Print 5 rows of raw data at a time.
    while question == 'yes':
        question = input("Anser 'yes' to preview 5 rows of data at a time or 'no' to continue the analysis. ")
        if question != 'yes':
            break
        else:
            print(df.iloc[x:y])
            x += 3
            y += 3

    print("Let's continue our analysis.")
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Print the most popular month of travel.
    max_month = df['Start Month'].value_counts().idxmax()
    max_month_value = df['Start Month'].value_counts().max()
    print("\nThe most common month is {} with {} trips.".format(max_month,max_month_value))
    
    #Print the most popular day of the week for travel.
    max_dow = df['Start DoW'].value_counts().idxmax()
    max_dow_value = df['Start DoW'].value_counts().max()
    print("\nThe most common day of the week is {} with {} trips.".format(max_dow,max_dow_value))
    
    #Print the most popular start hour for travel.
    max_hour = df['Start Hour'].value_counts().idxmax()
    max_hour_value = df['Start Hour'].value_counts().max()
    print("\nThe most common start hour is {} with {} trips, on a 24-hour scale.\n".format(max_hour,max_hour_value))

    #Print the least popular month of travel.
    min_month = df['Start Month'].value_counts().idxmin()
    min_month_value = df['Start Month'].value_counts().min()
    print("\nThe least common month is {} with {} trips.".format(min_month,min_month_value))
    
    #Print the least popular day of the week for travel.
    min_dow = df['Start DoW'].value_counts().idxmin()
    min_dow_value = df['Start DoW'].value_counts().min()
    print("\nThe least common day of the week is {} with {} trips.".format(min_dow,min_dow_value))
    
    #Print the least popular start hour for travel.
    min_hour = df['Start Hour'].value_counts().idxmin()
    min_hour_value = df['Start Hour'].value_counts().min()
    print("\nThe least common start hour is {} with {} trips, on a 24-hour scale.\n".format(min_hour,min_hour_value))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    #Print the most popular start station of travel.
    max_st_station = df['Start Station'].value_counts().sort_values().index[-1]
    max_st_station_value = df['Start Station'].value_counts().max()
    print("\nThe most commonly used start station is {} with {} trips.".format(max_st_station,max_st_station_value))
    
    #Print the most popular destination station of travel.
    max_end_station = df['End Station'].value_counts().sort_values().index[-1]
    max_end_station_value = df['End Station'].value_counts().max()
    print("\nThe most commonly used end station is {} with {} trips.".format(max_end_station,max_end_station_value))   

    #Print the most popular combination of stations of travel.
    max_combo_station = df['Station Combo'].value_counts().sort_values().index[-1]
    max_combo_station_value = df['Station Combo'].value_counts().max()
    print("\nThe most frequent combination of start station and end station is {} with {} trips.".format(max_combo_station,max_combo_station_value))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    #Provide the total trip durations.
    travel_total = df['Trip Duration'].sum()
    print("\nThe total travel time is {}.".format(travel_total))
    
    #Provide the average trip duration.
    travel_avg = int(df['Trip Duration'].mean())
    print("\nThe average trip duration is {}.\n".format(travel_avg))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    #Provide the number of user types in the data set.
    user_types = df['User Type'].value_counts().sort_values()
    print("\nThe count of user types is as follows:\n",user_types)
    
    #Check whether there is data available about gender and birth year.
    if 'Gender' not in df:
        print("\nThere are no other user statistics recorded for the city of Washington.")
    else:
        #Print the count of each gender type.
        gender_cnt = df['Gender'].value_counts().sort_values()
        print("\nThe count of gender stats is as follows:\n",gender_cnt)
        
        #Provide statistics about birth years.
        earliest_yr = int(df['Birth Year'].min())
        recent_yr = int(df['Birth Year'].max())
        max_birth_yr = int(df['Birth Year'].value_counts().sort_values().index[-1])
        print("\nThe earliest year of birth is: {}\nThe most recent year of birth is: {}\nThe most common year of birth is: {}\n".format(earliest_yr,recent_yr,max_birth_yr))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        view_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()