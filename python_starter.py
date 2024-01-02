# first python program

a=10
print(float(a))

#round pow and abs
b=20.3456
print(round(b,2), type(b))

c=10
print(pow(c,10))

d=-5.5
print(abs(d))

#math functions == isnan,isfinite,exp,log,sqrt,pi
num=20

import math
math.isfinite(num)
math.isnan(num)
print(num ** 0.5)
round(math.sqrt(num),4)

math.exp(num)
math.log(num)
math.pi
# Strings type
str_1 = """ Hello Write it this Way.
i have  written it and revise
"""
print(str_1)
str_3 = 'The Text\n\n\nt\tare orderedly arranged'
print(str_3)

#string as an array, slice strings
var_str = "String Variable"
print(var_str[-1])
#slicing
print(var_str[7:15])
#negative slicing
neg_1 = "Try negatively" 
print(neg_1[-10:-3])
#concatenation
t1 = "Hi"
t2 = "spyder"
print(t1 + " " + t2,type(t1)) 

#"spyder" in t2 "spyder" not in t2

#String format using %
print("Age is in a float format %f where it is majorly a %s"%(20.00,"Date"))
#new way
print("Age is in a float format {0} where it is majorly a {1}".format(20,'Date'))

#raw strings
locate = r"C:\users\desktop"
print(locate)

print("I love to %s to %i"%("python",20))

print("I love to {name} to {age}".format(name ="messi",age = 10))

#more strings methods
strings = "Checking String formats"
strings.lower()
#len(strings) string length, strings.index('strings'),find(),index(),count()

#strings aligne
var_algn = "Python"
var_algn.rjust(12,"0")
#similarly for ljust => left justification

#spliting strings
var_split = "Ibrahim,M,19,300000,Programmer"
name,sex,age,salary,occupation = var_split.split(sep = ",")

#isnumeric method to check for numeric values
age.isnumeric()
#convert to integer for mathematical operations
age = int(age)
salary = int(salary)

#strip method as trim in javascript

#cr - carriage return and lf -line free /r/n
var_strip = "SetUp   ,M,19,  300000,  Engineer\n"
n,s,a,s,r = var_strip.split(sep = ",")

n = n.strip()
r = r.strip("\n")
s = s.lstrip()
print(r)
r = r.replace("Engineer","Developer")

#using real world examples 
var_data = "Ibrahim Is a Programmer and Ibrahim Plays Football"

var_c = input("Enter the current value to be replaced :")
var_n = input("Please enter the new value :")
count = input("Nmber of occurence :")
var_data.replace(var_c,var_n,int(count))

#conditional statement
salary = int(input("please Input Tour Salary:"))
if salary > 5000:
    print("You are eligible to take the loan!")
else:
    print("Your Salary of {value} Is not approved".format(value = salary))
#shortand if (no else to the if)
#if salary > 3000: print("Approved")
#print('approved') if salary > 2000 else print('not approved')

#Leraning Boolean
varB = True
if varB:
    print("The {type} Data is True".format(type = "Boolean"))
else:
    print("Falsehood!")    

#Checking For empty
var_pr = ""
if var_pr:
    print("This Variable Is Filled")
else:
    print("It is a False Statement")    

#Excercise to check empty value
var_empty = "d"
if len(var_empty) == 0:
    print("An Empty Text")
else:
    print("Filled Text")    

#Pass == Do nothing if a condition is checked
if var_empty:
    pass
else:
    print("Nothin inside")

#nestd if and elif statement
amount = int(input("Your Current amount: "))
if amount >= 8000:
    print("Automatic RSVP")
else: 
    if amount >=4000:
        print("Manual Approach")
    else:
        print("Rejectted Approval!")

#better way using elif
acc = int(input("Your Current amount: "))
if acc >= 8000:
    print("Auto RSVP")
elif acc >= 4000:
    print("Manual Approach")
else: 
    print("Rejectted Approval!")

