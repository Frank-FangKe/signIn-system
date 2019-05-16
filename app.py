from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/test"

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Stud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(80), nullable=False)
    Banj = db.Column(db.String(120), unique=False, nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    def __repr__(self):
      return '<Stud %r>' % self.user


@app.route('/')
def input_info():
    return render_template('input.html')

@app.route('/submit',methods=['GET','POST'])
def success():
    if request.method == 'GET':
        Xuehao = request.args.get("number")
        Mingzi = request.args.get("user")
        Dianh = request.args.get("phoneNum")
        Banji = request.args.get("class")
        print(Xuehao)
        print(Mingzi)
        log = Stud(number=Xuehao, user=Mingzi, Banj=Banji, phone=Dianh)
        db.session.add(log)
        return render_template('success.html')



@app.route('/warning')
def warning():
    return render_template('noMore.html')

if __name__ == '__main__':
    app.run()
