# Ford GoBike Data - Exploratory Analysis

![Ford GoBike](https://mtc.ca.gov/sites/default/files/images/GoBike_Launch_20.jpg)

This project aims to explore and analyze a dataset from the Ford GoBike bike-sharing system, covering the greater San Francisco Bay area for the month of February 2019. The data set includes information about individual rides made in the bike-sharing system.

## Dataset

The dataset used for this analysis can be accessed through this link: [Ford GoBike Dataset](https://video.udacity-data.com/topher/2020/October/5f91cf38_201902-fordgobike-tripdata/201902-fordgobike-tripdata.csv). It provides information about individual rides made during February 2019.

## Data Cleaning

Before conducting the analysis, the dataset underwent a data cleaning process to ensure the quality and integrity of the data. The cleaning process involved handling missing values, removing duplicates, and formatting data types as needed.

## Exploratory Analysis

Several explorations were conducted on the dataset to gain insights into the bike-sharing system and its riders. Here are some of the key findings:

1. **Ride Duration**: The majority of people ride the bike for around 10 minutes, with a right-skewed distribution. A logarithmic transformation was applied to handle outliers on the high end.

2. **Weekday vs. Weekend**: Bike rides are more frequent on weekdays compared to weekends, indicating higher usage for commuting purposes.

3. **Peak Hours**: The peak hours for bike rides are between 7-9 AM and 4-6 PM, aligning with typical commuting hours.

4. **Age Distribution**: The majority of riders fall between the ages of 20 to 40, indicating a younger user base.

5. **Gender Breakdown**: Male riders constitute the majority of bike users, although the dataset includes other gender options as well.

6. **Age and Ride Duration**: People between the ages of 20 to 60 tend to take the longest rides, indicating varying usage patterns across different age groups.

7. **Weekend Rides**: Longer rides are taken during the weekends, specifically on Saturdays and Sundays, potentially indicating leisure or recreational usage.

8. **Hourly Durations**: Ride durations are longest at 3 AM, which has the lowest ride frequency, suggesting that these rides may be outliers or unique in nature.

9. **Start Station Analysis**: The top three start stations for long rides are San Antonio Park, Palm St at Willow St, and Foothill Blvd at 42nd Ave, highlighting popular starting points for extended rides.

10. **Customer vs. Subscriber**: Customers (non-subscribers) tend to take longer rides compared to subscribers, indicating different usage patterns between these two user types.

11. **Gender and Ride Duration**: Female and other genders tend to take longer rides compared to males, indicating potential differences in riding behavior.

12. **Age and Ride Duration**: Regardless of gender, ride durations tend to taper off as a person gets older, suggesting that older individuals may opt for shorter rides.

### Additional Links

To view the interactive website for this analysis, visit: [Ford GoBike App](https://davidsonity-ford-gobike-app-t7q2i4.streamlit.app/)

For a more detailed exploration using Plotly, check out the Jupyter notebook on GitHub: [Plotly Notebook](https://github.com/Davidsonity/Ford-GoBike/blob/main/Plotly-EDA.ipynb)

For a comprehensive analysis, please refer to the complete notebook or analysis report.