#logical operators and or hint:(and:checks boh cond,or checks one.)
sal = int(input("Your Amounts Is : "))
age = int(input("Whats Your age:"))
if sal >= 1000 and age >= 30:
    print("alreadily approved")
else:
    print("null!")
    
    
#Memberships in if statement (in and not in)
str_key = "Python Programming is Quite Fun"
keyword = (input("Enter Parameter To Search"))    

if keyword in str_key:
    print("The Input Was Found")
else:
    print("Not Found!")
#excercise to check the position found
str_key = "Python Programming is Quite Fun"
keyword = (input("Enter Parameter To Search For: "))    

if keyword in str_key:
    print("The Input Was Found at position {pos}".format(pos = str_key.index(keyword)))
else:
    print("Not Found!")
    
    
#Loops in python!! Basics
# while loop
i = 0;
while i < 100:
    print(i)
    i += 10
#achieving same process with conditional statements
var_con = True
i = 0
while var_con:
    print(i)
    i += 10
    
    if i >= 100:
        var_con = False
   
#For loops in python are only applied on sequences,e.g: strings,list,turple,range[start,step,inc]     
# Bsasics
i = 1
name = "Ibrahim"
for letter in name:
    print("Character number is {}, {}".format(i, letter))
    i += 1

#Ranges in python range(start,stop,step)
for i in range(1,20,2):
    print(i)

#Ranges loop,
name = input('Enter Your Name :')

name_len = len(name)

for i in range(0, name_len,1):
    print('Characters Are {} of {}'.format(i, name[i]))


# using enumerate keyword
name= input('Enter Your Name')

for i,letters in enumerate(name,start=1):
    print("Character number is {}, {}".format(i, letters))

#Cross Multiplaication Table
for i in range(1,19,1):
    print("")
    for j in range(1,20,1):
        result = i * j
        print(result,end=" ")

#two functs for getting out of a loops in a PL are break,continue
for i in range(1,19,1):
    
    #so,if its get a number like 3(odd) skip to the next loop, you can also adjust for break to see the output which stop all.
    if i%2 != 0:
        continue
   
    for j in range(1,20,1):
        result = i * j
        print(result,end=" ")
        
    print("")          

#Collection Data types List,Set,Turple, Dictionary
#list is unique, Turple is immutable, Set is only Chngeable,
# Dictionary is changeable and indexed

#list is like array in javaScript
#initialize lists
list1 = ["hp","omen","pavilion"]
#YOu can create an empty list by using list() function
list2 = list1
list3 = list1.copy()
#assigned same label to list 2
list1.append('Lenovo')
print(list1,list3)

#using the copy() function,it copies but changes to the origin doesnt affects
#accessing values of a list
new_list =  ["hp","omen","pavilion","evo","Razer"]
print(new_list[1]) 
#new_list of -1 gets the last
#accessing a range of values
print(new_list[1:4])
#the code above prints starts from omen to evo(the third ele but you add 1)
#accessing range of negative values

new_list =  ["hp","omen","pavilion","evo","Razer"]
      
print(new_list[-4:-1])
#evo whch is the last is in -2 but we add 1 to it 

#looping through a list to gat all values
for lists in new_list:
    print(lists.upper())

#list add, append , remove update
#updating lists
new_list[-1] = "Acer"
#merge two lists together    
new_list.extend(['jg','kj'])
#insert to a list
new_list.insert(0, 'Dell')
#remove from list: removes value while pop removes index
new_list.remove('jhg')
#append : add to the last list
new_list.append('lol')
#sum values in a list and calculate mean
num_list = [10,20,10,78,90]
#delete a list using del list and clear list using .clear() 
print(int(sum(num_list)/len(num_list)))

#Sorting out a list
num_list.sort()
#descending order
num_list.sort(reverse=True)
#finding index of a list
num_list.index(10)

#excercise to prompt user to input text and form an array with it!!
curr = True
fill_arr = []


