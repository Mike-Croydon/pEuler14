#This program solves Project Euler problem 10, determining the longest Collatz sequence for the first 1,000,000 numbers
number = 1
maxnumber = 1
maxterms = 1
cache = []
cache.append(0)
#Simple loop checks every number and iterates through the sequence. Checks if the number of terms is greater than the previous max and stores it
#Implemented caching of number of terms for every number. 
while(number <= 1000000):
    ncopy = number
    numterms = 1
    #print(number) commented this out because it was taking substantial time
    while(ncopy != 1):
        #checks to see if the sequence has reached a number below it's start and if so it simply consults the cached number of terms
        if(ncopy < number):
            numterms = numterms - 1 + cache[int(ncopy)]
            break
        if(ncopy % 2 == 0):
            ncopy = ncopy / 2
        else :
            ncopy = (ncopy*3) + 1
        numterms += 1
    cache.append(numterms)
    if (numterms > maxterms):
        maxterms = numterms
        maxnumber = number
    number += 1

print ("The max number of terms is ", maxterms, "and the first term is", maxnumber)