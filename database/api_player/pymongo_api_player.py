# coding = utf-8


from pymongo import MongoClient

addr = 'localhost'
port = 27017

client = MongoClient(addr, port)

name_list = client.database_names()

print name_list

db = client['weshare']  # use weshare

cursor = db['gt_host'].find_one()

print cursor.keys()