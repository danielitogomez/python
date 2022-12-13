#!/usr/bin/python3

#Varialbes
input_json_file = "input.json"
output_yaml_file = "output.yaml"

#Importing modules
import yaml
import json
import pathlib

#Function evaluation
def input_json_evaluate():
    file = pathlib.Path(input_json_file)
    if file.exists ():
        print (f'Converting to yaml format in {output_yaml_file} file...')
        #Call function converter
        json_yaml_conver()
    else:
        print(f'No {input_json_file} file to make the conversion to {output_yaml_file}')
        exit(1)

#Function convert json to yaml
def json_yaml_conver():
    with open(input_json_file, 'r') as json_file:
        configuration = json.load(json_file)
    with open(output_yaml_file, 'w') as yaml_file:
        yaml.dump(configuration, yaml_file)

#Calling function
input_json_evaluate()