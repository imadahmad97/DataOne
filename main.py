import pandas as pd
import pandas_profiling
from flask import Flask, render_template, send_file
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

def report_creator(uploaded_file):
    raw_data = pd.read_csv(uploaded_file)
    return pandas_profiling.ProfileReport(raw_data).to_file('/Users/imadahmad/repos/DataOne/RETURN_FOLDER/report.html')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'


class UploadFileForm(FlaskForm):
    file = FileField("File", validators = [InputRequired()])
    submit = SubmitField("Upload File")


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                               app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))
        send_file(report_creator(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                    app.config['UPLOAD_FOLDER'],
                                    secure_filename(file.filename))))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
