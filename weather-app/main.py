from flask import Flask,request,render_template
import os
t_f = os.path.join(os.path.dirname(__file__),'templates')



app = Flask(__name__,template_folder=t_f)



#index page
@app.route('/')
def Index():
    return render_template('index.html')

#submission
@app.route('/submit', methods = ["POST","GET"])
def submit():
    if request.method == 'POST':
        response = request.form

        return response
        #send api request    
    else: 
        return "invalid method"





if __name__ == '__main__':
    app.run(debug=True)