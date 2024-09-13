from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = 0
    number_2 = 0
    try:
        number_1 = int(request.form.get("first"))
        number_2 = int(request.form.get('second'))
    except:
        pass
    operation = request.form.get('operation')
    result = 0
    if operation == 'add':
        result = requests.get(url = f'http://add-service:5051/{number_1}/{number_2}').text
    elif operation == 'minus':
        result = requests.get(url = f'http://minus-service:5052/{number_1}/{number_2}').text
    elif operation == 'multiply':
        result = requests.get(url = f'http://multiply-service:5053/{number_1}/{number_2}').text
    elif operation == 'divide':
        result = requests.get(url = f'http://divide-service:5054/{number_1}/{number_2}').text
    elif operation == 'gcd':
        result = requests.get(url = f'http://gcd-service:5055/{number_1}/{number_2}').text
    elif operation == 'lcm':
        result = requests.get(url = f'http://lcm-service:5056/{number_1}/{number_2}').text
    elif operation == 'modulus':
        result = requests.get(url = f'http://modulus-service:5057/{number_1}/{number_2}').text
    elif operation == 'exponent':
        result = requests.get(url = f'http://exponent-service:5058/{number_1}/{number_2}').text
    elif operation == 'greater_than':
        result = requests.get(url = f'http://greater-than-service:5059/{number_1}/{number_2}').text
    elif operation == 'lesser_than':
        result = requests.get(url = f'http://lesser-than-service:5060/{number_1}/{number_2}').text
    elif operation == 'equal':
        result = requests.get(url = f'http://equal-service:5061/{number_1}/{number_2}').text
    flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050, host="0.0.0.0")