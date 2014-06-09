from flask import Flask, Response
from flask import request
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient.constants import RAW
import json

#declare application
app = Flask(__name__)
app.debug = True

##################################
## web helper functions
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
## db helper functions
##################################
def UpsertUser(userid):
    db = GraphDatabase("http://localhost:7474/db/data/")
    user_query = "START ee=node(*) WHERE ee.userid! = \"" + userid + "\" RETURN ee;"

    result = db.query(q=user_query, returns=(client.Node, unicode, client.Relationship))
    if len(result) == 0:
        user = db.nodes.create(userid=userid)
    else:
        for node in result:
            user = node.pop()

    return user

def UpsertItem(itemid):
    db = GraphDatabase("http://localhost:7474/db/data/")
    item_query = "START ee=node(*) WHERE ee.itemid! = \"" + itemid + "\" RETURN ee;"

    result = db.query(q=item_query, returns=(client.Node, unicode, client.Relationship))
    if len(result) == 0:
        item = db.nodes.create(itemid=itemid)
    else:
        for node in result:
            item = node.pop()

    return item

def UpsertRating(user, item, rating):
    db = GraphDatabase("http://localhost:7474/db/data/")

    rating_query = "START a = node(" + str(user.id) + ") MATCH a-[r]-b WHERE b.itemid=\""
    rating_query += str(item.properties["itemid"]) + "\" RETURN r;"

    params = {}
    result = db.query(rating_query, params=params, returns=(client.Node, unicode, client.Relationship))
    if len(result) == 0:
        user.relationships.create("Rated", item, rating=rating)
    else:
        for rel in result:
            r = rel.pop()
            print r
            print r.get("rating")


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
#http://127.0.0.1:5000/rating/572/7/5
def rating (userid, itemid, rating):
    db = GraphDatabase("http://localhost:7474/db/data/")

    user = UpsertUser(userid)
    item = UpsertItem(itemid)
    UpsertRating(user, item, rating)

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