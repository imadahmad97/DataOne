from script import analyze
from io import BytesIO
from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:mdbpassword@databaseone.cyalagmldkju.us-west-2.rds.amazonaws.com/mariadbtest'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Upload(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     filename = db.Column(db.String(50))
#     data = db.Column(db.LargeBinary)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        # upload = Upload(filename=file.filename, data=file.read())
        # db.session.add(upload)
        # db.session.commit()
        data_for_function = BytesIO(file.read())
        analyze(data_for_function)
        return render_template(f'{data_for_function}.html')
    else:
        return render_template('index.html')

app.run()

