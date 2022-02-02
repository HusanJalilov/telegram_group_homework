from read_data import read_data
import json
def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    return len(data['messages'])

f=open('data/result.json',encoding='utf8').read()
data=json.loads(f)
print(find_number_of_messages(data))