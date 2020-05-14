#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:12:37 2020

@author: user
"""


total_cost=int(input('Enter the price of your dreamhouse'))
annual_salary=float(input('Enter your annual salary'))
portion_saved=float(input('Enter portion of your monthly salary to be saved'))
portion_down_payment=0.25
current_savings=0
r=0.04
monthly_return=current_savings*r/12
monthly_salary=annual_salary/12
monthly_saved=monthly_salary*portion_saved
number_of_month=1
total_saved=monthly_saved*number_of_month
while total_saved < (total_cost*portion_down_payment):
    current_savings=current_savings+total_saved
    monthly_return=current_savings*r/12
    print(current_savings)
    number_of_month+=1
    total_saved=monthly_saved*number_of_month+monthly_return

print('Saving will take',number_of_month,'month')


    




