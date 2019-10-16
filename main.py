# -*- coding: utf-8 -*-
import json
import os
import pprint
from processing import DataProcessing

# pathSource = './data/input/khoahoc_result.json'

# connect to mongodb to get data for processing
process = DataProcessing()
data_sources = process.read_data()
items = process.data_processing(data_sources)


# save a item to json file
def save_to_file(folder_path, file_name, item_data):
    try:
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        with open(folder_path + '/' + file_name + '.json', mode='w', encoding='utf8') as f:
            json.dump(item_data, f, ensure_ascii=False)
            f.close()
            return True
    except Exception as e:
        raise e


if __name__ == '__main__':
    iter_count = 0
    fol_path = './data/output/data'
    for item in items:
        path = fol_path + str(iter_count // 10)
        f_name = 'ID_' + str(iter_count)
        iter_count += 1
        if save_to_file(path, f_name, item):
            print('SAVED FILE ' + f_name + ' IN FOLDER ' + path + ' SUCCESS')
        else:
            print('SAVED FILE ' + f_name + ' IN FOLDER ' + path + ' FAILED')
