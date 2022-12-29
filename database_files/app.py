import random
import string
import io, os
from script import analyze
from flask import Flask, render_template, request, flash, redirect
from werkzeug.utils import secure_filename


dir_path = os.path.dirname(os.path.realpath(__file__))

ALLOWED_EXTENSIONS = set(['csv'])
UPLOAD_FOLDER = dir_path + '/uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]iasdfffsd/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files['file']
#         print(file)
#         # file = UPLOAD_FOLDER+'Car_details_v3.csv'
#         # data_for_function = io.BytesIO(file.read())
#         # analyze(data_for_function)
#         analyze(file)
#         # return render_template(f'{data_for_function}.html')
#         return render_template(f'{file.filename}.html')
#     else:
#         return render_template('index.html')

def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = get_random_string(8) + secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_path = UPLOAD_FOLDER + filename
     
        # data_for_function = io.BytesIO(file.read())
        analyze(file_path,filename)
        return render_template(f'{filename}.html')
    else:
        return render_template('index.html')


# app.run()
if __name__ == "__main__":
    app.run(host='0.0.0.0')
