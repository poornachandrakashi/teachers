from flask import Flask,render_template
import csv
import pandas as pd

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ise')
def ise():
    data=pd.read_csv('ise.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('ise.html',results=result)

@app.route('/cse')
def cse():
    data=pd.read_csv('cse.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('cse.html',results=result)

@app.route('/chem')
def chem():
    data=pd.read_csv('chem.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('chem.html',results=result)

@app.route('/auto')
def auto():
    data=pd.read_csv('auto.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('auto.html',results=result)

@app.route('/bt')
def bt():
    data=pd.read_csv('bt.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('bt.html',results=result)

@app.route('/ece')
def ece():
    data=pd.read_csv('ece.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('bt.html',results=result)

@app.route('/civil')
def civil():
    data=pd.read_csv('civil.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('civil.html',results=result)

@app.route('/ctm')
def ctm():
    data=pd.read_csv('ctm.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('ctm.html',results=result)

@app.route('/eee')
def eee():
    data=pd.read_csv('eee.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('eee.html',results=result)

@app.route('/maths')
def maths():
    data=pd.read_csv('maths.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('math.html',results=result)

@app.route('/mech')
def mech():
    data=pd.read_csv('mech.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('mech.html',results=result)

@app.route('/physics')
def physics():
    data=pd.read_csv('physics.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('physics.html',results=result)

@app.route('/soft')
def soft():
    data=pd.read_csv('soft.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('soft.html',results=result)

@app.route('/sports')
def sports():
    data=pd.read_csv('sports.csv')
    records=data.to_records(index=False)
    result = list(records)
    return render_template('sports.html',results=result)

if __name__ == "__main__":
    app.run(debug=True)