#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:12:37 2020

@author: user
"""


total_cost=1000000
epsilon=100
increment=0.01
annual_salary=float(input('Enter your annual salary'))
portion_saved=0
semi_annual_rise=0.07
portion_down_payment=0.25
set_time=36
current_savings=0
r=0.04
monthly_return=current_savings*r/12
monthly_salary=annual_salary/12
monthly_saved=monthly_salary*portion_saved
number_of_month=36
total_saved=monthly_saved*number_of_month
while (total_saved - (total_cost*portion_down_payment))<=epsilon:
    portion_saved+=increment  
    monthly_saved=monthly_salary*portion_saved
    current_savings=current_savings+total_saved
    monthly_return=current_savings*r/12
    total_saved=monthly_saved*number_of_month+monthly_return

print('Saving portion',portion_saved,'per month')


    




