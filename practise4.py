#Dictionary in Python: unordered(no particular index) and mutable
dict1 = {
    "key" : "value",
    "name" : "Rajeev",
    "age" : 18,
    "marks" : 98.5,
    "is adult" : True,
    "skills" : ["c", "html", "css", "javascript", "python"],
    "topics" : ("list", "tuples", "dictionary"),
    98 : 84  #key and value can be of any data type.
}
dict1["name"] = "Rajeev Gupta" #can change the value in dictinary
dict1["middle name"] = "kumar" #can add new key to the dictionary
print(dict1["name"])
print(dict1["age"])
print(dict1["marks"])
print(dict1["is adult"])
print(dict1["skills"])
print(dict1["topics"])
print(type(dict1))
print(dict1)

# #we cannot give two same key in a dictionary, in case we do, then the second key-value pair will overwrite the first one
# #for eg:
d = {
    "key" : 'value1',
    "key" : "value2"
}
print(d) #output: {"key" : "value2"}

null_dict = {} #can create null dictionary
print(null_dict)
null_dict["new key"] = "new value" #can add a new value to a null dictionary
print(null_dict)

#Nested Dictionaries
student = {
    "name" : "Rajesh Gupta",
    "subjects" : {
        "physics" : 98,
        "chemistry" : 96,
        "maths" : 97
    }
}
print(student)
print(student["subjects"]) #we can print the subdictionary only as well here.
print(student["subjects"]["physics"]) #we can print the particular key value from the subdictionary only as well here.

#Dictionary methods
print(student.keys()) #returns all the keys.
#print(student[subjects.keys()]) #we cannot return the keys of nested dictionary.
print(len(student))
print(list(student.keys())) #type casted 
print(student.values()) #returns all the values.
a = list(student.values()) #type casted and stored in a separate variable.
print(a)
a.append("applied science")
print(a)
print(student.items()) #returns all (key,value) pair as tuples.
b = list(student.items())
print(b[0])
print(student.get("name")) #it returns none if the key does not exist in the dictionary  #output: Rajesh Gupta. #returns the key according to value.
print(student["name"]) #it returns error if no key exist in the dictionary
student.update({"Locatin" : "India"}) #inserts the specified items to the dictionary.
print(student)


#Sets in python: Sets are mutable but Elements of sets are unique and immutable
set1 = {3,4,4,5,5,6,"Rajeev", "Gupta"} #does not print the duplicate items
print(set1)
print(type(set1))
print(len(set1)) #does not count the duplicate value.
set2 = {} #not a empty dictionary not a set
print(set2)
print(type(set2))
set3 = set() #syntax to create a empty syntax
print(type(set3))

#Set Methods
set = {2,35,3,5,3,2,3,5,"Rajeev", "Gupta",45,34}
collection = {3,3,45,6,4,"Rajeev"}
set.add("Rahul") #adds an element to the set. #"add" returns none so we need to print it separately.
print(set)
# set.add([2,3])
# print(set) #it gives type error because list is mutable so it can not be the element of set.
set.remove(3) #removes  the element from the set.
print(set)
set.remove(6) #if we try to remove the element which is not in the set, then it returns keyerror.
print(set)
set.clear() #empties the set
print(set)
print(len(set)) #outpur: 0
print(set.pop()) #removes a random value
print(set)
print(set.union(collection)) #combines both set and return new.
print(set.intersection(collection)) #combines common values and return new.

"""
Qn. 1: Store following word meaning in a python dictoinary:
table : "a piece of furniture", "list of facts and figures"
cat : "a small animal"
"""
dict1 = {
    "table" : ["a piece of furtniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(dict1)


"""
Qn. 2: You are given a list of subjects for students. Assume one classroom is required 
for 1 subject. How many classroom are needed by all students.
"python", "java", "C++", "python", "javascript", 
"java", "python", "java", "C++", "C"
"""
class_name = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(class_name))

"""
Qn. 3: WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary and add one by one. Use subjects name as key &  marks as 
value.
"""
marks1 = float(input("Enter the marks of the first subject: "))
marks2 = float(input("Enter the marks of the second subject: "))
marks3 = float(input("Enter the marks of the third subject: "))
dictionary = {}
dictionary.update({"first subject marks" : marks1})
dictionary.update({"second subject marks" : marks2})
dictionary.update({"third subject marks" : marks3})
print(dictionary)

"""
Qn. 4: Figure out a way to store 9 and 9.0 as separate values in the set.
(You can take help of built-in data types)
"""
num = {9, "9.0"}
print(num)