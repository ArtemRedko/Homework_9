import os
import json
import csv
import pickle


def json_csv_pickle(directory):
    # JSON
    result_dict_json = {}
    for dir_path, dir_file, file_name in os.walk(directory):
        result_dict_json[f'DIRECTORY - {dir_path}'] = [f'FILE - {i} = {os.path.getsize(os.path.abspath(dir_path + "/" + i))} byte' for i in file_name]
    with open('json_file.json', 'w', encoding='utf-8') as json_file:
        json.dump(result_dict_json, json_file, indent=4, separators=(',', ':'))
    # CSV
    data = [["Dir", "Files"]]
    for k, v in result_dict_json.items():
        data.append([k, v])
    with open('csv_file.csv', 'w', encoding='utf-8') as csv_f:
        write_csv = csv.writer(csv_f, dialect='excel-tab', delimiter=',')
        write_csv.writerows(data)
    # PICKLE
    with open('pickle_file.bin', 'wb') as pickle_file:
        pickle.dump(result_dict_json, pickle_file)