while curr:
    arr = int(input("Enter Your Desired Numbers : "))
    fill_arr.append(arr)
    
    if len(fill_arr) == 5:
        curr = False
print(fill_arr)        
#excercise Done!!

#excercis to fin index of a list through prompt.
in_prompt = int(input("Enter a number to Search For : "))

if in_prompt not in num_list: 
    print("The Origin Number of {} was not found ".format(in_prompt))
else:
    position = num_list.index(in_prompt)
    print("The Origin Number of {} was found at pos {}".format(in_prompt, position))
#excercise Done!!
#dynamic_listings: list itself is a data-type, you can store list in list
dy_list = [10,20,30,["Vol", "Pok"],[[30,40],[12,39]]]
print(dy_list[3][0])
dy_list[3].append("Vola")
print(dy_list[4][0][1]) #gets 40 out
print(dy_list[4][1][-1]) #gets 39 out!

#Tuples are immutable () and very fast to be processed you can't change the values like const in js

vr_t1 = (1,2,3)
t2 = (4,5,2)
print(vr_t1 + t2)
len(vr_t1)
vr_t1[1]

#Dictionary is like objects in js with key  and values,but key and values are both in strings!
#or json format
vr_address = {
    "Street": "Apete Ibadan",
    "State": "Oyo State",
    "City": "Ibadan",
    "Number": 36,
    }
#Updatin Dics
vr_address["Street"] = "No 15, Apete Ibadan"
#Adding dictionaries
vr_address['ZipCode'] = "200129"
#delete using del vr_address["ZipCode"]

#acces keys and objects with
#print(vr_address.keys())
#print(vr_address.values())
#print(list(["a","b"]))
#telephone-contact code
var_tel = True
phone_bookarr = []
print('E'.lower())
while var_tel:
    print("  ")
    print("Welcom To the Phonebook App")
    print(" ------------------------------- ")
    print("A- to add contact")
    print("S - to Search")
    print("E - to Exit.")
    keyE = input("Enter Something To Start : ")
    if keyE.lower() == "e":
        var_tel = False
    elif keyE.lower() == 'a':
        name = input("Enter Your Name : ")
        email = input("Enter Your Personal Mail : ")
        phone = int(input("Enter Your Phone Number : "))
        datas = list([name,phone,email])
        #append to empty phonebooks
        phone_bookarr.append(datas)
        if len(phone_bookarr) != 0:
            print("Successfully Created a new Contact!")
            #var_tel = False
    elif keyE.lower() == 's':
        sear_val = input("Enter the Name Value : ")
        for values in phone_bookarr:
            if  sear_val in values:
                pos = values.index(sear_val)
                print("Found {} at {}".format(sear_val,pos))
                print(values)
    else:
        print("You pressed the wrong key, read the docs!")

# Data types of Date and Time In Python
import datetime
print(datetime.date(2004,10,7))
#print(datatime.time(hour,minute,secnd,microsecond))
#get date as well as time in datetime module

date_and_time = datetime.datetime(2015,5,13,15,12,50)
d1 = datetime.date.today()
print(d1)
d2 = datetime.datetime.today()
print(d2)

# Date-time subsraction is the only operation in datetime
from datetime import datetime,date

f_day = datetime(2022,6,9,10,12,30)
s_day = datetime(2023,6,9,10,12,30)

n_day = s_day - f_day
#which gives a different known as timedelta
#replace a date with replace method
#.replace(years = 0)
print(f_day.replace(year=2020))

#dded to a date with timedelta function.timedalte(hours = 10)

#date iso methods and string methods
str(date.today())

#using the strftime methods : changes dates in any format
print(datetime.strftime(f_day, '%m/%d/%y'))
#can also replace with H=hours, M for minutes....
#getting weekdays using strftime format
#a-first 3 letters of the weekday
#A-the weekday
#w - week number
#b - Short month name
#B-full month name
#m - month number
#number which it falls from 0 = Sunday....

from datetime import datetime,date
print(datetime.strftime(f_day, '%a-%A-%w{}'.format('th')))
#converting to a 12 hour format with %I and %p for am or pm


