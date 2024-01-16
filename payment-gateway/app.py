from flask import Flask,render_template
import os

temp_fold = os.path.join(os.path.dirname(__file__),'templates')

app = Flask(__name__)


@app.rout("/")
def Home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()