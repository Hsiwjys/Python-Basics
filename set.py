"""
In this we are going to see about sets:
    Do not allow Duplicate, Duplicate values will be removed.
    Any type of data can be stored
    We cannot modify the set item but,we can add or remove
items.Sets are unordered.
    add(),update(),remove(),pop()
"""
asa = {1, 2, 3, 4, 1}
print(asa)
# asa[0] = 2 cannot be used , but we can use add function
asa.add(10.1)
asa.add("naan")
print(asa)
asa.remove(3)
print(asa)
asa.pop()
print(asa)
"""
output of last print statement is {2,4,10.1,'naan'} , due to
sets are un order
"""
asa.update([1, 8, 9, 'you'])
print(asa)
"""
Set are commands are completed now we are going to see 
about DICTIONARY{}:
          Do not allow Duplicate, Duplicate value will 
overwrite existing value Any type of data can be stored
get(), keys(), values(), items(), update(),
 pop(), del,clear()
SYNTAX:
        Variable = {
                      keys:values
                    } 
"""
nss = {
    "Name": "my name",
    "Age": 1,
    "Place": "Namakkal",
    "Friends": ["sri", "thiru", "anandan", "naveen"]
}
print(nss)
print(nss.keys())
print(nss.values())
nss["Age"] = 2
print(nss)
nss["colour"] = "red"
print(nss)
nss.update({"Age": 3})
print(nss)
nss.pop("Age")
print(nss)
del nss["colour"]  # if you give del nss => delete dict
print(nss)
nss.clear()
