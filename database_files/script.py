import pandas as pd
from pandas_profiling import ProfileReport

def analyze(fl, num):
    raw = pd.read_csv(fl)
    profile = ProfileReport(raw, title = "Report", explorative=True)
    profile.to_file(f'database_files/templates/{num}.html')