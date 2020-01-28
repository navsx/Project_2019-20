
#Header  Files
import os
import time

print('Enter your name:')
name = input()

os.system('cls')
print('Hello, ' + name)
print('\n\n\t\t\t\tINSTRUCTIONS\n')
print('There will be some sentences displayed on your screen, you\'ll have to type those\n')


start = time.time()

total_missing_characters=0

f = open('read.txt')
oneLine = f.readline()

while(oneLine!=''):
    os.system('cls')
    print('\n\n\t\t\t\tRead the lines and type\n\n')
    

    oneLine=oneLine[:-1]    
    print(oneLine)
    line = input()
        
    
    if(len(oneLine)!=len(line)):
        print("not full line")
        print("{} missing characters".format(len(oneLine)-len(line)))
        total_missing_characters+=(len(oneLine)-len(line))
    else:
        print('full line')
            
            
    total_mistakes=0
    mistakes=0
    i = 0
    while(i<len(line)):
        if(line[i]!=oneLine[i]):
            mistakes+=1
        i+=1   
    print("mistakes", mistakes)    
    oneLine = f.readline() 


        
end = time.time()
elapsed = end - start
total_mistakes+=mistakes
print("Total Mistakes : ",total_mistakes)
print("Total Missing Characters : ",total_missing_characters)
print("Total Time Taken",elapsed)