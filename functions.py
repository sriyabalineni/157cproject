
def fetch_high_rated_business(db ):
    collection = db.yelpc
    stars='stars'
    gte='$gte'
    id="_id"
    name="name"
    query= {stars:{gte:4}}
    projection={name:1,id:0}
    cursor = collection.find(query, projection)
    for record in cursor:
	    print(record)



menu_option={1: 'View high rated businesses', 2: 'Find Nearby Businesses',3: 'Find Businesses by Category.', 4: 'Find High Rated Businesses', 5:'Find Popular Businesses'}
def print_menu(menu_option):
    for key, value in menu_option.items():
        print(key,".", value)
print_menu(menu_option)
option = int(input('Enter your choice: '))
print(option)
from pymongo import MongoClient

try:
	conn = MongoClient()
	print("Connected successfully!!!")
except:
	print("Could not connect to MongoDB")
db = conn.yelpdb
if option==4:
    fetch_high_rated_business(db)
    






