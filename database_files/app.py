from script import analyze
import io
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        data_for_function = io.BytesIO(file.read())
        analyze(data_for_function)
        return render_template(f'{data_for_function}.html')
    else:
        return render_template('index.html')

app.run()

