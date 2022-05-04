import pymongo
from pymongo import MongoClient

menu_option = {1: 'Find Business by Name', 2: 'Find Nearby Businesses', 3: 'Find Businesses by Category.',
               4: 'Find High Rated Businesses', 5: 'Find Popular Businesses',7:'Find popular restaurats that do not require reservations', 8:'Find populat businesses that are wheel chair accessible',9:'Find popular restaurants that are good for kids',10:'Find popular restaurants that have outdoor seating',11:'Find popular businesses that are good for groups',12:'Find popular restaurants that offer takeout',13:'Find popular businesses that have free wifi',14:'Find popular restaurants that offer delivery',15:'Find popular businesses that accept credit card' ,16: 'Exit'}


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
    collection = db["business"]
    while (True):
        print_menu(menu_option)
        option = int(input('Enter your choice: '))

        if option == 16:
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
        elif option==7:
            fetch_restaurants_without_reservations(collection)
            break
        elif option==8:
            fetch_wheelchair_accesible_businesses(collection)
            break
        elif option==9:
            fetch_goodforkids_restaurants(collection)
            break
        elif option==10:
            fetch_outdoor_seating_restaurants(collection)
            break
        elif option==11:
            fetch_good_for_groups(collection)
            break
        elif option==12:
            fetch_takeout_restaurants(collection)
            break
        elif option==13:
            fetch_free_wifi_business(collection)
            break
        elif option==14:
            fetch_delivery_restaurants(collection)
            break
        elif option==15:
            fetch_creditcard_business(collection)
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
    projection = {name: 1, id: 0,stars:1}
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

# function 12 Find restaurants that offer takeout

def fetch_takeout_restaurants(collection):
    takeout = "attributes.RestaurantsTakeOut"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    query={takeout:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)

# function 13 Find businesses that have free wifi 

def fetch_free_wifi_business(collection):
    wifi = "attributes.WiFi"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    free="free"
    #db.yelpc.find({'attributes.OutdoorSeating':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={wifi:{"$regex": free}}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)

# function 14  Find restaurants that offer delivery
def fetch_delivery_restaurants(collection):
    delivery = "attributes.RestaurantsDelivery"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    free="free"
    #db.yelpc.find({'attributes.OutdoorSeating':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={delivery:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)

# function 15   Find businesses that accept credit card
def fetch_creditcard_business(collection):
    creditcard = "attributes.BusinessAcceptsCreditCards"
    id = "_id"
    name = "name"
    review_count = "review_count"
    true= "True"
    city="city"
    postal_code="postal_code"
    free="free"
    #db.yelpc.find({'attributes.OutdoorSeating':'True'}, {_id:0,name: 1, city: 1, postal_code: 1}).limit(5)
    query={creditcard:true}
    projection={name:1,id:0, city:1, postal_code:1}
    cursor = collection.find(query, projection).sort(review_count, -1).limit(5)
    for record in cursor:
            print(record)
if __name__=="__main__":
    main()
    
