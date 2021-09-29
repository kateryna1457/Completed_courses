import json
from datetime import datetime
import pandas as pd

def parse_time(ts):
    return datetime.datetime.isoformat(ts)
#Call json.dumps(object) to convert
#the previous result object into a JSON object.

time_cols = ['tpep_pickup_datetime',
             'tpep_dropoff_datetime']

df = pd.read_csv(r'D:\Epam\Self_study\Python for Data Scientists\Exercise Files\Ch02\challenge\1.csv',
                 parse_dates = time_cols)

df.to_json(path_or_buf = r'D:\Epam\Self_study\Python for Data Scientists\Exercise Files\Ch02\challenge\taxi.jl',
           orient='records',
           date_format='iso')
