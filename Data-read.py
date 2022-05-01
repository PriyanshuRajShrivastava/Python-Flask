from ctypes import sizeof
import os,json

path_to_json = 'data/'

for file_name in [file for file in os.listdir(path_to_json) if file.endswith('.json')]:
  with open(path_to_json + file_name) as json_file:
    data = json.load(json_file)
 
  print(file_name)