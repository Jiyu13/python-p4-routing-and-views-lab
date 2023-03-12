#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)


# 1. create index() view
@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'


# 2. create print_string() view that takes 1 string param 
@app.route('/print/<string:parameter>')
def print_string(parameter):
    # print string in console
    print(parameter)
    return parameter


# 3. create count() view, takes an int
@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(parameter):
        result += f'{i}\n'
    return result


# 4. create math() view, takes 3 params: num1, operation, num2
@app.route('/math/<int:num1><operation><int:num2>')
def math(num1, operation, num2):
    if operation == "+":
        return f"{num1 + num2}" 
    elif operation == "-":
        return f"{num1 - num2}" 
    elif operation == "*":
        return f"{num1 * num2}" 
    elif operation == "div":
        return f"{num1 / num2}"
    elif operation == "%":
        return f"{num1 % num2}" 
    
    return "please enter a correct operator: +, -, *, div, %"



if __name__ == "__main__":
    app.run(port=5555, debug=True)
