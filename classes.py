#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Implement a class Person with all the attributes of a 
    person including get() and set() functions
	- the attributes should contain at least following
		first name, last name, date of birth,
            phone number, email, location, gender
	- the init method should accept Name and gender
	- write get() and set() functions to 
        operate on the attributes
	- write set method to set all the values
	- update dob, phone etc using set method
	- write a get() method to get age based on dob"""

import datetime

now = datetime.datetime.now()

class Person:
 
    def __init__(self,fn,ln,gn):
        self.firstname = fn
        self.lastname = ln
        self.gender = gn
    
    def set(self,dob,em,ph,lc):
        self.dob = dob
        self.email = em
        self.phone = ph
        self.location = lc
            
    def get(self,dob):
        age = now.year-date1.year
        #return age
        print(self.firstname,' ',self.lastname)
        print(age)
        
n = input('enter Full name \s')
fn,ln = map(str,n.split(' '))
date_entry = input('Enter a date in YYYY-MM-DD format \s')
year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
em = input('enter email \s')
ph = input('enter phno \s')
lc = input('location \s')
newt = Person(fn,ln,'Male')
newt.set(date1,em,ph,lc)
newt.get(date1)


# In[ ]:


""" Implement a class Student with all the attributes 
    of a student including get() and set() functions
	- the attributes should contain at least following
		first name, last name, student id,
        course name, duration, course stat and end date
	- the init method should accept Name and student id
	- write get() and set() functions to operate on the 
        attributes
	- write __str__() method to print the object details
"""
class Student:
    def __init__(self,na,sid):
        self.Name = na
        self.studentid = sid
        
    def set(self):
        self.coursename = input('enter course')
        self.duration = input('duration ')
        self.coursestat = input('course stat ')
        self.enddate = input('enter end date ')
        
    def get(self):
        return self.coursename
        return self.duration
        return self.coursestat
        return self.enddate
        
    def __str__(self):
        print(self.Name)
        print(self.studentid)
        print(self.coursename)
        print(self.duration)
        print(self.coursestat)
        print(self.enddate)
      
newt = Student('yoyo',123)
newt.set()
newt.get()
newt.__str__()


# In[ ]:


"""Implement Employee class derived from Person class
	- the init method should contain employee id along 
    with name and gender
	- use the base class attributes to update employee data
	- write set and get methods to access class attributes
	- use a global variable to store total number of employees 
      and write a static method to get the count
	- check the object is base class or derived class"""
count = 0
class Employee(Person):
    def __init__(self, eid, name, gen):
        self.eid = eid
        self.name = name
        self.gen = gen
     # Using python built-in staticmethod, @decoration symbol also can be used  
     getNumInstances = staticmethod(getNumInstances)
        
newt = Employee()
newt.set()
newt.get()


# In[ ]:


"""Implement a shape class having attributes color, area etc
	- use inheritance to derive circle, rectangle, triangle
	- use features of polymorphism to find area"""
import math

class Shape:

    def __init__(self, color='black', filled=False):
        self.__color = color
        self.__filled = filled

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color
     
        
class Rectangle(Shape):

    def __init__(self, length, breadth):
        super().__init__()
        self.__length = length
        self.__breadth = breadth

    def get_area(self):
        return self.__length * self.__breadth


class Triangle(Shape):

    def __init__(self, base, height):
        super().__init__()
        self.__base = base
        self.__height = height


    def get_area(self):
        return (1/2)*self.__base * self.__height
   
   
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius


    def get_area(self):
        return math.pi * self.__radius ** 2


r1 = Rectangle(10.5, 2.5)
print("Area of rectangle r1:", r1.get_area())
print("Color of rectangle r1:", r1.get_color())
r1.set_color("orange")
print("Color of rectangle r1:", r1.get_color())

t1 = Triangle(10.5, 2.5)
print("\nArea of triangle t1:", t1.get_area())
print("Color of triangle t1:", t1.get_color())
r1.set_color("orange")
print("Color of triangle t1:", t1.get_color())

c1 = Circle(12)
print("\nArea of circle c1:", format(c1.get_area(), "0.2f"))
print("Color of circle c1:", c1.get_color())
c1.set_color("blue")
print("Color of circle c1:", c1.get_color())


# In[2]:


"""Implement a complex number class containing real and imaginary numbers
	- init method should take real number and optionally imaginary number
	- implement __add__, __del__ and __mul__ methods to add or delete or multiply two objects of this class 
"""
class Complex():
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)
               
    def disp(self):
        print(self.real,'+',self.imag,'j')
a = Complex(2,4)
b = Complex(1,3)
c = a + b
c.disp()

#A = complex(*map(float, input().strip().split()))
#B = complex(*map(float, input().strip().split()))
#print (A+B)


# In[ ]:


"""Implement Manager class derived from Employee class
	- manager has additional roles, project"""

class Manager(Employee):
    def roles():
        print ('role of manger')
    def project():
        print ('project of manager')
        
M = Manager()
M.roles()
M.project()


# In[ ]:




