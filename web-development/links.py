import os
from flask import Flask,render_template,request

t_f = os.path.join(os.path.dirname(__file__),'templates')

app = Flask(__name__, template_folder=t_f)

#app.route decorator to create a link to our first webpage
@app.route("/")
def Home():
    return render_template("home.html")

#user form login welocme
@app.route("/login")
def Login():
    return render_template("login.html")

#submit-btn-functionality
@app.route("/submit",methods = ["POST","GET"])
def submit():
    if request.method == 'POST':
        result = request.form
        return render_template("details.html",details=result)
    else:
        return "Invalid Parameter"
    # try:
    #     return render_template("details.html")
    # except Exception as error:
    #     print('Error'.format(error))

    
    

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