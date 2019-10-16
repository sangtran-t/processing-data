# -*- coding: utf-8 -*-
import json

from pymongo import MongoClient


class DataProcessing:
    def __init__(self):
        self.path = ''
        self.data = []

    # read data from mongodb
    @staticmethod
    def read_data():
        """read data from json file"""
        # with open(path, mode='r', encoding='utf8') as json_source:
        #     data = json.load(json_source)
        #     json_source.close()
        #     return data

        """read data from mongodb"""
        client = MongoClient(port=27017)
        db = client.data_mrc_project
        collection = db.SK_article
        data = collection.find()
        return data

    # process data
    @staticmethod
    def data_processing(data):
        json_object = {}
        for item in data:
            paragraphs = [' '.join(item['paragraphs'])]
            if paragraphs[0].__len__() <= 3500:
                json_object['link'] = item['link']
                json_object['title'] = item['title']
                json_object['paragraphs'] = paragraphs
                yield json_object
            # return json.dumps(json_object, ensure_ascii=False)

