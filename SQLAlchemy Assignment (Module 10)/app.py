# I cant get this part to work

# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
database_path = "../Resources/hawaii.sqlite"
engine = create_engine(f"sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

@app.route("/")
def welcome():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #create session link
    session = Session(engine)
    #query the last 12 months of precip data
    cutoff_date = '2016-08-23'
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > cutoff_date).all()
    session.close()

     precip_data = []
    for date, prcp in results:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        precip_data.append(precip_dict)

    return jsonify(precip_data)
# I cant get this part to work

#################################################
# Flask Routes
#################################################
