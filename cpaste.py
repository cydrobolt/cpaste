
#CPaste - v.0.1

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
#Init SQLAlchemy
engine = create_engine("sqlite:///cpaste.db")

db_session = scoped_session(sessionmaker(bind=engine))
#Init Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "CPaste : Hello World!"

if __name__ == "__main__":
    app.run()