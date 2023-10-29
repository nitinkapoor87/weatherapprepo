from flask import Flask,request,render_template
import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weatherapp',methods=['POST','GET'])
def get_weather():
    url='http://api.openweathermap.org/data/2.5/weather'
    params={'q':request.form.get('city'),'APPID':request.form.get('APPID')}
    resonse=requests.get(url,params=params)
    data=resonse.json()
    return f"{data}"


if __name__=='__main__':
    app.run(host='0.0.0.0')