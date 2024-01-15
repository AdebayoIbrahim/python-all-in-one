from flask import Flask,request,render_template
import os
t_f = os.path.join(os.path.dirname(__file__),'templates')
import requests


app = Flask(__name__,template_folder=t_f)



#index page
@app.route('/')
def Index():
    return render_template('index.html')



url = r'https://api.openweathermap.org/data/2.5/weather?'



#submission
@app.route('/submit', methods = ["POST","GET"])
def submit():
    if request.method == 'POST':
        response = request.form
        # return response
        #send api request
        params = {
        'q': response['city'],
        'units': response['units'], 
        'appid':'e79e96fad8f4304aaa405f4a70fd29a4',
        }
        api_fetch = requests.get(url=url, params=params)
        data_res = api_fetch.json() 
        # return data_res
        send_data = {
            'city' : response['city'],
            'temp' : data_res['main']['temp'],
            'feels_like': data_res['main']['feels_like'],
            'weather':data_res['weather'][0]['description'],
            'wind': data_res['wind']['speed']
        }
        return render_template('results.html',payload = send_data)    
    else: 
        return "invalid method"





if __name__ == '__main__':
    app.run(debug=True)