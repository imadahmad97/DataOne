import pandas as pd
from pandas_profiling import ProfileReport
import os

def analyze(fl):
    raw = pd.read_csv(fl)
    pandas_profiling_report = raw.profile_report(
    title="Pandas Profiling Report", 
    explorative=True,
    html={'style': 
          {'full_width': True,
           'theme':'flatly'} 
        })
    pandas_profiling_report.to_file(f'templates/{fl}.html')


