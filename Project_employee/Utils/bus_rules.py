# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 12:07:50 2024

@author: SetUp
"""

#this contains function to define rule for bunoses of employees according
#to their date of joinng
#if its 10 yrs or grater bonus is 10000
#if its 5yrs or greater bonus is 5000
#else not eligible for bonus
from datetime import date,timedelta

def Calc_bonus(date_c):
    bonus = 0
    #get todays date
    today = date.today() 
    
    #calculate time delatas
    timestamp  = timedelta(days = 365)
    five_years = timestamp * 5
    ten_years = timestamp * 10
    
    interval = today - date_c
    
    if interval >= ten_years:
        #print(10000)
        bonus = 10000
     
    elif interval >= five_years:
        #print(5000)
        bonus = 5000
        
    else:
        print("Not eligible")
        
        
        
    return bonus    