import os

from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime

def report_creator(uploaded_file):
    raw_data = pd.read_csv(uploaded_file)
    return pandas_profiling.ProfileReport(raw_data).to_file('/Users/imadahmad/repos/DataOne/RETURN_FOLDER/report.html')


ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_location = os.path.join('input', new_filename)
            file.save(save_location)

            output_file = report_creator(save_location)
            #return send_from_directory('output', output_file)
            return redirect(url_for('download'))

    return render_template('upload.html')


@app.route('/download')
def download():
    return render_template('download.html', files=os.listdir('output'))


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename)


app.run(port=8000)

