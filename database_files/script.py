import pandas as pd
from pandas_profiling import ProfileReport

def analyze(fl,tm):
    raw = pd.read_csv(fl)
    pandas_profiling_report = raw.profile_report(
    title="Pandas Profiling Report",
    pool_size=0,
    explorative=True,
    html={'style': 
          {'full_width': True,
           'theme':'flatly'} 
        })
    pandas_profiling_report.to_file(f'templates/{tm}.html')
     