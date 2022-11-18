#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import pandas_profiling
from flask import Flask
import os


# In[9]:


def report_creator(file):
    raw_data = pd.read_csv(file)
    return pandas_profiling.ProfileReport(raw_data).to_file('Profile-Report')


# In[24]:


from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = '/Users/imadahmad/repos/DataOne/UPLOAD_FOLDER'

@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
       if request.files:
        image = request.files["image"]

        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

        print("Image Saved")

        return redirect(request.url)
   return render_template('upload.html')

app.run(port=5000)


# In[ ]:




