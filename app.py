import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu

df = pd.read_csv('clean_data.csv')

fig1 = px.histogram(df, x="duration_min")

fig1.update_traces(xbins=dict(  # bins used for histogram
    start=0.0,
    end=40.0,
    size=1
))

fig1.update_layout(
    height=500,
    width=800,
    bargap=0.1,
    title='Average Duration of Rides',
    xaxis_title='Duration in Minutes',
    yaxis_title='Rides Frequency'
)

fig2 = px.histogram(df, x="duration_min", log_x=True)

fig2.update_layout(
    height=500,
    width=800,
    bargap=0.1,
    title='Log scale Distribution of Ride duration',
    xaxis_title='Duration in Minutes',
    yaxis_title='Rides Frequency'
)

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hour_order = np.arange(0, 24)

fig3 = px.histogram(df, x="start_day",
                    color="start_day",
                    category_orders={"start_day": day_order})

fig4 = px.histogram(df, x="start_hour",
                    category_orders={"start_hour": hour_order},
                    barmode='group')

fig3.update_layout(title='Distribution of Days of the week',
                   xaxis_title='Day of the week',
                   yaxis_title='Rides Frequency'
                   )

fig4.update_layout(bargap=0.1,
                   title='Distribution of Hours in a day',
                   xaxis_title='Hour of the day',
                   yaxis_title='Rides Frequency'
                   )

fig5 = px.histogram(df, x="member_age", nbins=40)

fig5.update_layout(
    height=500,
    width=800,
    bargap=0.1,
    title='Number of Rides Based on Age of Member',
    xaxis_title='Age of Rider',
    yaxis_title='Number of Rides'
)

df_gender = df['member_gender'].value_counts().index
fig6 = px.histogram(df, x="member_gender",
                    color="member_gender",
                    category_orders={"member_gender": df_gender})

fig6.update_layout(
    height=500,
    width=800,
    title='Usage by Gender',
    xaxis_title='Gender',
    yaxis_title='Number of people'
)

df_user = df['user_type'].value_counts().index
fig7 = px.histogram(df, x="user_type",
                    color="user_type",
                    category_orders={"user_type": df_user})

fig7.update_layout(
    height=500,
    width=800,
    title='Number of Users per User Type',
    xaxis_title='User Type',
    yaxis_title='Number of Users'
)

fig8 = px.scatter(df, x="member_age", y="duration_min", opacity=0.5)

fig8.update_layout(
    height=600,
    width=850,
    title='Relationship between Ride duration and Rider\'s Age',
    xaxis_title='Age of Rider',
    yaxis_title='Ride duration in minutes'
)

day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
hour_order = np.arange(0, 24)

fig9 = px.histogram(df, x="start_day",
                    y='duration_min',
                    color="start_day",
                    histfunc='avg',
                    category_orders={"start_day": day_order})

fig10 = px.histogram(df, x="start_hour",
                     y='duration_min',
                     histfunc='avg',
                     category_orders={"start_hour": hour_order}
                     )

fig9.update_layout(height=500,
                   width=900,
                   title='Relationship between Ride Duration and Day of the week',
                   xaxis_title='Day of the week',
                   yaxis_title='Ride Duration in minutes'
                   )

fig10.update_layout(height=500,
                    width=850,
                    bargap=0.1,
                    title='Distribution of Hours in a day',
                    xaxis_title='Hour of the day',
                    yaxis_title='Ride Duration in minutes'
                    )

# find average ride duration for start station and select the top 10 start stations
start_station = df.groupby('start_station_name')[['duration_min']].mean().reset_index()
start_station = start_station.sort_values(['duration_min'], ascending=False).head(10)

fig11 = px.histogram(start_station, x="duration_min",
                     y='start_station_name',
                     color="start_station_name"
                     )

fig11.update_layout(height=500,
                    width=900,
                    title='Top 10 Long Ride Start Stations',
                    xaxis_title='Ride Duration in minutes',
                    yaxis_title='Start Stations')

# hiding legend
fig11.update_traces(showlegend=False)

# hiding legend
fig11.update_traces(showlegend=False)

fig12 = px.box(df, x="member_gender", y="duration_min", color="member_gender",
               category_orders={"member_gender": ['Male', 'Female', 'Other']})

fig12.update_layout(yaxis_range=[-10, 50],
                    height=550,
                    width=850,
                    title='Ride Duration across Gender Types',
                    xaxis_title='Gender',
                    yaxis_title='Ride Duration in minutes')

fig13 = px.box(df, x="user_type", y="duration_min", color="user_type")

fig13.update_layout(yaxis_range=[-10, 50],
                    height=550,
                    width=850,
                    title='Ride Duration between Customers and Subscribers',
                    xaxis_title='User Type',
                    yaxis_title='Ride Duration in minutes')

fig14 = px.scatter(df, x="member_age", y="duration_min", color="member_gender", symbol="member_gender",
                   category_orders={"member_gender": ['Male', 'Female', 'Other']})

fig14.update_layout(height=550,
                    width=850,
                    title='Ride Duration Across Ages and Genders',
                    xaxis_title='Age',
                    yaxis_title='Ride Duration in minutes')

dff = df.groupby(['start_day', 'user_type'], as_index=False).mean()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
fig15 = px.line(dff, x='start_day', y='duration_min', color='user_type', markers=True)

fig15.update_layout(height=550,
                    width=850,
                    title='Ride Duration per day per User Type',
                    xaxis_title='Day of the Week',
                    yaxis_title='Ride Duration in minutes')

####################################################################
# streamlit
##################################################################

st.title("Ford GoBike Data - EDA")

selected = option_menu(
    menu_title='Analysis',
    options=['Home', 'Univariate', 'Bivariate', 'Multivariate'],
    icons=['house', 'graph-up', 'graph-up', 'graph-up'],
    menu_icon='bar-chart',
    orientation='horizontal'
)

if selected == 'Home':
    st.image(
        'https://mtc.ca.gov/sites/default/files/images/GoBike_Launch_20.jpg'
    )
    st.markdown(
    "> This data set includes information about individual rides made in a bike-sharing system covering the "
    "greater San Francisco Bay area for the month of February 2019. For this project, the data was made "
    "available by Udacity")

if selected == 'Univariate':
    st.markdown('## Univariate Exploration')
    st.markdown('> In this section, I investigated distributions of individual variables. I took a deeper look '
                'to clean things up '
                'and prepare myself to look at relationships between variables.')
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)
    st.plotly_chart(fig3)
    st.plotly_chart(fig4)
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)
    st.plotly_chart(fig7)

if selected == 'Bivariate':
    st.markdown('## Bivariate Exploration')
    st.markdown('> In this section, I investigated relationships between pairs of variables in my'
                'data that have been introduced in some'
                'fashion in the previous section (univariate exploration).')
    st.plotly_chart(fig8)
    st.plotly_chart(fig9)
    st.plotly_chart(fig10)
    st.plotly_chart(fig11)
    st.plotly_chart(fig12)
    st.plotly_chart(fig13)

if selected == 'Multivariate':
    st.markdown('## Multivariate Exploration')
    st.markdown(
        '> In this section, I would create plots of three or more variables to investigate my data even further.')
    st.plotly_chart(fig14)
    st.caption('For all gender, the durations taper off as a person gets older')

    st.plotly_chart(fig15)
