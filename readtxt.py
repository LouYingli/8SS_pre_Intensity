# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 17:36:22 2020

@author: yunyangye
"""
import csv

climate = ['1A','2A','2B','3A','3B','3C','4A','4B','4C','5A','5B','6A','6B','7A','8A']
variable = ['V3','V4','V5','V6','V7','V8','V9','V10','V11','V12','V13']

SA=['SA_GAM_','SA_LIN_REG_','SA_RP_REG_','SA_RS_REG_']
for i in range(len(SA)):
    if SA[i] != 'SA_LIN_REG_':
        sensitivity = []
        for j in range(len(climate)):
            f = open('./results/sensitive/'+SA[i]+climate[j]+'.txt','rb')
            lines=f.readlines()
            f.close()
            start_id = 0
            for k in range(len(lines)):
                if 'Input' in lines[k]:
                    start_id = k+1
            for k in range(len(variable)):
                temp = []
                temp.append(climate[j])
                temp.append(variable[k])
                for l in range(start_id,len(lines)):
                    if lines[l].split('	')[0] == variable[k]:
                        temp.append(lines[l].split('	')[1])
                        temp.append(lines[l].split('	')[1])
                        temp.append(lines[l].split('	')[1])
                if len(temp) == 2:
                     temp.append(0)
                     temp.append(0)
                     temp.append(0)
                sensitivity.append(temp)
        with open('./results/sensitive/sensitivity_'+SA[i]+'.csv', 'wb') as csvfile:
             for row in sensitivity:
                data = csv.writer(csvfile, delimiter=',')
                data.writerow(row)
    if SA[i] == 'SA_LIN_REG_':
        sensitivity = []
        for j in range(len(climate)):
            f = open('./results/sensitive/'+SA[i]+climate[j]+'.txt','rb')
            lines=f.readlines()
            f.close()
            start_id = 0
            for k in range(len(lines)):
                if 'Input' in lines[k]:
                    start_id = k+1
            for k in range(len(variable)):
                temp = []
                temp.append(climate[j])
                temp.append(variable[k])
                for l in range(start_id,len(lines)):
                    if lines[l].split('	')[0] == variable[k]:
                        temp.append(lines[l].split('	')[2])
                        temp.append(lines[l].split('	')[2])
                        temp.append(lines[l].split('	')[2])
                if len(temp) == 2:
                     temp.append(0)
                     temp.append(0)
                     temp.append(0)
                sensitivity.append(temp)
        with open('./results/sensitive/sensitivity_'+SA[i]+'.csv', 'wb') as csvfile:
             for row in sensitivity:
                data = csv.writer(csvfile, delimiter=',')
                data.writerow(row)
