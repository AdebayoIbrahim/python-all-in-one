from flask import Flask,render_template

app = Flask(__name__, template_folder=r"C:\Users\SetUp\Documents\python_starter\web-development\templates")

#app.route decorator to create a link to our first webpage
@app.route("/")
def Home():
    return render_template("home.html")

#user form login welocme
@app.route("/login")
def Login():
    return render_template("login.html")

#submit-btn-functionality
@app.route("/login/details")
def about():
    return render_template("details.html")

# @app.route("/contact")
# def Contact():
#     return render_template("contact.html")


# #query parameters ,variable name in routes
# @app.route("/greet-<name>")
# def Greet(name):
#     return f"Welcome {name}, How are You Doing"

#if its in the current diretory
if __name__ == "__main__":
    app.run()