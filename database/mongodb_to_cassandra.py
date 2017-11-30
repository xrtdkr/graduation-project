# coding=utf-8

from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel

from pymongo import MongoClient

from conf import *
from DDL import *


class Mon(object):
    '''
    mongodb dbs->collections->keys
    '''
    def __init__(self):
        self.addr = MONGO_ADDR
        self.port = MONGO_PORT
        self.client = MongoClient(MONGO_ADDR, MONGO_PORT)
        self.dbnames = self.client.database_names()

    def get_collection_name(self, dbname):
        '''
        :param dbname: mongodb中数据库的名字 
        :return: 数据库中包含的所有表名(collections)
        '''
        database = self.client[dbname]
        collection_names = database.collection_names()
        return collection_names

    def get_keynames(self, dbname, collection_name):
        '''
        :param dbname: mongodb 的数据库名字
        :param collection_name: mongodb 的表名
        :return: 对应的keys 名字的list
        '''

        database = self.client[dbname]
        collection = database[collection_name]
        cursor = collection.find_one()

        return cursor.keys()


class Cass(object):
    '''
    mongodb: dbs->collections->keys
    cassandra: keyspace->table->rows
    '''
    def __init__(self):
        self.addr = CASS_ADDR
        self.port = CASS_PORT
        self.cluster = Cluster()  # default

    def create_keyspace(self, mdb_name):
        '''
        :param mdb_name: 
        :return: 成功创建返回true，失败返回false
        '''
        pass





mon = Mon()

for dbname in mon.dbnames:
    print mon.get_collection_name(dbname)
