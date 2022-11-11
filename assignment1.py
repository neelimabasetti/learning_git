#1) what is variable ? what are the rules to define variable ?
#variable: It is a container for storing the data values.
#Rules:-
#1.variable name should not start with digits
#2.It allows only alphabets, digits(0-9) and underscore symbol only
#3.These are case sensitive


#2) what is the datatype? how many datatypes in python with example ?
#Datatype represents which type of data can store in that particular variable.
# There are 2 datatypes in python:
# 1)primitive datatypes
# int,float,bool,string,complex
# 2)Data structures
# bytes,bytearray,range,list,set,tuple,dictionary,frozenset

#3) what is the output ?   # here ( _ means underscore)
#_ = 10
#__ = 20
#print(_ + __)
#o/p:30

#4) what is the output of below code snippet ?
# x=10
# y=complex(x)
# print(y)
#o/p:(10+0j)

# 5) what is the output of below code snippet ?
# if=100  #if and else both are keywords
# else=20
# print(if+else)
# o/p:SyntaxError: invalid syntax

# 6) what is the output of below code snippet ?
# x = 65
# y = chr(x)
# print(y)
#o/p: A

# 7) what is list ? how to define the list with example ?
#list:List is a datastructure, it can store multiple different type of elements, list is mutable, it can follow insertion order
#It will allow duplicate elements, if we want to add the elements into the particular list those elements will add by end of the list and startingindex position is 0.
#ex:list=[] and a=list()
# list=[10,40.9,"python",True,(10+4j)]
# print(type(list))
# list.append(10)
# list.append(False)
# print(list[2])
# print(list)
#o/p:<class 'list'>
#python
#[10, 40.9, 'python', True, (10+4j), 10, False]

# 8) x=[10, 20, 5, 6] output: 20
# x=[10, 20, 5, 6]
# print(type(x))
# print(max(x))
#o/p:20

# 9) what is the output of below code snippet ?
# x=[1,2,256]
# print(type(x))
# y=bytes(x)   # It will allow only 0 to 255 ==>0+255=1+255=256
# print(type(y))
# print(y)
# #o/p:
# <class 'list'>
# ValueError: bytes must be in range(0, 256)

# 10) how to find the address of variable ?
#By using id() we can find the address of particuler variable and it is a predefined function.
# a=10
# print(type(a))
# print(a)
# print(id(a))
#o/p:
# <class 'int'>
# 10
# 140716801643592

# 11) what is the difference b / w bytes and bytearry ?
# bytes:These are immutable
#bytearry:This is mutable

# 12) x="Hello python"  output : llo
# x="Hello python"
# print(x[2:5])
# o/p:llo

# 13) x=[1,2,3,4,5,6] output : [1,3,5]
# x=[1,2,3,4,5,6]
# y=[i for i in x if i%2!=0]
# print(y)
#o/p: [1, 3, 5]

# 14) can we convert float to complex ?
#yes, we can convert float to complex
# x=10.5
# y=complex(x)
# print(y)
# o/p:(10.5+0j)

# 15) x=10 ,y="Hi"  output : 10Hi
# x=10
# y="Hi"
# #convert int to string then add two strings
# z=str(x)
# print(z)
# print(z+y)
# o/p:
# 10
# 10Hi

# 16) x=[10,30,50]  output : [50,30,10] #Hint :(use slicing)
# x=[10,30,50]
# print(x[-1::-1])
# o/p:[50, 30, 10]

# 17) x="Hello python"  output : eoyo   #Hint :(use slicing)
# x="Hello python"
# print(x[1:11:3])
# o/p: eoyo

# 18) x="10" y="ten" output : 200*ten?
# x="10"
# y="ten"
# #convert string to int
# z=int(x)
# print(z)
# print(z*y)
#o/p:

# 19) x=True ,y=False z=int(x)+float(y) what is the value of z ?
# x=True
# y=False
# z=int(x)+float(y)   #1+0.0 ==>1.0
# print(z)
# o/p:1.0

# 20) x=["HI",100,"HELLO",20]  o/p : 200 #Hint :(get that last ele of ist and multiply by 2)
# x=["HI",100,"HELLO",20]
# print(type(x))
# for i in x:
#     if i==100:
#        print(i*2)
#o/p:
#<class 'list'>
# 200
