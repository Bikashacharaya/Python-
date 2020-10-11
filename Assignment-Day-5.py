hydra={'Nick Fury': 'Tony Stark,Maria Hill,Norman Osborn','Hulk':'Tony Stark,HawkEye,Rogers', 'Rogers':'Thor','Tony Stark':'Pepper Potts,Nick Fury','Agent-13':'Agent-X,Nick Fury,Hitler','Thor':'HawkEye,Black Widow','Black Widow':'HawkEye','Maria Hill':"Hulk,Rogers,Nick Fury",'Agent-X':"Agent-13,Rogers", 'Norman Osborn': "Tony Stark,Thor"}

value=[]


list1=list(hydra.keys())
list2=list(hydra.values())
list3=set(list1)
def splitvalues(l):
    return l.split(',')

for each in list2:
    value.extend(splitvalues(each))

list1.extend(value)

s1=set(list1)
v111=[]
keys=['Nick Fury']

def findhydra(k):
    v111.extend(splitvalues(hydra[k]))
    
        
for k,v in hydra.items():
    if k in keys:
        keys.extend(splitvalues(hydra[k]))
kl=set(keys)
y=list3.intersection(kl)

for i in y:
    findhydra(i)

v222=set(v111)
print(s1-v222)

