#converting from float, complex, bool, str to int
a=10.4
converted_a=int(a)
print(type(converted_a))
print(converted_a)

#a=(10+5j)
#a=int(a)
#print(type(a))
#print(a)

a=False
converted_a=int(a)
print(type(converted_a))
print(converted_a)

#a="Hello"
#a=int(a)
#print(type(a))
#print(a)

#a="10.8"
#a=int(a)
#print(type(a))
#print(a)

#converting from int, complex, bool, str to float
x=10
x=float(x)
print(type(x))
print(x)

#x=(4+9j)
#x=float(x)
#print(x)

x=True
x=float(x)
print(type(x))
print(x)

x="10"
x=float(x)
print(type(x))
print(x)

#x="ten"
#x=float(x)
#print(type(x))
#print(x)


#converting from int, float, bool, str to complex
y=10
y=complex(y)
print(type(y))
print(y)

y=10.9
y=complex(y)
print(type(y))
print(y)

y=True
y=complex(y)
print(type(y))
print(y)

y="10"
y=complex(y)
print(type(y))
print(y)

y="abc"
converted_y=complex(y)
print(type(converted_y))
print(converted_y)