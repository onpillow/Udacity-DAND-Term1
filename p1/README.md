# P1: Explore US Bikeshare Data
## Overview
In this project, I wrote a Python script to create an interactive exprience in the terminal to present statistics for US Bikeshare Data in three major cities.
Through the interactive exprience, user would get summary statistics of bike share systems in Chicago, New York City, or Washington. The statistics include: top 3 common birth year of users, top 3 popular start station, etc. For more statistics details, see [Statistics Computed](#statistics-computed).
The data time period is the first six months of 2017, user can filter data by month, week day of week, or just investigate all duration.
## Installation and Requirements
- Python v3.6 or later.
- Download all three [data files](https://github.com/onpillow/Udacity-DAND-Term1/tree/master/p1/bikeshare_rawdata), be sure to include the raw data `chicago.csv`,
`new_york_city.csv`, and `washington.csv`.
- Download `bike_share.py` file from the [repo](https://github.com/onpillow/Udacity-DAND-Term1/tree/master/p1), and put it with `chicago.csv`,`new_york_city.csv`,`washington.csv`in the same folder.
- Run `bike_share.py`.
## Statistics Computed

### 1. Popular times of travel (i.e., occurs most often in the start time)

- top 3 popular months for travling
- top 3 day of weeks for travling
- top 3 hour for travling
### 2. Popular stations and trip
- top 3 popular start station
- top 3 popular end station
- top 3 station(combine start and end stations)
### 3. Trip duration
- total travel time
- average travel time
### 4. User info

- numbers of users for each type(Subscriber/Customer)
- counts of each gender (only available for NYC and Chicago)
- top 3 common birth year of users
- earliest, most recent year of birth (only available for NYC and Chicago)
## Example Output(partail output)
```
Hi! Let's explore some US bikeshare data!

What's the city do you want to explore? Chicago, New York City, or Washington?chicago
It's seems like you want to explore Chicago! If it is not the city you want, just restart the program!

What's the month do you want to explore? All, January, February, March, April, May, or June?all
It's seems like you want to explore in All! If it is not the month you want, just restart the program!

What's the day of week do you want to explore? All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?all
It's seems like you want to explore All! If it is not the city you want, just restart the program!
                                        
----------------------------------------
                                        
Just one moment! Your request will be process quickly!
                                        
----------------------------------------

Calculating The Top Frequent Times of Travel...
What's the top 3 day of weeks for travling?
                                        
       day  number of users
1  Tuesday            45912
2   Monday            44881
3   Friday            43922
                                        
----------------------------------------

Calculating The Most Popular Stations and Trip...

What's the top 3 station?
                    Top Station  number of users
1       Streeter Dr & Grand Ave            14423
2  Clinton St & Washington Blvd             8472
3     Lake Shore Dr & Monroe St             8305
----------------------------------------

Calculating Trip Duration...

Among the city, day and hour you specified,

total trip duration are about 78019 hours. Total number of traveller are 300000. Average trip duration are about 15.6 minites.

----------------------------------------

Calculating User Stats...
The numbers of users for each type:
                                        
Subscriber    238889
Customer       61110
Dependent          1
Name: User Type, dtype: int64

----------------------------------------
Would you like to restart? Enter yes or no.
no
```
## License
[MIT License](https://github.com/onpillow/Udacity-DAND-Term1/blob/master/p1/LICENSE)