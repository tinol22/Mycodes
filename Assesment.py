# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:42:08 2020

@author: lab2-15
"""
Songs=['Chak de india','Aashiqi','mere mehboob','Malang']
print('Before Sorting')
print(Songs)
print('length of songs:',end=' ')
for i in Songs:
    print(len(i),end=' ')
    
i=Songs.index('Chak de india')
i=i+1
print('\nIndex of Song:',Songs.index('Chak de india')+1)

print('\n')

Songs.sort(key=len)
print('After sorting:',Songs)
for i in Songs:
    print(len(i),end=' ')
   

print('\nthe Index of Song:',Songs.index('Chak de india')+1)
