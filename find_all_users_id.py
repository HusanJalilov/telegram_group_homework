import json
from unittest import result
from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    s=[]
    d=[]
    col=data["messages"]
    for x in range(len(col)):
        div=col[x]
        
        if 'actor_id' in div:
            key=div['actor_id']
            s.append(key)
    
    return s
    
f=open('data/result.json',encoding='utf8').read()
data=json.loads(f)
print(find_all_users_id(data))
