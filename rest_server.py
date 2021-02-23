#!/usr/bin/python
import json
from bson import json_util
from bson.json_util import dumps
import bottle
from bottle import route, run, request, abort
#imports for database
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


@route('/createStock/<ticker>', method='POST')
def createStock(ticker): // Create document
  data = request.json
  data.update( {'Ticker' : ticker} ) 
  print(data)
  for item in data:
    print(data[item])
  record_created = collection.insert(data) 
  added_doc = collection.find_one({"_id":record_created})
  return  " \n Created Document "+dumps(added_doc)+"\n\n "


@route('/getStock/<Ticker>', method='GET')
def getStock(Ticker):
  found_doc = collection.find({"Ticker":Ticker}) // return result
  return dumps(found_doc) // returns document


@route('/updateStock/<TickerValue>', method='PUT')
def UpdateStock(TickerValue):
  jsondata = request.json 
  query = { "Ticker" : TickerValue} 
  for key in jsondata:
    update =  { "$set":{key:jsondata[key]}} // Update document
    collection.update(query,update)
  updateDocs = collection.find({"Ticker":TickerValue})
  result = dumps(updateDocs) 
  return "\n   Updated Document  \n"+str(result)+" \n" // Confirms update

   
@route('/deleteStock/<TickerValue>', method='GET')
def deleteStock(TickerValue):
  query = {"Ticker" :TickerValue} 
  result = collection.delete_many(query) // Delete Document
  return "\n  Document Deleted \n" // Confirms deletion



 
if __name__ == '__main__':
  run(debug=True,reloader = True)
  #run(host='localhost', port=8080)
