"""
===================   TASK 3   ====================
* Name:  Roulette
*
* Write a script that will simulate casino game -
* Roulette but only for red, black or green (zero)
* fields. On each run, the script should return
* 'red', 'black' or '0'.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
===================================================
"""
import random

palo_na_broj = random.randrange(0,37)

if palo_na_broj == 0:
    print('0')

elif palo_na_broj in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
    print('red')

else:
    print('black')


import random
bacanje = random.random() #daje nam broj u opsegu od 0 do 1


if bacanje <= 18/37:   
    print('red')       

elif bacanje <= 2*(18/37):  
    print('black')          

else:
    print('0')