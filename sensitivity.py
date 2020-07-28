# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:09:58 2020

@author: YingliLou
"""
import numpy as np
import csv

climate = ['1A','2A','2B','3A','3B','3C','4A','4B','4C','5A','5B','6A','6B','7A','8A']
sensitivity=['fa','mo','SA_GAM_','SA_LIN_REG_','SA_RP_REG_','SA_RS_REG_','so']
num_var=11

sensitivity_results=[]
for i in range (len(climate)): #len(climate)
    results1=[]
    results2=[]
    for j in range (len(sensitivity)): #len(sensitivity)
        data_set_temp = np.genfromtxt('./results/sensitive/sensitivity_'+sensitivity[j]+'.csv',dtype=str,delimiter=',')
        var=[None]*num_var
        temp=[]
        for row in data_set_temp:
            if row[0] == climate[i]:
                temp.append(row[3])
        sensitive_value=1
        temp=np.array(temp)
        temp=np.argsort(temp)
        value=1
        for k in range(num_var):
            var[temp[k]]=value
            value +=1
        results1.append(var)
    for j in range (num_var):
        temp=0
        for k in range(len(sensitivity)):
            temp += float(results1[k][j])
        temp=temp/len(sensitivity)
        results2.append(temp)
    sensitivity_results.append(results2)
    
sensitivity_results=tuple(zip(*sensitivity_results))
    
with open('./sensitivity_results.csv', 'wb') as csvfile:
    for row in sensitivity_results:
        data = csv.writer(csvfile, delimiter=',')
        data.writerow(row)
        
            
        
    
        
    
                
                