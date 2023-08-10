#!/bin/python
# Author: Herdev Anish
# version: v0 

def convert(list):
    temp = []
    lists =[]
    for i in list:
        temp.append(i.strip().split(":"))
    for things in temp:
        lists.append({"name":things[0],"salary": things[1], "age":things[2],"id":things[3]})
    return lists


file1 = list(open('file1'))
file2 = list(open('file2'))
file1 = convert(file1)
file2 = convert(file2)
for item in file1:   #To check what has changed in file2 compared to file1
    a = 0
    for things in file2:
        if item["name"]==things["name"]:
            a+=1
            if item["salary"]==things["salary"]:
                if item["age"]==things["age"]:
                    if item["id"]==things["id"]:
                        break
                    else:
                        print(f"{item['name']} : ID has changed from {item['id']} to {things['id']}")
                else:
                    print(f"{item['name']} : Age has changed from {item['age']} to {things['age']}")
                    if item["id"]==things["id"]:
                        break
                    else:
                        print(f"{item['name']} : ID has changed from {item['id']} to {things['id']}")
            else:
                print(f"{item['name']} : Salary has changed from {item['salary']} to {things['salary']}")
                if item["age"]==things["age"]:
                    if item["id"]==things["id"]:
                        break
                    else:
                        print(f"{item['name']} : ID has changed from {item['id']} to {things['id']}")
                else:
                    print(f"{item['name']} : Age has changed from {item['age']} to {things['age']}")
                    if item["id"]==things["id"]:
                        break
                    else:
                        print(f"{item['name']} : ID has changed from {item['id']} to {things['id']}")
        else:
            continue
    if a == 0:
                print(f"{item['name']}: Not present in file2")
    

for things in file2:   # To check what items from file 2 are not present in file 1
    a = 0
    for item in file1:
        if things['name']==item['name']:
            a=0
            break
        else:
            a+=1
    if a > 0:
        print(f'{things["name"]}: Not present in file1')


# Testing some functionality
"""
for things in lines1:
    i=0
    for name in lines2:
        for i in range(4):
            if things[i] == name[i]:
                #print(f"True that {things} = {name}")
                i=0
                break
            else:
                #print(f"False that {things} = {name}")
                i += 1
    if i >0:    
        print(f"{things} exists in File 1 but not in File 2")"""
