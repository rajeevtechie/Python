#Functions Definition
def sum(a,b): #a and b parameters.
    sum = a+b
    return sum
print(sum(4,6)) #calling a function

def product(c,d):
    m1 = c*d
    print(m1)
    return m1

product(4,5) #4 and 5 are arguments.

sum(5,43)
product(7,23)

def sum1(e,f):
    return e+f   #return value becomes the value of the function which is used in rest of the program.

addition = sum1(4,45)
print(addition)
#OR
print(sum1(45,43))

def print_hello():
    print("hello world") #since there is no return in it, so will return "none"

print(print_hello())

def average(g,h,i):
    sum = g+h+i
    avg = sum/3
    print(avg)
    return avg

average(34,23,34)

#Default parameters
def prdct(a = 2, b = 4):
    print(a*b)
    
prdct() # in case of no argument, the function takes default parameters.

def prdct1(a,b=3):
    print(a*b)

output = prdct1(7)
print(output) #here "none" will be printed because it is captured in the output varaible.
prdct1(4) # no "none" will be printed though "none" is being returned by the funciton but it is not captured in any variable to print it.
print(prdct1(9)) #"print function" will print "none" here because "none" is returned by the function  

#Qn. 1: WAF to print the length of a list. (list is the parameter.)
fruits = ["mango", "apple", "grapes","papaya","orange"]
country = ["India", "Nepal", "USA","Germany","England","Bhutan", "Canada","New Zealand"]
def length_list(list):
    print(len(list))

length_list(fruits)
length_list(country)

#Qn. 2: WAF to print the elements of a list in a single line.(list is the parameter)
subjects = ["Physics","Chemistry","Maths","English"]
def elements_list(list):
    for elements in list:
        print(elements,end = " ")
        

elements_list(subjects)

#Qn.3: WAF to find the factorial of n (n is the parameter).
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    print(fact)

factorial(5)

#Qn.4: WAF to convert USD to INR.
def currency_convert():
    usd = int(input("Enter the amount in USD: "))
    inr = 84.3*usd
    print("The amount in INR is: ", inr)

currency_convert()
#OR
#Qn.5: WAF to convert USD to INR.
def currency_conversion(USD):
    INR = USD*84.3
    print("The amount in INR is: ", INR)

currency_conversion(56)

#Qn. 6: WAF to print even for even numbers and odd for odd numbers.
def type_number():
    num1 = int(input("Enter the number: "))
    if num1 % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

type_number()

#Recursion: function calls itself repeatedly.
def print_num(n):
    if n == 0:
        return
    print(n)
    print_num(n-1)

print_num(7)

def give(n):
    if n == 0:
        return
    print(n)
    give(n-1)
    print("End")

give(7)

def fact(n):
    if (n ==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

#Qn.7: Write a recursive function to calculate the sum of first n natural numbers.
sum1 = 0
def sum(n):
    if (n==0):
        return 0
    else:
        return sum(n-1) + n

print(sum(5))

#Qn.3: Write a recursive function to print all elements in a list.
brands = ["hp", "asus", "acer", "samsung", "mi"]
def elements(list,index):
    if index == len(list):
        return 
    else:
        print(list[index])
        elements(list,index+1)
        

elements(brands,0)
