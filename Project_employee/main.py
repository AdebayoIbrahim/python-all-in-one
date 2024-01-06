# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:56:22 2024

@author: SetUp
"""
from Classes.employee import Employee
from Utils.Converter import str_date
from Utils.bus_rules import Calc_bonus

#new_employee = Employee("Anonymous", "UG-001", "20150314",5000.0)


#input file read mode
#output file write mode

inp_data = open(r"C:\Users\SetUp\Documents\Project_employee\input\data.txt")
proc_data = open(r"C:\Users\SetUp\Documents\Project_employee\output\processed.txt","w")

#loop through the list and seperate the data and process it

for datas in inp_data:
    name,reg_no,JOD,email,salary = datas.split(sep = ",")
    new_employee = Employee(name, reg_no, JOD,int(salary))
    
    #method to calculate bonus
    JOD = str_date(JOD)
    print(JOD)

    #method to check for customer bonus eligibiltiy
    
    new_Calc = Calc_bonus(JOD)
    print(datas,new_Calc)
    
    #set bonus calling the set method
    new_employee.set_bonus(new_Calc)
    
    
    proc_data.write(str(new_employee))
    #now lets convert the str using operator overide by defining d method

proc_data.close()
#inp_data.close()









