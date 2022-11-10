import json
dicts=dict()

def loadDict(path,name):
    with open(path,mode="r",encoding="utf-8") as f:
        dicts[name]=json.load(f)
        # print(dicts[name])
        print(f"Loaded:{name} with {len(dicts[name])} words!")

loadDict("jp.json","jp")
while True:
    x=input()
    for i in dicts['jp']:
        if x in str(i):
            print(i)