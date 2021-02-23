import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def find_document(query): // Defines function to search for document
  try:
    result=collection.find(query).count()
    print("There Are "+str(result)+" Documents")
  except ValidationError as ve:
    abort(400, str(ve))
  

def main(): 
  high = float(raw_input("Enter Highest Values# ")) // Prompts user to input data
  low = float(raw_input("Enter Lowest Value# ")) // Prompts user for second value
  my_document = { "50-Day Simple Moving Average" : {"$gt":high,"$lt":low}}
  find_document(my_document)
main()