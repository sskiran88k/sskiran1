import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:<password>@cluster0.8aq5nqi.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
database = client['ineuron']

coll = database['fsds_8th']

data = {"class name " : "full stack data science 2.0 " ,
        "topic name " : "mongo db nosql ",
        "todays date ": "8th jan 2023"
}

coll.insert_one(data)
