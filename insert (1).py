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
collection_comp = db['company']


def insert_document(document): // Defines function to add document to database
  message = ""
  try:
    result=collection.insert(document)
    message = "Document Added Successfully" // Confirms addition
  except ValidationError as ve:
    abort(400, str(ve))
    message = "Document Could Not Be Added.."
  return message


def main():
  
  myDocument = { "Ticker" : "0210", "Volume":"030617"}
  print insert_document(myDocument) // Prints result
main()
