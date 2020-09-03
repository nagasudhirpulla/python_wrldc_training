'''
Session 36 - Flask API end points
Date - 03-Sep-2020
'''

from flask import Flask, render_template, request

app = Flask(__name__)
# this secret will be used for http session management
# use a strong secret from config file or environmnt variable instead
app.secret_key = 'someSecret'

# send simple text, when '/hello' is called
@app.route('/hello')
def hello():
    return 'Hello World!!!'

# send json
@app.route('/hello_json')
def helloJson():
    return {'message': 'Hello World!!!'}

# render 'home.html'
@app.route('/')
def home():
    return render_template('home.html')

# extract data from URL segments
@app.route('/sum/<int:x>/<int:y>')
def sumWithFragements(x: int, y: int):
    numSum = x + y
    return render_template('sum_result.html', data={'x': x, 'y': y, 'sumVal': numSum})

# extract data from query parameters, example abc.com?x=2&y=5
@app.route('/sum')
def sumWithQueryParams():
    x = request.args.get('x', 0, type=int)
    y = request.args.get('y', None, type=int)
    sumVal = x + y
    return render_template('sum_result.html', data={'x': x, 'y': y, 'sumVal': sumVal})

# extract data from post request body
@app.route('/sum', methods=['POST'])
def sumWithPostBody():
    reqJson = request.get_json()
    x = reqJson['x']
    y = reqJson['y']
    sumVal = x + y
    # return render_template('sum_result.html', data={'x': x, 'y': y, 'sumVal': sumVal})
    return {"message": f"sum of {x} and {y} is {sumVal}"}


# handle url segments, post request body, query parameters in one function itself,
# by using multiple decorators on a single function
# @app.route('/sum', methods=['POST', 'GET'])
# @app.route('/sum/<xIn>/<yIn>')
# def sumAllTypesHandler(xIn=None, yIn=None):
#     if request.method == 'POST':
#         reqJson = request.get_json()
#         x = reqJson['x']
#         y = reqJson['y']
#     else:
#         if xIn == None:
#             x = request.args.get('x', 0, type=int)
#             y = request.args.get('y', 0, type=int)
#         else:
#             x = xIn
#             y = yIn
#     sumVal = int(x) + int(y)

#     return render_template('sum_result.html', data={'x': x, 'y': y, 'sumVal': sumVal})
#     # return {"message": f"sum of {x} and {y} is {sumVal}"}


# start the server at specific port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50100, debug=True)
