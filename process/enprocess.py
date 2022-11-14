import json
import csv 
out=[]

def ft(s):
    return s.replace("\\n","☆").replace("\\r","")
with open("ecdict.csv",mode="r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(row)
        if row['word'][0] in ".-'0123456789":
            continue
        if " " in row['word']:
            continue
        x={
            'word':row['word'],
            'pron':row['phonetic'],
        }

        ex=ft(row['translation'])+"★"
        # if row['definition']!="":
        #     ex+=ft(row['definition'])+"★"
        if row['oxford']!="":
            ex+="[牛津三千词]"
        if row['tag']!="":
            ex+="[标签]"+row['tag']
        if row['exchange']!="":
            ex+="[词形变化]"+row['exchange']
        x['ex']=ex
        # print(x)
        # input()
        out.append(x)

with open("en.json",mode="w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False)
