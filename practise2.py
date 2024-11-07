str1 = "This is a string. String is a datatypes that stores a sequence of characters"
str2 = 'This is also a strig'
str3 = '''This is a string as well'''
str4 = "This is a rajeev's string"
print("This is a string")
print("This is a string. \n is a escape sequence character that changes the line")

#concatenation
print("Rajeev" + "Gupta") #RajeevGupta
st1 = "Hello"
st2 = "world"
st = st1 + st2
print(st)
print(len(st)) #spaces are also counted along with special characters and digits

#indexing: spaces are also counted in indexing
s = "rajeev gupta"
print(s[2]) 
print(s[6]) #we can access a particular string using index but cannot edit a particular value using indexing . for eg.
# s[3] = d #here i am trying to edit the digit in index 3 with d
# print(s) #it shows error

#slicing: accessing part of a string
k = "rajeev kumar gupta"
l = k[0:5]
m = k[4 : 8]
n = k[:3] #[0:3]
o = k[3:]#[3: len(k)]
print(l)
print(m)
print(n)
print(o)
#slicing: negative index
st1 = "rajeev kumar gupta"
print(st1[-4:-2])

#string functions
sr = "rajeev is a very gentle human being"
print(sr.endswith("ing"))
print(sr.endswith("in"))
print(sr.capitalize()) #capitilize the first while printing but doesnot change the initial value
sr = sr.capitalize() #creates new string and capitilize the first letter
print(sr)
print(sr.replace("gentle", "kind"))
print(sr.find("e")) #returns first index of first occurance
print(sr.find("is")) #if we enter the value which is not in the string then it returns -1 becasue -1 is not any such index place from starting.
print(sr.count('e')) # counts the occurence of substring
print(sr.count("is"))

#Qn. 1: WAP to input users's first name and print its length
a  = input("Enter the first name: ")
print("Length of your name is :",len(a))
 
#Qn.2: WAP to find the occurence of '$' in a string
b = input("Enter the string: ")
print(b.count("$"))

#Conditional statements
#to check whether the age criteria for Pan Card is fullfilled or not
age = int(input("Enter your age: "))
if (age >= 18): #always check for the condition
    print("Age eligibility for the for Pan card is fullfilled.")
else: #can only by written only once and always written at last when all the above conditon is false.
    print("The required age for the Pan Card is not reached yet.")

#traffic light
light = input("Enter the color of traffic light: ")
if (light == "red"): # we can add as much as we want "if" and "elif" statements
    print("Stop")
elif (light == "green"): #check the condition only when "if" gives false value.
    print("Go")
elif (light == "yellow"):
    print("Slow down")
else: 
    print("Enter valid color.")

#Grades obtained on the basis of the obtained marks
marks = float(input("Enter the marks obtained: "))
if (marks < 0 or marks > 100):
    print("Enter valid marks.")
elif (marks >= 90 and marks < 100):
    grade = "A"
elif (marks < 90 and marks >= 80):
    grade = "B"
elif (marks < 80 and marks >= 70):
     grade = "C"
else:
    grade = "D"
print("Your grade is:", grade)

#Nesting in conditional statements.
#lets take a example for pan card criterias.
nationality = input("Enter your nationallty:")
if (nationality == "Indian" or nationality == "NRI"):
    print("Your nationality is valid to apply for pan card")
    age1 = int(input("Enter your age: "))
    if (age1 >=18):
        print("Your age is also valid to apply for pan card.")
    else:
         print("But your age criteria is not fulfilled.")
else:
    print("Your nationality is not valid to apply for pan card.")

# #to check a person physically fit enough for driving or not
age2 = int(input("Enter your age: "))
if (age2 >= 18):
    if (age2 >= 90):
        print("Logicallky, you're not physically fit enough for driving a vehicle.")
    else:
        print("You can drive.")
else:
    print("You cannot drive at this early age.")

#Qn. 3: WAP to check if a number entered by the user is odd or even.
num = int(input("Enter the number"))
if (num % 2 == 0):
    print("It is a even number")
else:
    print("It is a odd number")

# Qn. 4: WAP to find the greatest of 3 numbers entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if (num1>num2 and num1>num3):
    print("First is the greatest number:", num1)
elif(num2>num1 and num2>num3):
    print("Second is the greatest number:",num2)
else:
    print("Third is the greatest number:",num3)

# Qn. 5: WAP to check if a number is a multiple of 7 or not.
number = int(input("Enter the number: "))
if (number % 7 == 0):
    print("The entered number is a multiple of 7.")
else:
    print("The entered number is not a multiple of 7.")

# Qn. 6: WAP to find the greatest among four numbers.
num1 = int(input("Enter number 1: ")) #user 1

num2 = int(input("Enter number 2: ")) #user 2

num3 = int(input("Enter number 3: ")) #user 3

num4 = int(input("Enter number 4: ")) #user 4

allNum = {num1, num2, num3, num4}

print("All numbers: ",allNum)

if(num1 > num2 and num1 > num4):

    print("User 1's number is greater")

elif(num2 > num3) :

    print("User 2's number is greater")

elif(num3 > num4) :

    print("User 3's number is greater")

elif(num4 > num2) :

    print("User 4's number is greater")

else :
    print("enter a valid numbers")