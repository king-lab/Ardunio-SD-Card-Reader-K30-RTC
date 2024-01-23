#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 15:23:20 2024
Analysis of CO2 out put iof two days on the same 24 hour graph
****** looped through for different days, NOT GOOD, time stamp might be better orgaized by day. ********** 
@author: merondibia
"""
#import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
#import pandas as pd
#import random

#open file from the right directory
f1 = open("/Users/merondibia/Desktop/Rutgers/Research/Fungi CO2 mearments/Data/111856.txt", "r")
mainstring = f1.read() # assign the info into a string variable 
#print(mainstring)
my_list1 = mainstring.split("\n") # break up each line of the string and make it a list 

f2 = open("/Users/merondibia/Desktop/Rutgers/Research/Fungi CO2 mearments/Data/121825.txt", "r")
mainstring = f2.read() # assign the info into a string variable 
#print(mainstring)
my_list2 = mainstring.split("\n") # break up each line of the string and make it a list 

def processCO2datafromrawfile(datastringlist):
    
    TimeStamp =[] # initalize list for datetime class
    CO2ppm = [] #initalize list for CO2 concentration in part per million
    for i in range(len(datastringlist)): # go through each line in the data file
        n = datastringlist[i].split("\t") # split each entry of data into a list
        if len(n) == 6:# check this is the line with full data set 
            if float(n[5])>=0: # check if the CO2 gave a positive/valid reading
                CO2ppm.append(float(n[5])) # add CO2 concentration value to the CO2 list
                #dt_str = n[2]+"/"+n[1]+"/"+n[0]+" "+ n[3]+":"+n[4]+":00" # rearreange date and time in a format that datetime.strptime function can interpret
                dt_str = "01/01/2000 "+ n[3]+":"+n[4]+":00"
                dt_obj = datetime.strptime(dt_str, '%d/%m/%Y %H:%M:%S') # interpret the rearranged string data into datetime class list using function
                #print(type(dt_obj))
                TimeStamp.append(str(dt_obj))#put the formated datetime class in a list OF FREAKING STRING, I WANTED DATETIME ???
    return TimeStamp,CO2ppm

test_str = processCO2datafromrawfile(my_list1)[0][0]
#test_timeobj = test_str.time()
#print(test_timeobj)


x1 = processCO2datafromrawfile(my_list1)[0] # set time and date as x axis
xs1 = matplotlib.dates.date2num(x1) # convert datetime string into numbers for the plot
y1 = processCO2datafromrawfile(my_list1)[1] # set CO2 ppm measurement as y axis

x2 = processCO2datafromrawfile(my_list2)[0] # set time and date as x axis
xs2 = matplotlib.dates.date2num(x2) # convert datetime string into numbers for the plot
y2 = processCO2datafromrawfile(my_list2)[1] # set CO2 ppm measurement as y axis

hfmt = matplotlib.dates.DateFormatter('%H:%M:%S') # axis label time stamp formating

#fig = plt.figure()
#ax = fig.add_subplot(1,1,1)
plt.figure().add_subplot(1,1,1).xaxis.set_major_formatter(hfmt)
#plt.setp(ax.get_xticklabels())
plt.xticks(rotation=45)
plt.scatter(xs1, y1, s=0.5, label="With Motor OFF")
plt.scatter(xs2, y2, s=0.5, label="With Motor ON")
plt.yticks(np.arange(0,150,10))
plt.legend()
plt.title("CO2 ppm with the motor on and off")
plt.xlabel("Time") #label x axis
plt.ylabel("CO2 ppm") # label y axis
plt.show()


# print(x[1])
# timearray = np.arange('2000-01-01', '2000-01-02',np.timedelta64(1,'h'), dtype='datetime64')
# randomlist = []
# for i in range(0,24):
#     n = random.randint(1,30)
#     randomlist.append(n)
    
# start_dt = datetime(2022, 6, 10)
# end_dt = datetime(2022, 6, 15)

# # difference between current and previous date
# delta = timedelta(days=1)

# # store the dates between two dates in a list
# dates = []

# while start_dt <= end_dt:
#     # add current date to list by converting  it to iso format
#     dates.append(start_dt.isoformat())
#     # increment start date by timedelta
#     start_dt += delta

# print('Dates between', start_dt, 'and', end_dt)
# print(dates)

# plt.scatter(timearray,randomlist)
#plt.xticks(rotation=45)
#plt.yticks(np.arange(0,150,10))
# plt.locator_params(axis='x', nbins=24)
# print(np.arange(x[0],x[200],timedelta(hours=1)))

# plt.scatter(x,y,s=0.5) # plot data
# plt.xlabel("Date and Time") #label x axis
# plt.ylabel("CO2 ppm") # label y axis
# plt.xticks(rotation=45)

# plt.show()

# plt.yticks(np.arange(0,150,10 ))
# plt.show(block=False)
# TimeStamp =[] # initalize list for datetime class
# year = [] #initalize list for year
# month = [] #initalize list for month
# date = [] #initalize list for date
# hour = [] #initalize list for hour
# minute = [] #initalize list for minute
# CO2ppm = [] #initalize list for CO2 concentration in part per million
# for i in range(len(my_list)): # go through each line in the data file
#     n = my_list[i].split("\t") # split each entry of data into a list
#     if len(n) == 6:# check this is the line with full data set 
#         if float(n[5])>=0: # check if the CO2 gave a positive/valid reading
#             # print(float(n[5])>=0)
#             # year.append(n[0])# add year value to the year list
#             # month.append(n[1]) # add month value to the month list
#             # date.append(n[2]) # add date value to the date list
#             # hour.append(n[3]) # add hour value to the hour list
#             # minute.append(n[4]) # add minute value to the minute list
#             CO2ppm.append(float(n[5])) # add CO2 concentration value to the CO2 list
#             dt_str = n[2]+"/"+n[1]+"/"+n[0]+" "+ n[3]+":"+n[4]+":00" # rearreange date and time in a format that datetime.strptime function can interpret
#             dt_obj = datetime.strptime(dt_str, '%d/%m/%Y %H:%M:%S') # interpret the rearranged string data into datetime class list using function
#             TimeStamp.append(str(dt_obj.time())) #put the formated datetime class in a list  
        
# get the second, it matters
"""
for i in range(len(my_list)): # put the time form the data in a time class list
    n = my_list[i].split("\t") # split each entry of data into a list
    if len(n) == 6: # check this is the line with full data set 
        if float(n[5])>=0: # check if the CO2 gave a positive/valid reading
            dt_str = date[i]+"/"+month[i]+"/"+year[i]+" "+ hour[i]+":"+minute[i]+":00" # rearreange date and time in a format that datetime.strptime function can interpret
            dt_obj = datetime.strptime(dt_str, '%d/%m/%Y %H:%M:%S') # interpret the rearranged string data into datetime class list using function
            #print(dt_obj)
            TimeStamp.append(dt_obj) #put in ina list  
"""

# x = TimeStamp # set time and date as x axis
# y = CO2ppm # set CO2 ppm measurement as y axis
# plt.scatter(x,y,s=0.5) # plot data
# plt.xlabel("Date and Time") #label x axis
# plt.ylabel("CO2 ppm") # label y axis
# #plt.xaxis.set_major_locator(plt.dates.HourLocator())
# #plt.xaxis.set_major_formatter(plt.dates.DateFormatter('%H'))
# plt.xticks(rotation=45)

# plt.yticks(np.arange(0,150,10 ))
# plt.show(block=False)
#print(a)
