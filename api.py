from flask import Flask, Response
from flask import request
import json

#declare application
app = Flask(__name__)
app.debug = True

##################################
## helper functions
##################################
def WrapCallbackString(result_data):
    callback_string = request.args.get('callback')
    if callback_string:
        results = callback_string
        results += "(" + json.dumps(result_data, indent=4) + ")"
    else:
        results = json.dumps(result_data, indent=4)

    return results


##################################
## ROUTES
##################################
#index
@app.route('/')
def index():
    return 'graph Recommender v0.1'

##################################
#add rating
@app.route('/rating/<string:userid>/<string:itemid>/<int:rating>')
#http://127.0.0.1:5000/recommenderitems/572/7/5
def rating (userid, itemid, rating):
    results = WrapCallbackString("OK")

    resp = Response(response=results,
                    status=200,
                    mimetype="application/json")

    return resp

##################################
#recommendation getters
@app.route('/recommenderitems/<string:userid>/<string:itemid>/<int:numitems>/<string:mode>')
@app.route('/recommenderitems/<string:userid>/<string:itemid>/<int:numitems>',defaults={'mode': 'simple'})
#http://127.0.0.1:5000/recommenderitems/572/7/50/detail or http://127.0.0.1:5000/recommenderitems/572/7/50

def recommenderitems (userid, itemid, numitems, mode):

    results = WrapCallbackString("hello world")

    resp = Response(response=results,
                    status=200,
                    mimetype="application/json")

    return resp

##################################
## App bootstrap
##################################
if __name__ == '__main__':
    app.run()