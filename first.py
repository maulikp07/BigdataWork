from pymongo import MongoClient
import re

regx = re.compile("hillary", re.IGNORECASE)
conn = MongoClient("mongodb://localhost:27017")
db = conn.trump
tweets = db.tweets.find({'text': {'$regex': regx}}, {"_id": "1", "text": "0",
                                                     "source": "1"})  # db.collectionname.find({'files':{'$regex':'^File'}})
count = 0
for e in tweets:
    count += 1
    print(e['text'])

print("There are ", count, " tweets about Hillary.")


def fib(n):
    a, b = 0, 1
    """Print a Fibonacci Series Upto n"""
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


fib(100)
