#This program solves Project Euler problem 10, determining the longest Collatz sequence for the first 1,000,000 numbers
number = 1
maxnumber = 1
maxterms = 1

#Simple loop checks every number and iterates through the sequence. Checks if the number of terms is greater than the previous max and stores it
while(number <= 1000000):
    ncopy = number
    numterms = 1
    print(number)
    while(ncopy != 1):
        if(ncopy % 2 == 0):
            ncopy = ncopy / 2
        else :
            ncopy = (ncopy*3) + 1
        numterms += 1
    if (numterms > maxterms):
        maxterms = numterms
        maxnumber = number
    number += 1

print ("The max number of terms is ", maxterms, "and the first term is", maxnumber)