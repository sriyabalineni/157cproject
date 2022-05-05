import pymongo
from pymongo import MongoClient

menu_option = {1: 'Find Business by Name', 2: 'Find Nearby Businesses', 3: 'Find Businesses by Category.',
               4: 'Find High Rated Businesses', 5: 'Find Popular Businesses', 6: 'Find popular businesses that allow pets',
               7: 'Find popular restaurants that do not require reservations', 8: 'Find populat businesses that are wheel chair accessible',
               9: 'Find popular restaurants that are good for kids', 10: 'Find popular restaurants that have outdoor seating',
               11: 'Find popular businesses that are good for groups', 12: 'Find users join from a specific date',
               13: 'Find user by name', 14: 'Find elite users in a specific year',
               15: 'Find influenced user', 16: 'Exit'}


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

    db = mongoClient["projectDatabase"]
    businessCollection = db["business"]
    userCollection = db["user"]

    while (True):
        print_menu(menu_option)
        option = int(input('Please enter your choice: '))

        if option == 16:
            mongoClient.close()
            break
        elif option == 1:
            find_business_by_name(businessCollection)
        elif option == 2:
            find_nearby_businesses(businessCollection)
        elif option == 3:
            find_businesses_by_category(businessCollection)
        elif option == 4:
            fetch_high_rated_business(businessCollection)
        elif option == 5:
            fetch_popular_business(businessCollection)
        elif option == 6:
            fetch_business_alloiwing_pets(businessCollection)
        elif option == 7:
            fetch_restaurants_without_reservations(businessCollection)
        elif option == 8:
            fetch_wheelchair_accesible_businesses(businessCollection)
        elif option == 9:
            fetch_goodforkids_restaurants(businessCollection)
        elif option == 10:
            fetch_outdoor_seating_restaurants(businessCollection)
        elif option == 11:
            fetch_good_for_groups(businessCollection)
        elif option == 12:
            fetch_user_on_date(userCollection)
        elif option == 13:
            fetch_user_by_name(userCollection)
        elif option == 14:
            fetch_elite_user(userCollection)
        elif option == 15:
            fetch_influenced_user(userCollection)

# function 1
def find_business_by_name(collection):
    name = input("Please Enter Business Name: ")
    output = collection.find({"name": {"$regex": name}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)


# function 2
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
    projection = {name: 1, id: 0, stars: 1}
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
        
# function 6 find businesses that allow pets
def fetch_business_alloiwing_pets(collection):
    pets_allowed = "attributes.DogsAllowed"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    query={pets_allowed:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)

# function 7 Find restaurants that do not require reservations

def fetch_restaurants_without_reservations(collection):
    reservations = "attributes.RestaurantsReservations"
    id = "_id"
    name = "name"
    review_count = "review_count"
    false= "False"
    city="city"
    postal_code="postal_code"
    #db.yelpc.find({'attributes.RestaurantsReservations':'False'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={reservations:false}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)

# function 8 Find businesses that are wheelchair accessible

def fetch_wheelchair_accesible_businesses(collection):
    wheelcahir_access = "attributes.WheelchairAccessible"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    #db.yelpc.find({'attributes.WheelchairAccessible':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={wheelcahir_access:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)

# function 9 Find restaurants that are good for kids          
def fetch_goodforkids_restaurants(collection):
    goodforkids = "attributes.GoodForKids"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    #db.yelpc.find({'attributes.WheelchairAccessible':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={goodforkids:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)

# function 10 Find restaurants that have outdoor seating
def fetch_outdoor_seating_restaurants(collection):
    OutdoorSeating = "attributes.OutdoorSeating"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    #db.yelpc.find({'attributes.OutdoorSeating':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={OutdoorSeating:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)

# function 11 Find businesses that are good for groups 

def fetch_good_for_groups(collection):
    goodforgroups = "attributes.RestaurantsGoodForGroups"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    #db.yelpc.find({'attributes.goodforgroups':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={goodforgroups:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
        print(record)


# function 12 Find users join on a specific date
def fetch_user_on_date(collection):
    date = input("Please enter a date in format YYYY-MM-DD: ")
    output = collection.find({"yelping_since": {"$regex": date}},
                             {"_id": 0, "friends": 0}).limit(5)
    for doc in output:
        print(doc)


# function 13 Find user by user name
def fetch_user_by_name(collection):
    name = input("Please Enter User Name: ")
    output = collection.find({"name": {"$regex": name}},
                             {"_id": 0, "friends": 0}).limit(5)
    for doc in output:
        print(doc)


# function 14  Find elite user
def fetch_elite_user(collection):
    year = input("Please enter a year: ")
    output = collection.find({"elite": year},
                             {"_id": 0, "friends": 0}).limit(5)
    for doc in output:
        print(doc)


# function 15   Find influenced user
def fetch_influenced_user(collection):
    output = collection.find({}, {"_id": 0, "friends": 0}).sort({"review_count": -1}).limit(5)
    for doc in output:
        print(doc)


if __name__=="__main__":
    main()
    
