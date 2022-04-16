# function 3
def find_businesses_by_category(collection):
    category = input("Please enter a category!\nFor example: Fast Food, Sushi, Italian, etc: ")
    output = collection.find({"categories": {"$regex": category}},
                             {"name": 1, "address": 1, "city": 1, "state": 1, "postal_code": 1,
                              "stars": 1, "review_count": 1}).limit(5)
    for doc in output:
        print(doc)

#function 4
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

#function 5
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
                                                                                                                 99,10         Bot
