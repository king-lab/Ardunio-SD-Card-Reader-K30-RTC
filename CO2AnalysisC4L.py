#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 18:55:18 2024

@author: merondibia
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime

#open file from the right directory
f1 = open("/Users/merondibia/Desktop/Rutgers/Research/Fungi CO2 mearments/Data/111856.txt", "r")
mainstring = f1.read() # assign the info into a string variable 
my_list1 = mainstring.split("\n") # break up each line of the string and make it a list 


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

x1 = processCO2datafromrawfile(my_list1)[0] # set time and date as x axis
xs1 = matplotlib.dates.date2num(x1) # convert datetime string into numbers for the plot
y1 = processCO2datafromrawfile(my_list1)[1] # set CO2 ppm measurement as y axis

hfmt = matplotlib.dates.DateFormatter('%H:%M:%S') # axis label time stamp formating, THIS CREATE A LOOPING ARTIFACT THAT MAY NEED TO BE FIXED

plt.figure().add_subplot(1,1,1).xaxis.set_major_formatter(hfmt)

plt.xticks(rotation=0)
plt.scatter(xs1, y1, s=0.5, label="With Motor OFF")

plt.yticks(np.arange(0,150,10))
plt.legend()
plt.title("CO2 ppm in a 24 hour cycle")
plt.xlabel("Time") #label x axis
plt.ylabel("CO2 ppm") # label y axis
plt.show()
