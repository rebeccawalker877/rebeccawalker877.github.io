import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def update_document(query,update): // Defines function to change documents
  try: 
    collection.update_many(query,update)
    result=collection.find(query,{"Current Ratio":1,"Ticker":1,"Total Debt/Equity":1,"Volume":1})
    print("\t\t RESULTS ");
    print(dumps(result)) // prints result
  except ValidationError as ve:
    abort(400, str(ve))
  

def main():
  print("\t\t Provide The Ticker Value for The Documents To Be Updated \n");
  tvalue = raw_input("Enter Ticker Value# ") // Prompt user to input value
  print("Received >>"+tvalue);
  query = {"Ticker" : tvalue}
  result=collection.find(query,{"Current Ratio":1,"Ticker":1,"Total Debt/Equity":1,"Volume":1})
  print(dumps(result)) // Prints updated value
  
  volume = float(raw_input("New Volume#"))
    
  update =  { "$set":{"Volume":volume}}
  update_document(query,update)
  
main()