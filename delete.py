import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def deleteDocument(document,tvalue):// Delete Function
  try:
    result = collection.remove(document)
    print("Documents With Ticker Value "+tvalue+" Have Been Deleted  \n")
    print(dumps(result))
  except ValidationError as ve:
    abort(400, str(ve))
  

def main():
  print("\t\t Provide The Ticker Value for The Documents To Be DELETED \n"); //Prompt user to input data
  tvalue = raw_input("Enter Ticker Value #")// Value entered by user
  myquery = {"Ticker" : tvalue}
  result=collection.find(myquery)
  print(dumps(result)) // prints results
  deleteDocument(myquery,tvalue) // Delete document
main()