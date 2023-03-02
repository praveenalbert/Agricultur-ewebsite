from flask import Flask, render_template, request,redirect
import pickle
import numpy as np
import random
import openai
model = pickle.load(open(r'D:\p\freshshop\Market.pkl','rb') )

app = Flask(__name__)



@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='POST':
        data1 = request.form['l']
        data2 = request.form['v']
        data3 = request.form['s']
        data4 = request.form['m']
        data5= request.form['t']
        data6= request.form['vc']
        data7= request.form['q']
        data8= request.form['e']
        data7=int(data7)
        pred=random.choice([30,50,70,25,25,130,10,35,35,45,75,45,90,30,40,15,12,50,10,35,35,45,40,45,20,80,30,20,70,20,25,30])
        
        #pred = model.predict(arr)
        return render_template('result.html',data=pred*data7,veg=data2)
    return render_template('home.html')

@app.route('/c')
def commnd():
    return render_template("commnd.html")

@app.route('/weather')
def weather():
    return render_template("weather.html")

@app.route('/c', methods=['POST','GET'])
def Chatgpt():
    if request.method=='POST':
        openai.api_key="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"
        model_engine="text-davinci-003"
        prompt=request.form['command']
        #if 'exit' in prompt or 'quit' in prompt:
         #       break
        completion=openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,stop=None,
            temperature=0.5
            )
        response=completion.choices[0].text
        return render_template('commnd.html',res=response)

if __name__ == "__main__":
    app.run(debug=True)
