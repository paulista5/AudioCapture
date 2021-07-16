from pymongo import MongoClient

username = "root"
password = "pass12345"

conn = MongoClient('mongodb://%s:%s@127.0.0.1:27017' % (username, password))