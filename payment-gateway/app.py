from flask import Flask,render_template
import os

app = Flask(__name__)


@app.rout("/")
def Home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()