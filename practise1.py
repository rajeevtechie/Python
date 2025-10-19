#exploring varaibles in python
name = "Rajeev Gupta"
age = 20
study = 'B. Tech (Running)'
activity = '''Learning Python(securing the future)'''
hobby = "Playing Cricket"
medals = 1.00
POTM = False
print("My name is :",name)
print("My current age is : ",age)
print("Academic qualification : ",study)
print("My favourite hobby is :",hobby)
print("No. of gold medals received in crickey:",medals)
print("My current activity is: ",activity)
print(type(name))
print(type(age))
print(type(medals))
print(type(study)) 
print(type(POTM))

#logical use of variables (eg. performic sum of two numbers)

c = 22
d  = 33 
sum = c+d
print("sum of the given numbers is:", sum)

#performing some other arithmentic operations
a = 34
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#relational operators
num = 20
num = num + 5
num += 5 #+= is equivalent to num + 5
num -= 5
num *= 5
num /= 5
num %= 5
num **= 5
print(num)
 
#Logical operators
print(not False)
print(not True)

g = 20
h = 10
print(not (g > h))
val1 = True 
val2 = False
print("AND operator: ", val1 and val2)
print("OR operator: ", val1 or val2)
print("OR operator : ", (g > h) or (g == h))

# type conversion(python itself change the data type)
k = 4 
l = 6.65
sum = k+l # k=4.0, l=6.65
print(sum)
s = "4" 
t = 6.65
sum1 = s + t
print(sum1)

#type casting(we convert data type manually ourselves)
m = int("4") 
n = 6.65
sum = m + n # m=4.0, n=6.65
print(sum)
print(type(m))
o = 7.4
o = str(c)
print(type(o))

#input(accept the values from the user)(always take value in string type)
input("What is your age: ")
name = input("Enter your name: ")
print("Hello!", name)
marks =int(input("Enter the marks: "))
print(type(marks))

#Qn.1: write a program to input 2 numbers and print their sum
N1 = int(input("Enter the first number"))
N2 = int(input("Enter the second number"))
print("The sum of the given two numbers is : ", N1+N2)

#Qn. 2: WAP to input side of square and print its area
z = float(input("Enter the length of the side of ther square: "))
print("The area of the square is :", z*z)

#Qn. 3: WAP to input 2 floating point numbers and print their average
first = float(input("Enter the first floating number: "))
second = float(input("Enter the second floating number: "))
print("Their average is: ", (first + second)/2)

# Qn. 4: WAP to input 2 int numbers a and b. Print True if a greater than or equal to b. If not print False
u = int(input("Enter the first number"))
v = int(input("Enter the second number"))
print((u > v) or (u == v))