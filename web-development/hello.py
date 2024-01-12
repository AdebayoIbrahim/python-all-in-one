from flask import Flask

app = Flask(__name__)

#app.route decorator to create a link to our first webpage
@app.route("/")
def welcome():
    return "Welcome!"

#if its in the current diretory
if __name__ == "__main__":
    app.run()