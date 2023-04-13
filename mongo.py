import pymongo

connection = pymongo.MongoClient("i6.cims.nyu.edu", 27017, username="ek3395", password="NTW6qKn2", authSource="ek3395")
db = connection["ek3395"]
collection = db["listings"]

docs = collection.find({}).limit(10)

for doc in docs:
    print(doc)

query = {"beds": {"$gt": 2}, "neighbourhood": "Centrum-Oost"}
projection = {"name": 1, "beds": 1, "review_scores_rating": 1, "price": 1}
results = collection.find(query, projection).sort("review_scores_rating", pymongo.DESCENDING)
for result in results:
    print("Name:", result["name"])
    print("Beds:", result["beds"])
    print("Price:", result["price"])
    print("Review Scores Rating:", result["review_scores_rating"])
    print()

