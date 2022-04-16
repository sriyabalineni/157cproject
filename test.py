import pymongo
from pymongo import MongoClient
mongoCLient = MongoClient("54.156.111.243:27017")
db = mongoCLient["myDB"]
collection = db["business"]
# Read
print(collection.find_one({"business_id": "jaxMSoInw8Poo3XeMJt8lQ"}))
# Insert
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
print("Before Update")
print(collection.find_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA"},
                          {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1}))
print(collection.update_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA"},
                            {"$set": {"address": "1234 Oak St"}}))
print("After Update")
print(collection.find_one({"business_id": "eEOYSgkmpB90uNA7lDOMRA"},
                          {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1}))
# Delete
print(collection.find_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))
print(collection.delete_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))
print(collection.find_one({"business_id": "mpfCx-BjTdTEA12CZrA5Pw"}))