import json
# import dill

# l = {
#     'name':['hriody','khan'],
#     'age':[20,21],
#     'city':['delhi','mumbai']
# }

# with open('save.json','w') as file:
#     json.dump(l,file,indent=4)

with open('save.json','r') as file:
    l = json.load(file)
    print(l)