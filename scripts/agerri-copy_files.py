import os

arr = [1, 2, 6, 7, 8, 9, 10, 11, 12]

for i in arr: 
    os.system('cp result{0}.properties result{0}-400k.properties'.format(i))