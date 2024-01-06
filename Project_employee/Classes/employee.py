# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:57:52 2024

@author: SetUp
"""


class Employee:
    def __init__(self,name,reg_no,JOD,salary,bonus = 0.0):
        self.name = name
        self.reg_no = reg_no
        self.JOD = JOD
        self.bonus = bonus
        self.salary = salary

    #getters for bonus/salary
    def get_bonus(self):
        return self.bonus
    
    
    #setters for bonus
    def set_bonus(self,bonus):
         self.bonus = bonus
         
    #define str method to convert to a real string
    def __str__(self):
        string = self.name + '\n'
        return string


        