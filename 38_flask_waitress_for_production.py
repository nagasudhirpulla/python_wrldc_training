'''
using waitress module to serve flask web server
pip install waitress
https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/#run-with-a-production-server
'''

from flask import Flask, render_template
from waitress import serve
app = Flask(__name__)

# just return 'Hello World!' text when the route '/' is called
@app.route('/')
def index():
    return 'Hello, World!'


# __name__ will be __main__ only if this file is the entry point
if __name__ == '__main__':
    # run the server on this ip and port 50100
    serve(app, host='0.0.0.0', port=50100, threads=1)
