# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:41:49 2024

@author: SetUp
"""
from datetime import date


#here is a module to convert string obtained from employee to date

def str_date(date_str):
    #collect the raw date as arguent and process it
    #i.e = 20220428
    years = int(date_str[0:4])
    month = int(date_str[4:6])
    days = int(date_str[6:8])
    #from datetime library
    date_converted = date(years,month,days)
    return date_converted