#datetime.strptime is the reverse method for datetime.strftime format i.e Converts string to original date format.
print(datetime.strptime("2019/04/20","%Y/%m/%d"))  #note Capital Y

#File handling in Python :( Open Read Write and Close )
#Modes Of Opening == r=-read a=- append w -= ovewrite 


file_o = open(r"C:\Users\SetUp\Documents\C_book.txt")
#dded r for the unicode error
 
# added a read mode 
file_r = open(r"C:\Users\SetUp\Documents\C_book.txt","r")
file_r.mode
file_r.close()

##Reading modes ,readline()read and place the cursor on the current so, when run again it goes to the next!

file_o = open(r"C:\Users\SetUp\Documents\C_book.txt")
curr_read = file_o.readlines() #.readline reads  the current and CAn be 
#reset with .seek(0) method
#append using file.write(your new content)

#other method for opening file without writting the .close()
with open(r"C:\Users\SetUp\Documents\C_book.txt","w") as file_with:
    filw = file_with.write("Crack Interview")

#Python-Functions

def myFunction():
    print("Hello new function!!")
myFunction()

#function that calculates:
    
def Multiply(n1,n2):
    answer = n1 * n2
    print("Result of {} times {} is {}".format(n1,n2,answer))

num1 = int(input('input Number1 :'))
num2 = int(input("input Number2 :"))

Multiply(num1, num2)


#Excercise For Tax0Calculator In python
def calcRate(amount,rebate):
    if  amount < 50000:
        tax_rate = (10/100) * amount
        tax_rate = (tax_rate - 500) if rebate else tax_rate
        print('Tax Shows 10% rate, therefoe, Your Tax anually is Calculated to be ${}'.format(tax_rate))
    
    elif amount >=50000 or amount <= 100000:
         tax_rate = (20/100) * amount
         tax_rate = (tax_rate - 500) if rebate else tax_rate
         print('Tax Shows 20% rate, therefoe, Your Tax anually is Calculated to be ${}'.format(tax_rate))
    elif amount >= 100000:
         tax_rate = (30/100) * amount
         tax_rate = (tax_rate - 500) if rebate else tax_rate
         print('Tax Shows 30% rate, therefore, Your Tax anually is Calculated to be ${}'.format(tax_rate))
    

def CheckTaxRate():
    isFemale = False
    print("----------TAX--CALCULATOR----------")
    print("----WIZARD----...........")
    print("Input Your Gender and Salary")
    
    amount = int(input("Input Your Salariy: "))
    gender = str(input('Your Gender: M for male and F for female: '))
    
    if gender.lower() == "f":
        isFemale = True
    calcRate(amount,isFemale)    
    

CheckTaxRate()    


#Global and Local Variable
#Local is defined within a function while Global is general scoped variable def in the body

#Function arguments and parameters
#PARAMETERS ARE THE VARIABLES OF A FUNCTION
#ARGUMENTS ARE THE ACTUAL DATA OF  FUNCTION

#e.g => def Func(parameter1,parameter2): return parameter1 + parameter2
#then call the function Func(argument1,argument2) => Func(2,4)

#required arguments,required args, default args, variable args
#1reduired arguments is normal func args
#number of arg passed must be equal to number of arg expected
#POS arg accept data in same po sequence

#2 DEFault arguments
#Accepts default arguments when not provided
def Func(var_1='Hel',var_2='llo'):
    return var_1 + var_2

Func(2,3)
#So if no argument is specified ot takes the default one in parameter
#Func()

#   3Keyword arguments
#Keys are mappes to the argument
#position does not matter
#follows key-value-pair-protocol

def myName(name,age):
    return print("Details of name is {} and age is {}".format(name, age))

myName(name = "Setup", age=19)
#Mixed : not placing default before the positional argumnet 
#required - default - keyword

#   4 Variable lengthor abitrary arguments:
#  when the min or max argument is unknown and can range from 0 to n 
#basically like spread parameter in javaScript

