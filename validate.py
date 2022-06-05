import json
import jsonschema
from jsonschema import validate

def get_data():
    with open("file.json", 'r') as f:
        #if it fails to find the file, please mention the entire path to where file.json is in your system
        data = json.load(f)
        return data

def get_schema():
    with open("schemafile.json", 'r') as f:
        #if it fails to find the schema file, please mention the entire path to where schemafile.json is in your system
        schema = json.load(f)
        return schema

def Validatejson():
    schema = get_schema()
    data = get_data()
    try:
        validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def Validate():
    isValid = Validatejson()
    if isValid:
        print("TRUE!")
        print("The given JSON data is valid")
    else:
        print("FALSE!")
        print("The given JSON data is invalid!")

Validate()
    