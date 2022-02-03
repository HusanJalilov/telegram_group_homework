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
    itm=[]
    col=data["messages"]
    for x in range(len(col)):        
        ser=col[x].get('actor_id',False)
        if ser:
            s.append(ser)
    
    for i in s:
        if i not in itm:
            itm.append(i)

    return itm
f=open('data/result.json',encoding='utf8').read()
data=json.loads(f)
print(find_all_users_id(data))
