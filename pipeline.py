import json
from bson import json_util
from bson.json_util import dumps
from pymongo import MongoClient
connection = MongoClient('localhost', 27017)
database = connection['market']
collection = database['stocks']

def pipeline(pipe):
  try:
    result=collection.aggregate(pipe)
    result = dumps(result)
    print(result)
  except ValidationError as ve:
    abort(400, str(ve))
  

def main():
  sectorname = raw_input("Name Of The Sector: ")
  firstStage = { '$match': { "Sector": sectorname } }
  secondStage= { '$group': { '_id': "$Industry", 'Total Austanding Shares:': {'$sum': "$Shares Outstanding" } } }
  pipe = [firstStage,secondStage]
  pipeline(pipe)
main()