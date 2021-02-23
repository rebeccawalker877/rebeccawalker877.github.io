import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def find_document(query,to_display):
  try:
    result=collection.find(query,to_display)
    print(dumps(result))
  except ValidationError as ve:
    abort(400, str(ve))
  

def main():
  industry_name = raw_input("Name Of The Industry# ")
  query = {"Industry" : industry_name}
  to_display = {"Ticker":1,"_id":0}
  find_document(query,to_display)
 
main()