from flask import Flask

app = Flask(__name__)

# landing page
@app.route('/')
def hello_world():
    return 'Hello, World!'

# this is to test if the script can run on localhost
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)