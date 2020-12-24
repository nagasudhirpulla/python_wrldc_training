'''
using flask module to create a web server
using layouts to reusing html in mulitple pages
using partials to split html among multiple files
pip install flask
https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
'''

from flask import Flask, render_template
app = Flask(__name__)

# just return 'Hello World!' text when the route '/' is called
@app.route('/')
def index():
    return 'Hello, World!'

# just return hello.html.j2 when the route '/hello' is called
# flask looks for html files in templates folder
@app.route('/hello')
def hello():
    return render_template('hello.html.j2')


# just return hello.html and pass the nameStr from url
# when the route '/greet/<nameStr>' is called
@app.route('/greet/<nameStr>')
def greet(nameStr):
    return render_template('hello.html.j2', data={'name': nameStr})

# just return home.html.j2 when the route '/home' is called
# this page uses template inheritence to extend a base tempplate
# refer 'home.html.j2' file
@app.route('/home')
def home():
    return render_template('home.html.j2', user={'name': 'Nagasudhir'})

@app.route('/anonymous')
def anonymous():
    return render_template('home.html.j2')

# __name__ will be __main__ only if this file is the entry point
if __name__ == '__main__':
    # run the server on this ip and port 50100
    app.run(host='0.0.0.0', port=50100, debug=True)
