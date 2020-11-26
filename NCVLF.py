# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 22:03:05 2020

@author: Admin
"""

list2 = [({'name':'Peter','age':2},{'name':'John','age':21}),({'name':'Mary','age':2},{'name':'Trandanpro','age':21}),({'name':'Nam','age':2},{'name':'Hung','age':21}),({'name':'Mai','age':2},{'name':'loan','age':21})]

for index ,item in enumerate(list2,1):
    print(index,'=',item)
    for i in item:
        print(i)
        print('name:',i['name'])
        print('age:',i['age'])
        
    
    
    
   
    
    