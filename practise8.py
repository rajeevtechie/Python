#OOPS in Python
#Class and object 

#creating a class:
class student:
    name = "Rajeev"

#creating object
s1 = student()
print(s1)
print(s1.name)

class bus:
    color = "blue"
    size = "large"
    seats = "60"
    AC = "yes"
    speaker = "yes"

 
bus1 = bus()
print(bus.color, bus.size, bus.seats, bus.AC, bus.speaker)

class student:
    college_name = "XYZ college."
    print(college_name)
    def __init__(self, name,marks):
        self.name = name
        self.marks = marks

s2 = student("Rajeev",98)
print(s2.name, s2.marks )

s3 = student("Shyam", 97)
print(s3.name, s3.marks)

