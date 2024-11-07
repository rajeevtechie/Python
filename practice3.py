# Lista in python: lists are mutable
marks = [25.88, 43.76, 94, 54, 87.67, 98]
print(marks)
print(type(marks))
print(marks[3])
print(marks[5])
print(len(marks))
std = ["Rajeev", "is very", "kind", 98] #we can store multiple type of data in list.
print(std)
std[2] = "gentle" 
print(std)
lst1 = [1] #we don't have to give comma at the end in case of list.
print(type(lst1))

#list slicing
age = [45, 43, 42, 65, 23]
print(age[1:3])
print(age[:3]) #same as [1:3]
print(age[1:]) #same as [1:len(age)]
print(age[-4:-2])
print(age[0:4:2]) #substring = s[start : end : step]

#List methods
list = [5, 3, 6, 73, 64]
print(list)
print(list.append(56)) #adds an element at the end
print(list.sort()) #sort the list in ascending order
print(list.sort(reverse=True)) #sort the list in descending order
print(list.reverse()) #reverse the list
print(list.remove(5)) #removes the first occurence of element
print(list.pop(3)) #removes the element at index
print(list.insert(3,98)) #insert element at index [list.insert(index,element)]
##these methods like append, sort,etc make changes in the list but does not return anything so its prints "none"
##so we can print the updated list in the way mentioned below.and all the changes that takes place one by one , take place in updated list.
lst = [54,95,34,64,95,98]
print(lst)
lst.append(77)
print(lst)
lst.sort(reverse = False)
print(lst)
lst.sort(reverse = True)
print(lst)
lst.insert(4,56)
print(lst)
lst.reverse()
print(lst)
lst.insert(10,72) #if we try to insert the element exceeding the index of the elements in the list, it add the element to the last.
print(lst)
lst.remove(95)
print(lst)
lst.pop(3)
print(lst)

#we can also perform these methods in sting values.
fruits = ["pineapple", "apple", "guava", "mango"]
print(fruits)
fruits.append("litchi")
print(fruits)
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits.insert(3, "grapes")
print(fruits)
fruits.reverse()
print(fruits)
fruits.remove("grapes")
print(fruits)
fruits.pop(3)
print(fruits)

#tuple
tup = (1,) #it is a tuple but (1) is not tuple instead it is taken as a integer by the python.
print(tup)
print(type(tup))
tup1 = (1,3,4,5,6,7,6,8,6) #here it is also a tuple but when don't need to give comma at the end due to multiple elements.
print(tup1)
print(type(tup1))
print(tup1[:3])
print(tup1.index(5)) #returns the index of the first occurence
print(tup1.count(6)) #counts the total occurences

#Qn. 1: WAP to ask the user to enter names of their 3 favourite movies and store them in a list.
movie1 =  input(("Enter the your first favourite movie: "))
movie2 =  input(("Enter the your second favourite movie: "))
movie3 =  input(("Enter the your third favourite movie: "))
movies = []
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)
#same program(Qn. 1) can be written in short form as well.
mov = []
mov.append(input("Enter your first favourite movie: "))
mov.append(input("Enter your second favourite movie: "))
mov.append(input("Enter your third favourite movie: "))
print(mov)

# Qn. 2: WAP to take input of list from user and check if a list contains a palindrome of elements.
ls = list(input("Enter the elements of the list with , :").split(','))
print(ls)
ls_reversed = ls[::-1] #reversed using slicing
print(ls_reversed)
if (ls == ls_reversed):
    print("The list contains a palidrome of elements")
else:
    print("The list does not contain a palidrome of elements")

#the same above problem can be solve in another way as well which is discussed below.
ls = list(input("Enter the elements of the list with , :").split(','))
print(ls)
copy_list = ls.copy() #it creates a copy of original list and changes made in the new list does not reflect in original list.
copy_list.reverse() #it reverses the original list. it does not return new list and changes made in it reflect in the original list.
print(copy_list)
if (ls == copy_list):
    print("The list contains a palindrome of elements.")
else:
    print("The list does not contain a palindrome of elements.")

#Qn.3.1: WAP to count the number of student with a "A" grade in the following tuple
#("C","D","A", "A", "B", "B", "A")
tuple = ("C","D","A", "A", "B", "B", "A")
print(tuple.count("A"))
#Qn. 3.2: Store the above values in a list and sort them from "A" to "B"
grade= ["C","D","A", "A", "B", "B", "A"]
grade.sort()
print(grade)
