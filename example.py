#!/opt/bin/python
#https://github.com/Jayy001/Carta/
import os
import json
import uuid 
import re
import heapq

# Set default font
os.environ["RMKIT_DEFAULT_FONT"]="/usr/share/fonts/ttf/chnfont.otf"

from carta import ReMarkable, Widget 
rm = ReMarkable() 
rm.fontsize = 40

dicts=dict()

def loadDict(path,name):
    with open("/home/root/apps/"+path,mode="r",encoding="utf-8") as f:
        dicts[name]=json.load(f)
        # print(dicts[name])
        print(f"Loaded:{name} with {len(dicts[name])} words!")

def wrap(s):
    res=[]
    ns=""
    count=0
    for i in s:
        ns+=i
        if ord(i)<=ord('z'):
            count+=1
        else:
            count+=2
        if count>=90:
            res.append(ns+"-")
            ns=""
            count=0
    res.append(ns+"==")
    return res
# loadDict("testdict.json","TestDict")
loadDict("idiom.json","成语词典")
loadDict('jp.json',"日本語辞書")
loadDict("cn.json","汉语词典MDBG")

searchbox = Widget(id="sbox", typ="textinput", value="S", x="10%", y="10%",width=100,height=100)
lbl = Widget(id="lbl",typ="label",value="'!'全匹配。'?'反向。==",x="50%",y="10%")
rm.add(searchbox,lbl)

tmplbls=[]

while True:
    res = rm.display()
    print(res)

    # Initialize
    for i in tmplbls:
        print("Removing",i)
        rm.remove(i)
    tmplbls.clear()
    count=0
    rm.eclear()

    lbl.value="No result..."
    kw=res['sbox '].lower()

    pq=[]
    

    for i in dicts:
        for j in dicts[i]:
            # print(j)
            check=False

            if len(kw)>0 and kw[0]=='!':
                if j['romaji'].lower() == kw[1:]:
                    check=True
                    v="Strict Searched:"+kw[1:]+"==" 
                    lbl.value=v
            elif len(kw)>0 and kw[0]=='?':
                if kw[1:] in j['ex'].lower():
                    check=True
                    v="Reverse Searched:"+kw[1:]+"==" 
                    lbl.value=v
            else:
                if kw in j['romaji'].lower():
                    check=True
                    v="Searched:"+kw+"==" 
                    lbl.value=v
            
            if check:
                towrap=f"【{j['word']}】（{j['pron']}）{j['ex']}--{i}"
                pq.append((len(j['romaji']),towrap))
                pq.sort()
                if len(pq)>10:
                    pq.pop()

    for i in pq:
        count+=1
        towrap=i[1]
        val=wrap(towrap)
        print(towrap,val)

        for ln in val:    
            y="20%"
            if len(tmplbls)!=0:
                y="step"
            lbl2=Widget(id="lbl_"+str(uuid.uuid1()),typ="label",value=ln,x="50%",y=y)
            tmplbls.append(lbl2.id)
            rm.add(lbl2)



