# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Apr 20 12:53:58 2020

# @author: user
# """
# from ps1_partition import get_partitions
# import time
# import timeit
# cows={}
# with open('ps1_cow_data.txt','r') as file:
#     for row in file:
#         text=row.split(sep=',')
#         cows.update({text[0]:int(text[1].strip('\n'))})
# # print (cows)
# cows_sorted={k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
# # print(cows_sorted)
# # for k,v in cows_sorted:
# #     print(k)
# def greedy_cow_transport(cows,limit=10):
#     """
#     Uses a greedy heuristic to determine an allocation of cows that attempts to
#     minimize the number of spaceship trips needed to transport all the cows. The
#     returned allocation of cows may or may not be optimal.
#     The greedy heuristic should follow the following method:

#     1. As long as the current trip can fit another cow, add the largest cow that will fit
#         to the trip
#     2. Once the trip is full, begin a new trip to transport the remaining cows

#     Does not mutate the given dictionary of cows.

#     Parameters:
#     cows - a dictionary of name (string), weight (int) pairs
#     limit - weight limit of the spaceship (an int)
    
#     Returns:
#     A list of lists, with each inner list containing the names of cows
#     transported on a particular trip and the overall list containing all the
#     trips
#     """
#     cows_sorted={k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
#     trips2=[]
#     total_weight=0
#     for i in range(len(cows_sorted)):
#         trips=[]
#         total_weight=0
#         for k,v in cows_sorted.items():
#             if total_weight+cows_sorted[k]<=limit:
#                 trips.append(k)
#                 total_weight+=cows_sorted[k]
#                 cows_sorted[k]=limit+10
#         if trips!=[]:
#             trips2.append(trips)
                
#     print(trips2)
    
# def brute_force_cow_transport(cows,limit=10):
#     trips2=[]
#     for partition in get_partitions(cows): 
#         trips=[]
#         total_weight=0
#         for i in partition:
#             for k in i:
#                 if k in cows:
#                     total_weight+=cows[k]
                
#             if total_weight<=limit:
#                 trips.append(i)
#             total_weight=0
#         if len(trips)!=len(partition):
#             trips=[]
#         if trips!=[]:
#             trips2.append(trips)

#     trips2.sort(key=len)
#     print(trips2[0])
        
          
# # greedy_cow_transport(cows)
# # brute_force_cow_transport(cows)

# start = time.time() 
# greedy_cow_transport(cows)
# end = time.time() 
# print (end,start)

# x1=10
# x2=5
# x3=1
# x=25
# n=99
# y=n//x
# print(y)
# y2=(n-x*y)//x1
# print(y2)
# y3=(n-x*y-x1*y2)//x2
# print(y3)
# y3=(n-x*y-x1*y2)//x3
# print(y3)

x = (1, 5, 10, 25)
for i in range(len(x) - 1, -1, -1):
    print(x[i])







    
