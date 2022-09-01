from flask import Flask, render_template

app = Flask(__name__)

# landing page
@app.route('/')
def hello():
    return '''<html>
    <style>
        h1 {text-align: center; font-family: Arial}
    </style>

    <h1>
        Hello, World!
    </h1>
    </html>
    '''

@app.route('/login')
def login():
    return '''<html>
    <style>
        h1 {text-align: center; font-family: Arial}
        button {font-family; Arial; font-size: 20px; padding: 7px; border-radius: 7px}
        #container {text-align: center}
    </style>

    <h1>
        This is the Login Page
    </h1>

    <div id='container'>
        <button type='button' onclick='alert("This feature is not available at the moment")'>
            Login
        </button>
    </div>
    </html>
    '''

@app.route('/milkis')
def milkis():
    return '''<html>
    <style>
        h1 {text-align: center; font-family: Arial}
        #container {text-align: center}
    </style>

    <h1>
        This is a picture of Milkis
    </h1>

    <div id='container'>
        <img src='https://cdn.shopify.com/s/files/1/0338/0694/2253/products/LotteMilkisDrinkCanOriginalFlavor8.45oz_front_900x.jpg?v=1650574585'>
    </div>
    </html>
    '''

# this is to test if the script can run on localhost
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)