import json
f=open('result.json',encoding='utf8').read()
data=json.loads(f)
s=data["messages"]
print(len(s),type(s))
