import json
out=[]

def format(s):
    x=[['āáǎà','a'],['ēéěè','e'],['īíǐì','i'],['ūúǔù','u'],['ǖǘǚǜ','v'],['ōóǒò','o']]
    ns=""
    for i in s:
        if i==' ':
            continue
        ok=False
        for j in x:
            if i in j[0]:
                ns+=j[1]
                ok=True
                break
        if not ok:
            ns+=i
    return ns
with open("idiomraw.json",mode="r",encoding="utf-8") as f:
    ans=json.load(f)
    for i in ans:
        out.append({
            'romaji':format(i['pinyin']),
            'word':i['word'],
            'pron':i['pinyin'],
            'ex':i['explanation']+'★'+i['derivation']
        })

with open("idiom.json",mode="w",encoding="utf-8") as f:
    json.dump(out,f,ensure_ascii=False)
