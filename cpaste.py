
#CPaste - v.0.2

from flask import Flask,render_template,request,g
import sqlite3
from datetime import datetime,timedelta
#Init SQLite

DATABASE = 'cpaste.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

#Init Flask
app = Flask(__name__)

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def root():
    return render_template("index.html")

@app.route("/paste", methods=['GET','POST'])
def paste():
	pname = request.form['pname']
	pcontent = request.form['pcontent']
	date = datetime.date()
	pasteit = query_db("INSERT INTO pastes ('title','paste','timestamp') VALUES('?','?','?')", [pname,pcontent,date])
	return render_template('paste.html', pname=request.form['pname'], pcontent=request.form['pcontent'])

if __name__ == "__main__":
    app.run(debug=True)