def Spread(*args):
    print(args)
    #its end data type is of class tuple
    print(type(args))
    
    for elem in args:
        print("{},".format(elem),end='')
        
Spread(3,4,5,6,7,"SetUp")


# Variable length-keyword argument
#two star args
def Keyword(**kwargs):
    print(kwargs)
    #has type of dictionary
Keyword(name = "SetUp",gender = "Male", Country = "Nigeria")

#Mixed arbitrary arguments
def Mixed(required, *args, **kwargs):
    print("required argument is :", required)
    print("Arbitrary argument is :", args)
    print("Keyword argument is :", kwargs)
    
Mixed("Hello",20,29,13,56,19,"lists",name = "school", address = "none")
       
#PASS BY VALUE OR PASS BY REFERENCE
# python uses either pass by reference or pass by value 
# Pass by value reference wtih different memory address either in body or function 
#with same label as in var1 = 'kdd' in each
#PAss by reference uses same in both

# Python uses pass by object reference
#e.g
a = 10
b = 14
print("Address of a", id(a)) 
print("Address of b", id(b)) 
#a and b has same address loction if they have same value
#python create an object for b and it is immutable
#CONCLUSION :
# for mutable it uses pass by reference7
#for immutable it uses pass by values
    
#BUILT IN MAP() FUNCTION JUST LIKE MAP IN JAVASCRIPT
#without using map
def Sqr(lst):
    area = lst ** 2
    return area


new_list = [1,2,3,4]
answ = []
#run a loop to calculate the square
for j in new_list:
    answ.append(Sqr(j))
    
#Using built in map function
#map(function to be applied,the iterable list)

mapped = list(map(Sqr,new_list))    
    

#FILTER FUNCTION
filt_list = [2,3,4,5,10,39,20]

numList = []
def Filter(filt):    
    return filt > 8

for num in filt_list:    
    numList.append(Filter(num))

#on-a-go-line
filtered_list = list(filter(Filter, filt_list))

#for a zero list or empty list
non_list = ["a","c","",0,3,5," "]
list_non = list(filter(None, non_list))
#code above filters out a zero element in a list or empty in a list

#LAMBDA FUNCTIONS also Anonymous functions
#lamda arguments: expression
a = lambda side: side ** 2
print(a(4))

#using lamda  function for shortand map
lam = [2,3,4,5,6]

#using lamda for mapping
mapp = list(map(lambda width: width ** 3,lam))
#clean and short!!

#using lamda for filtering lists
fl_lam = [10,20,30,40,20,11]

filtered = list(filter(lambda high: high > 20, fl_lam))

#lamda for sort using 2d list

two_d = [["Ibrahim",80,"A"],
         ["Quyyum",74,"A"],
         ["Lateef",68,"B"],
         ["All",60,"B"]]

#two_d.sort()

## Sorting by the item key using normal function
def Sorted(li):
    ke_y = li[1]
    return ke_y

two_d.sort(key = Sorted)

## Sorting by the item key using normal function reverse order
def Sorted(li):
    ke_y = li[1]
    return ke_y

two_d.sort(key = Sorted, reverse = True)

#USing lamda  shortand sort

two_d.sort(key = lambda item : item[1])

#        -----      PYTHON OOP(OBJECT-ORIENTED-PROGRAMMING)
# object cosist of
# properties : 
#methods : the func of props
#Classes: is like a class or blueprints of the object or attributes
#using the classes we can create multiple INSTANCE of the object


#ABSTRACTION: THIS IS THE FACILITY TO DEFINE OBJECT "ACTORS" THAT CAN
#perform work
#report on and cange their state
#communicate with other objects in system


#ENCAPSULATION: THIS IS SECURING DATA IN A CLASS FOR SECURITY PURPOSE(encapsule)
#avoid unauthorized


#INHERITANCE: THIS SIMPLY IMPROVES CODE REUSABILITY, ABILITY TO INHERIT METHODS FROM #PARENT OBJECT

