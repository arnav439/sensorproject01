from pymongo.mongo_client import MongoClient
import pandas as pd
import json

url = "mongodb+srv://pwskills:5wE1dlgeC5jYzjGU@cluster0.t6e5k4g.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# create a new client and connect to server 
client = MongoClient(url)

#create databse name  and collection name 
DATABASE_NAME ="pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\Users\hp\Downloads\sensorproject\notebooks\wafer_23012020_041211.csv")

df = df.drop("Unnamed: 0",axis=1)
json_record=list(json.loads(df.T.to_json()).values())
json_record=list(json.loads(df.T.to_json()).values())