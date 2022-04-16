import pymongo
from pymongo import MongoClient
mongoClient = MongoClient("localhost:27020")
db = mongoClient["projectDatabase"]
collection = db["business"]

# Read
def read_doc():
    print("Read file")
    print(collection.find_one({"business_id": "jaxMSoInw8Poo3XeMJt8lQ"}, {"_id": 0, "hour": 0}))

# Insert
def insert_doc():
    print("Insert file")
    testInsert = {"business_id": "mpfCx-BjTdTEA12CZrA5Pw",
                  "name": "My Fantasy",
                  "address": "28712 Main St",
                  "city": "San Jose",
                  "state": "CA",
                  "postal_code": "95111",
                  "stars": 4.5,
                  "review_count": 7
                  }
    print(collection.insert_one(testInsert))

# Update
def update_doc():
    print("Before Update")
    print(collection.find_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA"},
                              {"_id": 0, "name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1}))
    print(collection.update_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA", "postal_code": "33602"},
                                {"$set": {"address": "1234 Oak St"}}))
    print("After Update")
    print(collection.find_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA"},
                              {"_id": 0, "name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1}))

# Delete
def delete_doc():
    print("Delete file")
    print(collection.find_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))
    print(collection.delete_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))
    print(collection.find_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))


read_doc()
insert_doc()
update_doc()
delete_doc()