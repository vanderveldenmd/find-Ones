# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:01:53 2021
This function finds the number of times the number "one" appears in all numbers.
The first part of the function, fastWay does this by finding the number in each place
value. The function will determine this.

lessHundred finds the last 100 digits, since this is simply easier to iterate than
doing the math because there are a number of edge cases which makes this process
more difficult.

These functions are made so that the final part of the code is easier. The final
part we are finding all n such that f(n) (finding number of 1's) = n. The function
adds all n together, finds digits and their sum to prove answers are all the same.

This challenge was taken from r/dailyprogrammer.
@author: vv238
"""
import math

def slowWay(number):
    count = 1
    numOnes = 0
    while count <= number:
        countStr = str(count)
        countList = list(countStr)
        for x in countList:
            if x == "1":
                numOnes += 1
        count += 1
    print(numOnes)

def fastWay(number):
    remain = number
    numOnes = 0
    lastWasOne = 0
    temp_numOnes = 0
    
    
    while remain > 100:
        digits = math.ceil(math.log(remain, 10)) #number of digits in the current number
        numDigit = int(remain / (10 ** (digits - 1))) #this number will determine how many to add overall
        
        #since the math.ceil function doesn't quite work for what I'm doing here, there needs to be an edge
        #case for if it returns 10
        if numDigit == 10:
            digits += 1
            numDigit = 1  
        
        #if there are 3 digits it is 300, 4 digits 4000, 5 digits 50000, etc.
        placeFactor = (digits - 1) * (10 ** (digits - 2) ) # getting the factor of that current digit
        jumpFactor = 10 ** (digits - 1) + (2 * placeFactor) #jumpFactor is 1 added to the front of placeFactor * 2
        
        #we will need to manipulate this number later so we use a temporary variable for storage
        temp_numOnes += placeFactor
        
        # this finds how many the digit will add to the overall count
        if numDigit <= 1:
            temp_numOnes += 1
        elif numDigit == 2:
            temp_numOnes += jumpFactor
            temp_numOnes -= placeFactor
        else:
            temp_numOnes +=jumpFactor
            temp_numOnes += int(placeFactor * (numDigit - 3))
        remain -= numDigit * (10 ** (digits - 1))
        
        #if the last digit was a 1, we need to account for that digit in all the others being counted
        # if lastWasOne == 1:
        #     print("here")
        #     temp_numOnes *= 2
        
        lastWasOne = 0
        
        #this step accounts for the fact that the 1 digit will not count itself otherwise
        if numDigit == 1:
            lastWasOne = 1
            temp_numOnes += remain
        numOnes += temp_numOnes
        temp_numOnes = 0
        
    #once we get here we just go through the last 100 to make it easier
    temp_numOnes += lessHundred(remain)
    numOnes += temp_numOnes
    #print(numOnes)
    return numOnes
    
    
#since the last 100 numbers has too many edge cases, it makes sense to plow through it iteratively
def lessHundred(number):
    count = 1
    numOnes = 0
    while count <= number:
        countStr = str(count)
        countList = list(countStr)
        for x in countList:
            if x == "1":
                numOnes += 1
        count += 1
    return numOnes
    


#howMany = 1111810


    
#slowWay(howMany)
totalOnes = 0
#totalOnes = fastWay(howMany)

totalOnesStr = str(totalOnes)
totalOnesList = list(totalOnesStr)
sumOnes = 0
for x in totalOnesStr:
    sumOnes += int(str(x))

#print(sumOnes)


#This function will find the number of times f(n) = n for the above equation
#It will be skipping a lot of numbers because there are few of these numbers present
count = 0
sumCount = 0
i = 1
factor = 0.01
while i < 5 ** 20:
    method = fastWay(i)
    if (method == i):
        count += i
    elif  i / method > 1:
        i *= (i/method) ** factor
    else:
        i *= (method/i) ** factor
    i = int(i)
    i += 1    
    
print(count)
print("digits:", math.ceil(math.log(count, 10)))
countStr = str(count)
countList = list(countStr)
for x in countList:
    sumCount += int(str(x))
print("sum of digits:", sumCount)




# print(numOnes)
    





