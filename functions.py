
def fetch_high_rated_business(db ):
    collection = db.yelpc
    stars='stars'
    gte='$gte'
    id="_id"
    name="name"
    query= {stars:{gte:4}}
    projection={name:1,id:0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
	    print(record)

def fetch_popular_business(db):
    collection = db.yelpc
    is_open="is_open"
    id="_id"
    name="name"
    review_count="review_count"
    #db.yelpc.find( {is_open:1},{"name":1,"_id":0,  "review_count":1}).sort({review_count:-1})
    query={is_open:1}
    projection={name:1,id:0, review_count:1}
    sort_query= {review_count:-1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)

menu_option={1: 'Find Business by Name', 2: 'Find Nearby Businesses',3: 'Find Businesses by Category.', 4: 'Find High Rated Businesses', 5:'Find Popular Businesses'}
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
    






