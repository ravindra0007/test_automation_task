import json
import os
curr_dir = os.getcwd()
def json_modify(file):
    with open(file, 'r') as data_file:
        data = json.load(data_file)
        del data['inParams']['appdate']
        del data['outParams']
    with open('updated_jsonfile.json', 'w') as data_file:
        data = json.dump(data, data_file)
obj = json_modify(curr_dir+"\\test_payload.json")