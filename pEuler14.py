
number = 1
maxnumber = 1
maxterms = 1

while(number < 1000000):
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

print ("The max number of terms is ", maxterms, "and the first term is", maxnumber)