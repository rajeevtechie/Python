#Qn. 1: WAP to find the area of a circle,rectangle,square and traingle
print("Consider the mentioned number to select the particular shape.")
print("1 for Circle \n2 for Rectangle \n3 for Square \n4 for Traingle")
shape = int(input("Enter the shape to find the area."))
if shape == 1:
    r = float(input("Enter the radiua of the circle."))
    print("Area of the circle is: ",(22/7)*r**2)
elif shape == 2:
    l = float(input("Enter the length of rectangle:"))
    b = float(input("Enter the breadth of the rectangle: "))
    print("The area of the rectangle is: ",l*b)
elif shape == 3:
    s = float(input("Enter the side of a square: "))
    print("The area of the square is: ", s**2)
elif shape == 4:
    b = float(input("Enter the base of the traingle: "))
    h = float(input("Enter the height of the traingle: "))
    print("The area of the triangle is: ", (1/2)*b*h)
else:
    print("Invalid choice.")

#Qn.3: WAP to determine whether the student passed or not.
n = int(input("Enter the number of subjects: "))
print("Enter the marks of each subject one by one out of hundred.")
sum = 0
for i in range(1,n+1):
    marks = float(input(f"Enter the mark of subject {i}: "))
    sum = sum + marks
    i+=1

total_marks = n*100
percentage = (sum/total_marks)*100
print("Your percentage is: ", percentage)
if (percentage >= 35):
    print("You're PASS.")
else:
    print("You're FAIL.")

#Qn.4: WAP that takes three coefficients a,b and c of a quadratic equation ax2+bx+c =0 as input and compute all possible roots.
a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))
r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
print("the possible roots are: ",r1, "and ",r2)

# Qn. 5: WAP to read three number and prints the value of the largest number.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
if (a>b and a>c):
    print("The largest number is : ",a)
elif (b>a and b>c):
    print("The largest number is: ",b)
else:
    print("The largest number is: ",c)

#Qn. 6: WaP to take the temperature in Celcius and convert it to Fahrenheit.
temp_celcius = float(input("Enter the temperature in celcius: "))
temp_fahrenheit = (9/5)*temp_celcius + 32
print("The temperature in fahrenheit is: ", temp_fahrenheit)

#Qn. 7: WAP to perform different set operations like in mathematics.
u = {2,34,2,3,523,234,23,43,35,32,63,34,1,2,23,45,34,674}
set1 = {2,34,2,3,523,234,23}
set2 = {43,35,32,63,34,1,2,23}
union = set1.union(set2)
print(union)
intersection = set1.intersection(set2)
print(intersection)
print(set1 == set2) #comparison
difference = set1 - set2
print(difference)
print("Length of set1 is: ",len(set1))
print("Lenght of set2 is: ", len(set2))
print(max(set1)) # max() gives the maximum value.
print(max(set2))
print(min(set1)) #gives the minimum value.  
print(min(set2))
print(u - union) #gives the complement of set.

# Qn.8: WAP to check whether a given year is a leap year.
year = int(input("Enter the year: "))
if ( year % 4 == 0 and year % 100 != 0 ) or ( year % 400 == 0 ): 
    print (year," is a leap year .") 
else : 
    print(year,"is not a leap year.")

#Qn.8: WAP to take in the marks of 5 subjects and display the grade.
print("Enter the marks of 5 subjects out of hundred.")
sum = 0
for i in range(1,6):
    mark = float(input(f"Enter the marks of subject {i}: "))
    sum = mark + sum
    i += 1
percentage = (sum/500)*100
print(percentage)
if percentage <=100 and percentage >=90:
    print("Your grade is: A")
elif percentage <=89 and percentage >=80:
    print("Your grade is: B")
elif percentage <=79 and percentage >=70:
    print("Your grade is: C")
elif percentage <=69 and percentage >=60:
    print("Your grade is: D")
else: 
    print("Your grade is: E")

#Qn. 9: WAP to check if a date is valid and print the increment data if it is.
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
# Validate year, month, and determine max days in a month
if year >= 1 and 1 <= month <= 12:
    # Days in each month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    elif month == 2:   # Leap year check for February
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    if 1 <= day <= max_days:   # Validate day
        print("The date is valid.")

        if day < max_days: # Increment the date
            day += 1
        else:
            day = 1 #if date is 31 and month november than it sets day 1 and later on increases the month by 1.
            if month == 12:  # Move to the next year
                month = 1
                year += 1
            else:
                month += 1

        print(f"The next date is: {day}/{month}/{year}")
    else:
        print("The date is invalid.")
else:
    print("The date is invalid.")

#Qn.10: WAP to find the factorial of a number.
num = int(input("Enter the number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
    i +=1
print(f"The factorial of {num} is: ",fact)

# Qn. 11: WAP to print an different star pattern.
for i in range(1,5):
    print(i*"*") #The * operator is used here to repeat the character i times.
    i +=1

for j in range(1,5):
    for k in range(j,6):
        print(k*"*")
        k +=1
    j +=1
ht = int(input("Enter the height of the pattern."))
for i in range(0,ht):
    print("*"*(ht-i))

l=[]
for a in range(0,3):
    elmt = int(input("Enter the numbers: "))
    l.append(elmt)
    a+=1
print(l)
for i in range (3):
    for j in range(3):
        for k in range(3):
            if (i!=j and j!=k and i!=k): #for non repeating of same digits in any digits.
                print(l[i],l[j],l[k])
               
