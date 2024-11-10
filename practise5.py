# # loops in python: they are used to repeat instructions in a program.
"""
# while loops:Often used in situations where the number of iterations is not 
 predetermined.(until a condition becomes false)
""" 
i = 1
while i <=4:
    print("Rajeev")
   
    i +=1
j = 1
while j<=6:
    print(j, "Ramkesh")
    j += 1
print(j)

# Print numbers from 5 to 20.
k = 5
while k<=20:
    print(k)
    k +=1

#print numbers from 30 to 20
l = 30
while l>=20:
    print(l)
    l -= 1

#Qn. 1: Print numbers from 1 to 100
num1 = 1
while num1<=100:
    print(num1)
    num1 += 1

#Qn.2: Print numbers from  100 to 1.
num2 = 100
while num2 >=1:
    print(num2)
    num2 -=1

#Qn.3: Print the multiplication table of a number entered by the user.
n = int(input("Enter the number."))
num3 = 1
while num3<=10:
    print(n*num3)
    num3 +=1

"""
#Qn.4: Print the elements of the following elements using a loop.
[1,4,9,16,25,36,49,64,81,100]
"""
num4 = [1,4,9,16,25,36,49,64,81,100]
index = 0
while index<=(len(num4)-1):
    print(num4[index]) #num4[0], num4[1], num4[2]...
    index +=1

"""
#Qn.5: Search for a number x in the tuple using loop.
(1,4,9,25,36,49,64,81,100)
"""
x = int(input("Enter the number to be identified."))
num5 = (1,4,9,16,25,36,49,64,81,100)
u = 0
while u < len(num5):
    if(num5[u] == x):
        print("The number is found at index:",u)
    else:
        print("Not found at index:",u)
    u +=1

#Break statement:terminate the entire loop
s = 1
while s <= 7:
    print(s)
    if (s == 5):
        break #it terminates the current loop prematurely..(the entire loop is terminated)
    s +=1

x = int(input("Enter the number to be identified."))
num5 = (1,4,9,16,25,36,49,64,81,100)
r = 0
while r < len(num5):
    if(num5[r] == x):
        print("The number is found at index:",r)
        break
    else:
        print("the  number is not found at index:",r)
    r +=1

# #For eg: To find if a number is primt or not.
a = int(input("Enter the number: "))
b = 2
while b == (a-1):
    if (a % b == 0):
        print("It is not a prime numebr")
        break
    else:
        print("It is a  prime number")
        break

#Continue statement:used to Skip a particular thing
q = 0
while q <=6:               
    if (q == 3):   # {when q = 3, while condition and if condition are true so by the increment in if condition, 
        q +=1      # q becomes 4 and continue prevents the execution of further block of code.}
        continue  # {the loop doesn't terminate; instead, it jumps to the next iteration, 
    print(q)      #skipping any remaining statements in the current iteration.}
    q +=1
 
#for eg 1: to print odd numbers less than 10
w = 1
while w<=10:
    if (w % 2 == 0):
        w +=1
        continue 
    print(w)
    w+=1
    
#For eg2: to print the even numbers less then 10
e = 1
while (e<=10):
    if (e%2!=0):
        e+=1
        continue
    print(e)
    e+=1


"""
for Loops: The loop continues for a fixed number of iterations 
    or over elements in a sequence(Often used for iterating over a known sequence).
    eg. for traversing list,string, tuples,etc.

syntax: for "variable" in "sequence":
            # Code block to execute
variable is a temporary placeholder that takes the value of 
the current element from the sequence(from 0 index) during each iteration.
"""

lst1 = [1,3,5,6,9]
for val in lst1:
    print(val)

fruits = ("apple", "mango", "guava","grapes", "banana")
for fr in fruits:
    print(fr)

name = "Rajeev"
for nm in name:
    print(nm)

location = "india"
for ln in location:
    if (ln == "i"):
        print("Found i")
        break
else:  #(completely optional to use in for loop)
    print("end")  

#Qn.6: Using for loop, print the elements of the following list.
#[1,4,9,25,36,49,64,81, 100]

lst2 = [1,4,9,25,36,49,64,81, 100]
for val1 in lst2:
    print(val1)

"""
#Qn.7: Using for loop, search for a number x in the tuple.
(1,4,9,25,36,49,64,81,4,36, 100)
"""

lst3 = (1,4,9,25,36,49,64,81,4,36, 100)
srch = int(input("Enter the number to be identified."))
idx = 0
for val2 in lst3:
    if (val2 == srch):
        print("found at index", idx)
    idx +=1    #if we want to print only once than we can use break statement.
    
#Range function: Returns a sequence of numbers staring from 0 (by default if not provided) and increment by 1 (by default.)
for nm in range (6):  #range(start?,stop,step?)
    print(nm) #output: 0,1,2,3,4,5

for nm1 in range (3,7):
    print(nm1) #output: 3,4,5,6

for nm2 in range(2,8,1):
    print(nm2)

for nm3 in range(4,10,2):
    print(nm3) #output: 4,6,8

#for eg: to print even numbers between 1 to 15.
for nm4 in range(2,15,2):
    print(nm4)

#for eg: to print odd numbers between 1 to 15.
for nm5 in range (1,15,2):
    print(nm5)

#Qn.8: using for & range(), print the numbers from 1 to 100
for nm6 in range(1,100):
    print(nm6)

#Qn.9: Using for and range(), print numbers from 100 to 1.
for nm7 in range(100,0,-1):
    print(nm7)

#Qn.10: using for and range(), print the multiplication of a number z
z = int(input("Enter the number:"))
for num8 in range(5,53,z):
    print(num8)
#OR
z1 = int(input("Enter the number"))
for num9 in range (1,11):
    print(num9*z1)

#Pass statement: it does nothing and used as a placeholder for futute code.
for rj in range(8):
    pass

rj1 = 1
if rj1 <= 7:
    pass

#Qn. 11: WAP to find the sum of first n natural numbers using while.
number = int(input("enter the number to which we have to find the sum:"))
sum = 0
rtm = 1
while (rtm <= number):
    sum = sum + rtm
    rtm += 1
print("the sum upto the number is: ", sum)

# Qn. 12: WAP to find the factorial of first n numbers using for.
number1 = int(input("Enter the number whose factorial is to be found:"))
fact = 1
for i in range(1,number1+1):
    fact = fact*i
print("factotail of the number is :", fact)

