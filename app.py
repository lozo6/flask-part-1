from flask import Flask, render_template

app = Flask(__name__)

# created a page from templates folder taught in class
@app.route('/')
def hello():
    return render_template('hello.html')

# this page will show a heading and a button that has an alert
@app.route('/login')
def login():
    return render_template('login.html')

# this page will show you a heading and a picture
@app.route('/milkis')
def milkis():
    return render_template('milkis.html')

# this is to test if the script can run on localhost
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)