# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# 1. import Flask
from flask import Flask, jsonify

#################################################
# Flask Setup
################################################## 
# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Connect to SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"<br/>Welcome to the Climate app!<br/>"
        f"<br/>"
        f"<br/>Available Routes:<br/>"
        f"<br/>Main page:<br/>"
        f"<br/>/<br/>"
        f"<br/>Precipitation data for year before August 23, 2017 (inclusive):<br/>"
        f"<br/>/api/v1.0/precipitation<br/>"
        f"<br/>List of stations:<br/>"
        f"<br/>/api/v1.0/stations<br/>"
        f"<br/>Temperature observations for year before August 23, 2017 (inclusive):<br/>"
        f"<br/>/api/v1.0/tobs<br/>"
        f"<br/>Min, Max and Avg temperatures for range beginning with specified start date up to last date on database:<br/> "
        f"<br/>/api/v1.0/temp/start_date (input date as MMDDYYYY) <br/>"
        f"<br/>Min, Max and Avg temperatures for range beginning with specified start date up to specified last date:<br/> "
        f"<br/>/api/v1.0/temp/start_date/end_date (input date as MMDDYYYY) <br/>"
    )
# Code for precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return the precipitation data for the last year"""
    # Calculate the date 1 year ago from last date in database
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query for the date and precipitation for the last year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= query_date).all()

    session.close()
    
    # Dict with date as the key and prcp as the value
    all_precipitation_dates = []
    for date, prcp in precipitation:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        all_precipitation_dates.append(precipitation_dict)
    
    # Return the results
    return jsonify(all_precipitation_dates=all_precipitation_dates)

# Code for stations route
@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    results = session.query(Station.station).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    stations = list(np.ravel(results))
    
    # Return the results
    return jsonify(stations=stations)

# Code for temperature observations route
@app.route("/api/v1.0/tobs")
def temp_monthly():
    """Return the temperature observations (tobs) for previous year."""
    # Calculate the date 1 year ago from last date in database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query the primary station for all tobs from the last year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    session.close()
    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))

    # Return the results
    return jsonify(temperatures=temps)

# Code for date statistics with start only or start and finish 
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats_range(start=None, end=None):
    
    """Return TMIN, TAVG, TMAX."""

    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
             
        # calculate TMIN, TAVG, TMAX for range of all dates greater than start
        start = dt.datetime.strptime(start, "%m%d%Y")
       
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()

        session.close()
        
        # Unravel results into a 1D array and convert to a list
        temps = list(np.ravel(results))
        
        # Return the results
        return jsonify(Range_temp_stats=temps)


    # calculate TMIN, TAVG, TMAX for range with start and end dates
    start = dt.datetime.strptime(start, "%m%d%Y")
    end = dt.datetime.strptime(end, "%m%d%Y")
    
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()

    session.close()

    # Unravel results into a 1D array and convert to a list
    temps = list(np.ravel(results))
    
    # Return the results
    return jsonify(Range_temp_stats=temps)

# Enable debug mode
if __name__ == '__main__':
    app.run(debug=True) 
 