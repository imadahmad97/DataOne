import pandas as pd
from pandas_profiling import ProfileReport
from flask import render_template

def analyze(fl, idx):
    raw = pd.read_csv(fl)
    profile = ProfileReport(raw, title = "Report", explorative=True)
    profile.to_file(f'database_files/templates/{idx}.html')