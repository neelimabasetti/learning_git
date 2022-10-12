#d={}
#print(d)
#print(type(d))

#d=dict()
#print(d)
#print(type(d))

student_info={
"rollno":"123",
"studentname":"neelu",
"studentphno":"23466878",
"stuaddress":{
   "houseno":"9791",
   "streetaddress":"w foothill dr",
   "city":"peoria",
   "state":"az",
   "zipcode":"85383"
   }
}
#student_info["studentname"]="Advaith"
#student_info["college"]="srit"

#print(student_info["studentname"])
#print(student_info["stuaddress"]["city"])
del student_info["stuaddress"]["city"]
print(student_info)

