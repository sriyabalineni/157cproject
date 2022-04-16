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

    db = mongoClient.yelpdb
    collection = db.yelpc

    while (True):
        print_menu(menu_option)
        option = int(input('Enter your choice: '))

        if option == 6:
            mongoClient.close()
            break
        elif option==1:
            find_business_by_name(collection)
            break
        elif option==2:
            break
        elif option==3:
            find_businesses_by_category(collection)
            break
        elif option==4:
            fetch_high_rated_business(collection)
            break
        elif option==5:
            fetch_popular_business(collection)
            break


# function 1
def find_business_by_name(collection):
    name = input("Please Enter Business Name: ")
    output = collection.find({"name": {"$regex": name}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)


# function 2 PETER
def find_nearby_businesses(collection):
    zipcode = input("Please Enter Your Zipcode: ")
    output = collection.find({"postal_code": zipcode}, {"name": 1, "address": 1, "stars": 1})
    for doc in output:
        print(doc)


# function 3
def find_businesses_by_category(collection):
    category = input("Please enter a category!\nFor example: Fast Food, Sushi, Italian, etc: ")
    output = collection.find({"categories": {"$regex": category}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)


# function 4
def fetch_high_rated_business(collection):
    stars = 'stars'
    gte = '$gte'
    id = "_id"
    name = "name"
    query = {stars: {gte: 4}}
    projection = {name: 1, id: 0}
    cursor = collection.find(query, projection).limit(5)
    for record in cursor:
        print(record)


# function 5
def fetch_popular_business(collection):
    is_open = "is_open"
    id = "_id"
    name = "name"
    review_count = "review_count"
    #db.yelpc.find( {is_open:1},{"name":1,"_id":0,  "review_count":1}).sort({review_count:-1})
    query={is_open:1}
    projection={name:1,id:0, review_count:1}
    sort_query= {review_count:-1}

    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)

    for record in cursor:
            print(record)


if __name__=="__main__":
    main()
    
