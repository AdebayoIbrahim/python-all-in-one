from flask import Flask

app = Flask(__name__)

#app.route decorator to create a link to our first webpage
@app.route("/")
def Home():
    return "Welcome!"



@app.route("/about")
def about():
    return "About page"

@app.route("/contact")
def Contact():
    return "Contact Page"
#if its in the current diretory
if __name__ == "__main__":
    app.run()