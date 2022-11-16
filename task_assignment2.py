# 1) difference b/w List and set with example?
#list:It is mutable, list is enclosed with []braces, it will allow duplicates, here we can fetch elements through index and it follows insertion order
#ex1:
# list= [1,2,4,4,3,3,3,6,50]
# print("List contains multiple and duplicate numbers:")
# print(len(list))
# print(list.count(4))
# print(list[3])
# print(list[6])
# print(list[8])
# list.append(100)
# print(list)
#o/p:
# List contains multiple and duplicate numbers:
# 9
# 2
# 4
# 3
# 50
# [1, 2, 4, 4, 3, 3, 3, 6, 50, 100]
#ex2:
# list=[["python",True,9],[5.6,"java",(10+0j)]]
# print(list)
# print(list[0][0])
# print(list[1][2])
#o/p:
# [['python', True, 9], [5.6, 'java', (10+0j)]]
# python
# (10+0j)
#set:It is mutable, it is enclosed with {}braces, it doen't allow duplicates and it doesn't follow any order
#ex:
# set={1, 2, 4, 4, 3, 3, 3, 6, 5}
# print("set elements:")
# print(set)
# set.add("hi")  #adding single element to the set
# set.update("python","hello")
# set.add((8,10))
# print("after adding the elements to the set:")
# print(set)
#o/p:
# set elements:
# {1, 2, 3, 4, 5, 6}
# after adding the elements to the set:
# {1, 2, 3, 4, 5, 6, 'l', 'hi', 'p', 'h', 'y', 'o', (8, 10), 't', 'e', 'n'}


# 2) difference b/w set and dict with example?
#set:It is mutable, it is enclosed with {}braces, it doen't allow duplicates and it doesn't follow any order
# set={"python",10,4.5,"hi"}
# print(set)
# for i in set:   #accessing elements using for loop
#     print(i,end=" ")
# print("\n")
# print("hi" in set)
#o/p:
# {10, 'python', 4.5, 'hi'}
# 10 python 4.5 hi
#
# True

#Dict:It should be key:value pair, dict is mutable and data can be accessed using keys.
#duplicate keys are not allowed but duplicate values can be allowed, it supports both homo and hetrogenious
# dict={"empno":10,"empname":"neelu","empphno":3757593599,"empaddress":{"H-no":9787,"street-addr":"w foothill dr","city":"peoria","state":"AZ","zipcode":85674}}
# print("Dictionary:")
# print(dict)
# print(dict.keys())
# print(dict["empaddress"].keys())
# print(dict["empphno"])
# dict["empname"]="Advaith"  #update empname
# dict.pop(("empaddress"))  #it removes the particular key-value
# print(dict)

#o/p:
#Dictionary:
# {'empno': 10, 'empname': 'neelu', 'empphno': 3757593599, 'empaddress': {'H-no': 9787, 'street-addr': 'w foothill dr', 'city': 'peoria', 'state': 'AZ', 'zipcode': 85674}}
# dict_keys(['empno', 'empname', 'empphno', 'empaddress'])
# dict_keys(['H-no', 'street-addr', 'city', 'state', 'zipcode'])
# 3757593599
# {'empno': 10, 'empname': 'Advaith', 'empphno': 3757593599}


# 3) x=[1,2,3,5] # add 10 to all elements o/p :[11,12,13,15]
#
# x=[1,2,3,5]
# for i in x:
#     print(i+10,end=",")

#o/p: 11,12,13,15,



# 4) x=[1,3,2,4,2,5,3] remove dupicates from list o/p :[1,2,3,4,5] #Hint(Use typecasting)
# x=[1,3,2,4,2,5,3]
# print(type(x))
# y=set(x)
# print(y)
# print(type(y))
# print(list(y))
#o/p:
# <class 'list'>
# {1, 2, 3, 4, 5}
# <class 'set'>
# [1, 2, 3, 4, 5]

# 5) z={'A':100,'B':200,'A':300} find the syntax is correct or not ?
#dictionary doesn't allow duplicate keys, if we give duplicate keys also it will override the data(means it will take updated value)
# z={'A':100,'B':200,'A':300}
# print(type(z))
# print(z)
#o/p: {'A': 300, 'B': 200}

# 6) x={'A':[1,2,3],'B':{4,5,6,4,7} 'C':(8,9,10),'D':{'i':200,j:500}} print the all the values from dict?
# x={'A':[1,2,3],'B':{4,5,6,4,7},'C':(8,9,10),'D':{'i':200,'j':500}}
# print(type(x))
# print(x['A'])
# print(x['B'])
# print(x['C'])
# print(x['D'])
# print(x.keys())   #It will print all the keys in the dictionary
# print(len(x))
# print("List:",x.get('A'))
# print("set:",x.get('B'))
# print("tuple",x.get('C'))
# print("dict:",x.get('D'))
# print(x['D'].keys())
# print(x['D'].values())
# print(x['D'].items())
# print(x.get('E'))
#o/p:
# <class 'dict'>
# [1, 2, 3]
# {4, 5, 6, 7}
# (8, 9, 10)
# {'i': 200, 'j': 500}
# dict_keys(['A', 'B', 'C', 'D'])
# 4
# List: [1, 2, 3]
# set: {4, 5, 6, 7}
# tuple (8, 9, 10)
# dict: {'i': 200, 'j': 500}
# dict_keys(['i', 'j'])
# dict_values([200, 500])
# dict_items([('i', 200), ('j', 500)])
# None

