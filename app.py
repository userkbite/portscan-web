from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/send_data', methods=['POST'])
def send_data():
    ip_form = request.form['ip']
    
    ip = portScan(ip_form)
    
    return render_template('index.html', ip=ip)

if __name__ == '__main__':
    app.run(debug=True)
