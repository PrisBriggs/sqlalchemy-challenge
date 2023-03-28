# sqlalchemy-challenge

Georgia Tech Data Analytics BootCamp - March 2023

Homework Module 10 - SQLAlchemy Challenge
By Priscila Menezes Briggs

Challenge history
I've decided to treat myself to a long holiday vacation in Honolulu, Hawaii. To help with my trip planning, I gathered some data and decided to do a climate analysis about the area. 

My database consists of three files. Their contents are described below:

hawaii.sqlite: contains two tables as following:
    measurement: shows data about stations (column station), date (date), precipitation (prcp), temperature observations (tobs)
    station: stations (column station), name of station (name), latitude of station (latitude), longitude of station (longitude), elevation of station (elevation)

The sqlite file is also available in two separate .csv files:
hawaii_measurements.csv
hawaii_stations.csv

For this project, I used Python and SQLAlchemy to do a basic climate analysis and data exploration of my climate database. Specifically, I used SQLAlchemy ORM queries, Pandas, and Matplotlib. In addition, I designed my Climate App using Flask based on the queries that I developed. The sections below outline the steps that I took to accomplish this task.

Part 1: Analyzing and Exploring the Climate Data

    Precipitation Analysis
    In this section:
    - I found the most recent date in the dataset.
    - Using that date, I got the previous 12 months of precipitation data by querying the previous 12 months of data.
    - I plotted the results by using the DataFrame and a bar chart.
    - Finally, I printed the summary statistics for the precipitation data.

    Station Analysis
    In this section:
    - I designed a query to calculate the total number of stations in the dataset.
    - I designed a query to find the most-active stations (that is, the stations that have the most rows). 
    - I designed a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query.
    - Finally, I plotted the results as a histogram.

Part 2: Designing My Climate App
    In this section, I designed a Flask API based on the queries that I developed. I used the following routes:
    - / : This is the homepage, where all the available routes are listed.
    - /api/v1.0/precipitation : I converted the query results from my precipitation analysis (i.e. retrieving only the last 12 months of data) to a dictionary,
    - /api/v1.0/stations : This shows a list of stations from the dataset.
    - /api/v1.0/tobs : I made a query for the dates and temperature observations of the most-active station for the previous year of data.
    - /api/v1.0/temp/<start> : Shows a list of the minimum temperature, the average temperature, and the maximum temperature for all the dates greater than or equal to the specified start date.
    - /api/v1.0/temp/<start>/<end> : Shows a list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date and end date, calculating TMIN, TAVG, and TMAX for those dates from the start date to the end date, inclusive.

Data Analysis

The queries could show, among other results, that the most common temperatures during a year in Hawaii range from 70 to 80 degrees Fahrenheit. The average temperature detected by one of the stations was 71.6 degrees Fahrenheit. In additon, the periods with the highest precipitation levels found are between August and November and also between April and July. However, the average precipitation is only 0.17 in. These queries calculated accurate results in order to complete my research project. 

The file "climate_starter_Priscila.ipynb" inside the SurfsUp folder contains the script for the queries of this project, while the file "app.py" contains the Climate app. 

The script for this challenge is found in the GitHub's repository on:
https://github.com/PrisBriggs/sqlalchemy-challenge

The references used in this Challenge were the activities and lessons given in class in addition to the websites below. 

All webpages were visited in March/2023.

References:

https://www.projectpro.io/recipes/convert-string-datetime-in-python
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
https://matplotlib.org/2.0.2/users/legend_guide.html
https://www.w3schools.com/python/matplotlib_grid.asp
https://flask.palletsprojects.com/en/2.2.x/debugging/
