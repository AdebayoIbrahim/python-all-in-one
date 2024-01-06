# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:43:16 2024

@author: SetUp
"""
#try accessing the get_details funcion from info.py

#method-1
from Customer import info

info.get_details("Ibrahim")
#the fall-back here is that we have to call info.function() every time 
#we try accessing the function

#method-2
from Customer.info import get_details

get_details("SetUp")

#method 3
#using alias

from Customer.info import get_details as greet
greet("All")


#Method 4 its not recomended importing all func from info directly
#from Customer.info import *
#will import all function from info 
#not the best practice though

#from Customer import *
#will import all modules from customer 
#not the best practice though