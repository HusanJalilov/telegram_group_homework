from read_data import read_data
import json

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    s=[]
    col=data["messages"]
    for x in range(len(col)):
        div=dict(col[x])
        
        if 'actor' in div:
            key=div['actor']
            s.append(key)
        
        
    return s,len(s),type(s)    
    
f=open('data/result.json',encoding='utf8').read()
data=json.loads(f)
print(find_all_users_name(data))

