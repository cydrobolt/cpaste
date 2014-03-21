
#CPaste - v.0.1

from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#Init SQLAlchemy
engine = create_engine("sqlite:///cpaste.db")

db_session = scoped_session(sessionmaker(bind=engine))
#Init Flask
app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/paste", methods=['GET','POST'])
def paste():
	pname = request.form['pname']
	pcontent = request.form['pcontent']
	return render_template('paste.html')



if __name__ == "__main__":
    app.run(debug=True)