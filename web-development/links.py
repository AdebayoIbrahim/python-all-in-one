from flask import Flask,render_template

app = Flask(__name__)

#app.route decorator to create a link to our first webpage
@app.route("/")
def Home():
    return render_template("home.html")



@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def Contact():
    return render_template('contact.html')


# #query parameters ,variable name in routes
# @app.route("/greet-<name>")
# def Greet(name):
#     return f"Welcome {name}, How are You Doing"

#if its in the current diretory
if __name__ == "__main__":
    app.run()