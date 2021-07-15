import pandas as pd
import json


def read_csv_demo():
    school_data_to_load = "resources\schools_complete.csv"
    school_data_df = pd.read_csv(school_data_to_load)
    return school_data_df;

def read_json_demo():    
    with open('resources\simples.json') as json_file:
        dictionary_from_json_file = json.load(json_file)
    
        # Print the type of data variable
        print("Type:", type(dictionary_from_json_file))  

    return dictionary_from_json_file