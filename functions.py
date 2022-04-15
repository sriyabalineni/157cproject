import pymongo
from pymongo import MongoClient

menu_option = {1: 'Find Business by Name', 2: 'Find Nearby Businesses', 3: 'Find Businesses by Category.',
               4: 'Find High Rated Businesses', 5: 'Find Popular Businesses', 6: 'Exit'}


def print_menu(menu_option):
    for key, value in menu_option.items():
        print(key, ".", value)


def main():
    mongoClient = None
    try:
        mongoClient = MongoClient("localhost:27020")
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")

    db = mongoClient.get_database("projectDatabase")
    collection = db.get_collection("business")

    while (True):
        print_menu(menu_option)
        option = int(input('Enter your choice: '))

        if option == 6:
            mongoClient.close()
            return
        else:
            match option:
                case 1:
                    find_business_by_name(collection)
                    break
                case 2:
                    break
                case 3:
                    find_businesses_by_category(collection)
                    break
                case 4:
                    fetch_high_rated_business(collection)
                    break
                case 5:
                    break



    if option == 4:
        fetch_high_rated_business(db)


# function 1
def find_business_by_name(collection):
    name = input("Please Enter Business Name: ")
    output = collection.find({"name": {"$regex": name}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)


# function 2 PETER

# function 3
def find_businesses_by_category(collection):
    category = input("Please enter a category!\nFor example: Fast Food, Sushi, Italian, etc: ")
    output = collection.find({"categories": {"$regex": category}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)


def fetch_high_rated_business(collection):
    stars = 'stars'
    gte = '$gte'
    id = "_id"
    name = "name"
    query = {stars: {gte: 4}}
    projection = {name: 1, id: 0}
    cursor = collection.find(query, projection)
    for record in cursor:
        print(record)
