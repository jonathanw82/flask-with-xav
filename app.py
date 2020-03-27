import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", page_title="Index Page")


@app.route("/nextpage") 
def nextpage():
    mylist =["hello","world"]
    return render_template("nextpage.html", page_title="Next Page", mylist=mylist)


if __name__ == "__main__":
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=int(os.environ.get('PORT', 5000)),
            debug=True) 