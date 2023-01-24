# Ford GoBike Data - Exploratory Analysis

<center>
    <img src= "https://mtc.ca.gov/sites/default/files/images/GoBike_Launch_20.jpg" width="800" alt="cognitiveclass.ai logo" />
</center>

> visit website @ https://davidsonity-ford-gobike-app-t7q2i4.streamlit.app/


## Dataset

> This data set includes information about individual rides made in a bike-sharing system covering the greater San Francisco Bay area for the month of February 2019. For this project, the data was made available by Udacity with this link [dataset](https://video.udacity-data.com/topher/2020/October/5f91cf38_201902-fordgobike-tripdata/201902-fordgobike-tripdata.csv)

## Context
Data Cleaning and Data Analysis using both plotly and seaborn


### Summary of Findings
After cleaning and data exploration was done on the dataset, the following insights were acknowledged:
1. Most people ride the bike for around 10 minutes:
> This was found after plotting a histogram to show the average duration of rides. Because some outliers on the high end extremely skewed the data, a logrithmic transformation was done here.

2. People tends to ride more frequently during the weekdays than weekends
> This was found after plotting a bar chart to show what days in the week had more riders.

3. People ride more frequently between 7-9 AM and 4-6 PM.
> This was found after plotting a bar chart to show what hour in the day had more riders.

4. Majority of people taking the rides are between age 20 to 40
> This was found after plotting a histogram to show the distribution of riders by their age.

5. Majority of the people riding the bikes are Male
> This was found after plotting a barchart to show the various gender of riders

6. People between the ages of 20 to 60 tend to take the longest rides
> This was found after plotting a scatterplot to find the relationship between ride duration and rider's Age

7. Longer duration of ride are taken during the weekend(saturday and sunday).
> This is found after plotting a barchart to show the relationship between days of the week and ride duration

8. Although 3am has the lowest ride frequency, 3am has the longest ride duration
> This is found after plotting a barchart to show the relationship between hour of the day and ride duration

9. San Antomio Park, Palm St at Willow St, Foothill Blvd at 42nd Ave are the top 3 start stations with the longest ride duration
> This was found after plotting a horizontal barchart to show the relationship start stations and ride duration

10. Customers takes longer rides compared to subscribers
> This was found after plotting a boxplot to show the relationship between user-type and ride Duration

11. Both female and other gender rides longer trips then males.
> This was found after plotting a boxplot to show the relationship between gender and ride Duration

12. Irrespective of the gender, the durations taper off as a person gets older.
> This was found by plotting a scatter plot to show th relationship between gender, age aride duration.

### Website
https://davidsonity-ford-gobike-app-t7q2i4.streamlit.app/
