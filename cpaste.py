from flask import Flask,render_template,request,g,redirect
import sqlite3
import datetime
from baseencode import base62_encode,base62_decode
import pprint
from htmlescape import htmlesc
#Init Flask
app = Flask(__name__)
 
from models import db
db.init_app(app)

DATABASE = 'cpaste.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/<pastebv>")
def showpaste(pastebv):
    dbco = get_db()
    g.pastebv = pastebv
    decbase = pastebv
    findpaste = dbco.execute("SELECT `title`,`paste`,`timestamp`,`lang` FROM pastes WHERE id=?", (decbase,))
    tpi = findpaste.fetchall()
    if(tpi==[]):
        return render_template('404.html',pagename=pastebv)
    else:
        for row in tpi:
            tpititle = row[0]
            tpipaste = row[1]
            tpitimestamp = row[2]
            tpilang = row[3]

        return render_template('paste.html',pname=tpititle,pcontent=tpipaste,pdate=tpitimestamp,plang=tpilang)


@app.route("/paste", methods=['GET','POST'])
def paste():
    pname = request.form['pname']
    pcontent = request.form['pcontent']
    plang = request.form['codelang']
    if (len(plang)<1)|(len(pcontent)<1)|(len(pname)<1):
        return render_template('error.html',error="You may not leave fields empty. Go back and try again.")

    now = datetime.datetime.now()
    date = str(now.hour)+":"+str(now.minute)+":"+str(now.second)+", "+str(now.month)+"/"+str(now.day)+"/"+str(now.year)
    dbo = get_db()
    curride = dbo.execute("SELECT MAX(id) FROM pastes")
    dboq = curride.fetchall()
    for row in dboq:
        idresp = row[0]
    if((idresp==None)|(idresp==0)):
        currid = 1
    else:
        currid = int(idresp)+1

    baseidi = base62_encode(currid)
    ptuple = (pname,pcontent,date,plang,baseidi,)
    pasteit = dbo.execute("INSERT INTO pastes ('title','paste','timestamp','lang','baseid') VALUES(?,?,?,?,?);" , (ptuple))
    dbo.commit()
    purl = "/"+base62_encode(currid)
    return redirect(purl, code=302)
    #return render_template('paste.html', pname=request.form['pname'], pcontent=request.form['pcontent'],plang=request.form['codelang'])

@app.route("/tupletest")
def tupletest():
    tuples = ('one',2,'three','4',5,'6')
    for thetuples in tuples:
        print thetuples
    return "Check the console."
@app.route('/testdb')
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'
@app.route('/encbase/<bv>')
def encbase(bv):
    g.bv = bv
    nbv = base62_encode(bv)
    return nbv
@app.route('/decbase/<bvd>')
def decbase(bvd):
    g.bvd = bvd
    nbv = base62_decode(bvd)
    return nbv    


if __name__ == "__main__":
    app.run(debug=False)