#POLYMORPHISM: MEANS MORE THAN ONE FORM,IT MAKES WRITIIN AND IMPLEMENTING CODE FASTER
#A METHOD CAN BE IN MORE THAN ONE FORM


class Student:
   #class attributes or static
    country = "NIGERIA"
    
    #create attributes for the methods using init keyword in python
    def __init__(self,fname,lname,gender,age,admin_no):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.age = age
        self.admin_no = admin_no
    
    def New(self):
        print("Class Students OOP",self.lname,self.country)

s1 = Student("SetUp","Ibrahim","Male",14,236586)

s1.New()

s2 = Student("Ibrahim", "Adebayo", "Male", 14, 236587)
s2.country = "Canada"
s2.New()
#print(s1.fname)
#access object method using the  positional argument of self

#EXCERCISE 1 GET STUDENT DATA FROM THE USER INPUT
#first define the class and methods then use input 

class Student:
    
    #define the objects attribues
    def __init__(self,fname,lname,gender,matric_no):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.matric_no = matric_no


fname = str(input("Enter Your First Name: "))
lname = str(input("Enter Your Last Name: "))
gender = str(input("Enter Your Gender: "))
matric_no = int(input("Enter Your Matric: "))


stu_1 = Student(fname,lname,gender,matric_no)

#excercise one done!


#EXCERCISE 2!!
#using the above create a method to print  all student info
class Student:
    
    #define the objects attribues
    def __init__(self,fname,lname,gender,matric_no):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.matric_no = matric_no
    
    def Print(self):
        print(""" Successfully created here are your details\n
              FirstName: {f}\n
              LastName: {l}\n
              Gender: {g}\n
              Matric: {m}""".format(f=fname, l=lname,g=gender,m=matric_no))


fname = str(input("Enter Your First Name: "))
lname = str(input("Enter Your Last Name: "))
gender = str(input("Enter Your Gender: "))
matric_no = int(input("Enter Your Matric: "))


stu_1 = Student(fname,lname,gender,matric_no)
#print out the details here:
stu_1.Print()
#excercise2 done!


#EXCERCISE 3!!!
#using the above obtain the marks for 3 sujects and print the average

class Student:
    
    #define the objects attribues
    def __init__(self,fname,lname,gender,matric_no):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.matric_no = matric_no
    
    #method to print details
    def Print(self):
        print(""" Successfully created here are your details\n
              FirstName: {f}\n
              LastName: {l}\n
              Gender: {g}\n
              Matric: {m}""".format(f=fname, l=lname,g=gender,m=matric_no))

    #methos for average
    
    def Avg(self,markList):
        average = sum(markList) / len(markList)
        print("Your average mark in your best 3 is: {}".format(round(average,2)))
    
    
    
fname = str(input("Enter Your First Name: "))
lname = str(input("Enter Your Last Name: "))
gender = str(input("Enter Your Gender: "))
matric_no = int(input("Enter Your Matric: "))


stu_1 = Student(fname,lname,gender,matric_no)

marks_arr = []
for i in range(1,4):
    quest = int(input("Enter for Subject {}: ".format(i)))
    marks_arr.append(quest)

#print out the details here:
stu_1.Print()
#perform the method
stu_1.Avg(marks_arr)

#Excercise 3 done!!

#EXCERCISE 4!!
#Accept marks for 7 different subjects and calculate their average

class Student:
    
    #define the objects attribues
    def __init__(self,fname,lname,gender,matric_no):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.matric_no = matric_no
    
    #method to print details
    def Print(self):
        print(""" Successfully created here are your details\n
              FirstName: {f}\n
              LastName: {l}\n
              Gender: {g}\n
              Matric: {m}""".format(f=fname, l=lname,g=gender,m=matric_no))

    #methos for average
    
    def Avg(self,markList):
        average = sum(markList) / len(markList)
        print("Your average mark in your best 3 is: {}".format(round(average,2)))
    
    #method to calculate average of 7 subjects
    
    def Sev_avg(self,res_li):
        average = sum(res_li) / len(res_li)
        print("Your average mark is: {}".format(round(average,2)))
    
