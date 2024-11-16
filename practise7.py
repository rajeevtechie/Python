#Reading a file.
f = open("testing.txt","r")
file = f.read() #reads the entire data. 
print(file)
print(type(file))
f.close()


g = open("testing.txt","r")
print(type(g.read(6))) #if we want to read a particular data.
g.close()
print(g.read()) #it won't print the data inside the file because the file is closed above.

h = open("testing.txt","r")
line1 = h.readline()  #reads only one line at a time.
print(line1)
line2 = h.readline() #but if we have already all line above by using "read", there won't be anything print in "readline".
print(line2)
line3 = h.readline()  #in this way we can read line by line.
print(line3)

#Writing to a file.
i = open("testing.txt", "w")
i.write("this is a new line to the file.") #overwrites the entire file).
i.close() #now testing file has only one above line.

j = open("testing.txt","a")  #"w" and "a", creates a new file if the file is not there.
j.write("Life has been quite good till now.") #adds a new line to the file.

k = open("testing.txt","r+")
k.write("This is") #adds "this is" at the beginning.
print(k.read())

l = open("testing.txt","w+")
l.write("this is") #truncates entire file and adds "this is".
 
m = open("testing.txt","a+")
m.write("that's it.") #adds "that's it at the end."
m.read()
m.close()

#with syntex
with open("testing.txt","r") as n:
    print(n.read())

#Deleting a file.
import os
os.remove("random.txt")

#Practise Questions:
"""
#Qn.1: Create a new file "practice.txt" using python.Add the following data in it:
Hi everyone
I'm are learning file I/O
using java
i like programming in java
"""
o = open("practice.txt","w")
o.write("Hi everyone.\nI'm learning file I/O.\nusing java. \nI like programming in java.")
o.close()

#Qn.2: WAF that replace all occurence of "python" with "java" in above file
def replace():
    with open("practice.txt","r") as p:
        data = p.read()

    new_data = data.replace("java","python")
    print(new_data)

    with open("practice.txt","w") as q:
        q.write(new_data)

replace()

# Search if the wprd "learning" exists in the file or not.
word = "learning"
with open("practice.txt","r") as r:
    file1 = r.read()
    if(file1.find(word) != -1):
        print("Found")
    else:
        print("not found")

"""
#Qn.4: WAF to find in which line of the file does the word "learning" occure first.
Print -1 if the word not found.
"""
def find_line():
    word1 = "learning"
    data1 = True
    line_no = 1
    with open("practice.txt","r") as s:
        while data1:
            data1 = s.readline()
            if (word1 in data1):
                print(line_no)
                return 
            line_no +=1
    return -1

print(find_line())

#Qn.5: From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("numberfile.txt","r") as t:
    data2 = t.read()

    numbers = data2.split(",")
    print(numbers)
    for val in numbers:
        if (int(val) % 2 == 0):
            count +=1

print(count)