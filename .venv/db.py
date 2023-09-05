import json  
import os 




# # Get the current script's directory
# script_directory = os.path.dirname(os.path.realpath(__file__))

# # Set the working directory to the script's directory
# os.chdir(script_directory)



actions_list='''
    
      { 
        "actions":[

        {
            "id":1,
            "action":"addition"
        },
        {
            "id":2,
            "action":"multiplication"
        }
    

      ]}  
'''

# data=open('.venv\db1.json')
# json_data=json.loads(data)
# with open('.venv\db1.json', 'r') as file:
#     print(file)
#     json_data=json.load(file)



# def read_json_file(file_name):
#     with open(file_name, 'r') as file:
#         data = json.load(file)
#     return data

# # Usage example
# json_data = read_json_file('data.json')


file_name = 'data.json'

try:
    with open(file_name, 'r') as file:
        myNewData = json.load(file)
       
        
        
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except json.JSONDecodeError:
    print(f"Error decoding JSON data in '{file_name}'.")



def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

# Usage example
json_data = read_json_file(os.getcwd()+'\\.venv\\data.json')    