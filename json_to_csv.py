import json
import os
import pandas as pd
from flatten_json import flatten
from collections.abc import MutableMapping
import csv

path_to_json="data/"

my_dict = {
"innings"
}

new_data = []


def read_file_individually(file):    
    obj = json.load(file)
    only_info = without_keys(obj,my_dict)
    flattened = flatten_dict(only_info)
    return flattened
            
def _flatten_dict_gen(d, parent_key, sep):
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, MutableMapping):
                yield from flatten_dict(v, new_key, sep=sep).items()
            else:
                yield new_key, v


def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.'):
    return dict(_flatten_dict_gen(d, parent_key, sep))

       
def without_keys(d, keys):
        return {k:v for k,v in d.items() if k not in keys}



#with open('mycsvfile.csv', 'w') as f:  
#    w = csv.DictWriter(f, FD.keys())
 #   w.writeheader()
 #   w.writerow(FD)

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
      with open(path_to_json + file_name) as json_file:
            #data = json_file.read()
            M = read_file_individually(json_file)
            new_data.append(M)
            

print(new_data)