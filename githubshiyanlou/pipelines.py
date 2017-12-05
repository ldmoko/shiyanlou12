# -*- coding: utf-8 -*-
from sqlalchemy.orm import sessionmaker
from githubshiyanlou.models import Repository, engine
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class GithubshiyanlouPipeline(object):
#     def process_item(self, item, spider):
#         # self.session.add(Repository(name=item['name'], update_time=item['update_time']))

#         self.session.add(Repository(**item))
#         # print(item)
#         return item

#     def open_spider(self, spider):
#     	self.session = sessionmaker(bind=engine)()

#     def close_spider(self, spider):
#         self.session.commit()
#         self.session.close()


# use pymysql
# import pymysql
# class GithubshiyanlouPipeline(object):
#     def process_item(self, item, spider):
#         name = item['name']
#         update_time = item['update_time']
#         commits = item['commits']
#         branche = item['branche']
#         releases = item['releases']
#         try:
#             sql = 'insert into repositories (name, update_time, commits, branche, releases) values(%s, %s, %s, %s, %s)'
#             lis = (name, update_time, commits, branche, releases)
#             self.cur.execute(sql, lis)
#             print('insert database success')
#         except Exception as err:
#             print(err)
#             print('insert database error')
#             self.conn.rollback()
        
#         # print(item)
#         return item

#     def open_spider(self, spider):
#         self.conn = pymysql.connect('localhost', 'root', '', 'shiyanlougithub', charset='utf8mb4')
#         self.cur = self.conn.cursor()

#     def close_spider(self, spider):
#         self.conn.commit()
#         self.cur.close()
#         self.conn.close()

# use pymongo
# from pymongo import *
# class GithubshiyanlouPipeline(object):
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
#         # print(item)
#         return item

#     def open_spider(self, spider):
#         self.client = MongoClient('localhost', 27017)
#         self.db = self.client['shiyanlou']
#         self.collection = self.db['data']

#     def close_spider(self, spider):
#         pass

# use MongoEngine
from mongoengine import *
connect('shiyanlou', host='localhost')
class GithubshiyanlouPipeline(object):
    def process_item(self, item, spider):
        
        self.data = Data(name=item['name'], 
            update_time=item['update_time'], 
            commits=str(item['commits']), 
            branche=str(item['branche']), 
            releases=str(item['releases'])
            )
        self.data.save()
        # print(item)
        return item
        

class Data(Document):
    name = StringField()
    update_time = StringField()
    commits = StringField()
    branche = StringField()
    releases = StringField()
