import os
rep=os.walk("D:\\Company")

d1={}
for r,d,f in rep:
    for file in f:
        d1.setdefault(file,[]).append(r)

file_name=input("Enter your File Name :") 
for k,v in d1.items():
    if file_name.lower() in k.lower():
        print(k,":",v)   
        for find_file in v:
            print(find_file)