fname = str(input("Enter Your First Name: "))
lname = str(input("Enter Your Last Name: "))
gender = str(input("Enter Your Gender: "))
matric_no = int(input("Enter Your Matric: "))

#for object attributes call
stu_1 = Student(fname,lname,gender,matric_no)

#for three subjects average
marks_arr = []
for i in range(1,4):
    quest = int(input("Enter for Subject {}: ".format(i)))
    marks_arr.append(quest)



#CREATE-FO-7-SUBJECTS
subject_arr = ["MTH 111","MTH 121","CSC 101","STA 114","STA 115",
               "PHY 102","GES 107"]
#run a loop 7 times to accept scores for each particular subject
result_list = []
for i in range(0,7):
    results = int(input("Enter Your Score for {}: ".format(subject_arr[i])))
    result_list.append(results)


#CALL ALL
stu_1.Print()
stu_1.Avg(marks_arr)
stu_1.Sev_avg(result_list)

#EXCERCISE 4 Done!!!

#Instances
#Getters(accessors) and setters(mutators)

class Stu:
    def __init__(self):
        self.fname = "pythhon"
        self.lname = "Programming"


    #getters method for lname
    def get_ln(self):
        return self.lname
    
    #setters method for fname
    def set_fn(self,val):
        self.fname = val

student = Stu()
#getters
print(student.get_ln())

#setters
student.set_fn("Python!")
#print(student.fname)


#Class method and Static Methods
#class methods 

class Stu:
    
    #class attribute
    club = "BARCELONA"
    
    def __init__(self):
        self.fname = "pythhon"
        self.lname = "Programming"


    #getters method for lname

    def get_ln(self):
        return self.lname
    
    #setters method for fname
    def set_fn(self,val):
        self.fname = val
        
        
    #define a method to call getters of a class attribute or static 
    #treat as a class method
    @classmethod
    def get_club(cls):
        return cls.club
    
    #for statics 
    @staticmethod
    def sta_cl(mark):
        return mark > 60

pupil = Stu()
#pupil.club
#calling class method as getters and setters
#same for setters instance
Stu.get_club()


# static uses @stticmethod with no cls or self argument
#cant modify class attributes and ovject attributes
mark = 77
Stu.sta_cl(mark)


#INHERITANCE METHODS EXAMPLE OOP
class University:
    def __init__(self,uname):
        self.uname = uname
        
    def get_uname(self):
        print("university method")
        #return self.uname
        
#Student can inherit all methods from the university using(oop inheritance) class coz 
#A student belongs to the university
class Student(University):
    def __init__(self,sname):
        self.sname = sname
            
    def get_sname(self):
        print("Student Mehod")
        #return self.sname    

uname = "University Of Ibadan"
sname = "Ibrahim"

un = University(uname)
sn = Student(sname)

un.get_uname()




#INHERITANCE MULTILEVEL INHERITANCE
#grand-parent-class
class University:
    def __init__(self,uname):
        self.uname = uname
        
    def get_uname(self):
        print("university method")
        #return self.uname


#A Campus belongs to a university
#parent
class Campus(University):
    def __init__(self,cname):
        self.cname = cname
        
    def get_cname(self):
        print("Campus Method")

#A student belongs to a campus
#children
class Student(Campus):
    def __init__(self,sname):
        self.sname = sname
            
    def get_sname(self):
        print("Student Mehod")
        #return self.sname   

uni2name = "University Of Ibadan"
cname = "Computer Science"
sname2 = "Ibrahim"


uni2 = University(uni2name)
campus = Campus(cname)
stud = Student(sname2) 

#student now has access to the campus and university method
stud.get_uname()
stud.get_cname()
#and also campus has access to the uni method
campus.get_uname()
#period...................