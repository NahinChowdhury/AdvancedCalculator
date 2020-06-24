import math

print('8,'*14  + '9,'*8 + '10,'*28 + '11,'*15  + '12,'*20)

# make a SD calculator
# take in inputs as numbers divided by commas
# make a function which retruns the number of inputs (len(smth))
# make another function that add all values and returns value
# make another function that calculates mean and returns its value


"""
numbers = input("Insert the numbers you want the mean of: ")
stringNumberList = numbers.split(',')
numberList = list()



for i in stringNumberList:
    numberList.append(int(i))
"""


# run a while loop which ends when user inputs '.' as their input
# ask them what their digit is. after that, ask them how many times the value occurs (cannot be 0 for now)
# after gathering the digit and the iterations, run a for loop which will insert the digit into a list


def takeInputs():
    cont = True
    numberList = list()
    print("Please enter the chosen digits and their frequencies below. If you want to stop entering any more digits, please enter a fullstop anytime, anywhere.\n")
    
    while(cont == True):
        digit = input("Enter a digit from your population: ")
        if '.' in digit:
            break
            
        iterations = input("Enter the frequency of the digit: ")
        if '.' in iterations:
            break
            
        for i in range(0,int(iterations)):
            numberList.append(int(digit))
            
        
        print(" ")
    return numberList    
    

def choice():
    
    print("What are you trying to find?")
    print("1- Mean")
    print("2- Variance")
    print("3- Standard Deviation")
    print("Please enter number assigned to what you are looking for.")
    print(" ")
    
    choice = input("Choice: ")
    
    print("")
    return int(choice[0])
    



def count(numberList):
    return len(numberList)

def sumValue(numberList):
    return sum(numberList)


def mean(numberList):
    return sumValue(numberList)/count(numberList)

def differences(numberList):
    # subtract mean(numberlist) from each element in numberList
    # and append to a new list 
    # return the new list
    
    differencesList = list()
    
    for i in numberList:
        
        differencesList.append(i - mean(numberList))
    
    return differencesList
    
#differencesList = differences(numberList)

def differencesSquared(numberList):
    differencesList = differences(numberList)
    differencesSquaredList = list()
    
    for i in differencesList:
        differencesSquaredList.append(i**2)
    
    return differencesSquaredList
   
    
#differencesSquaredList = differencesSquared(differencesList)


def sumOfDifferencesSquared(numberList):
    
    differencesSquaredList = differencesSquared(numberList)
    return sum(differencesSquaredList)

def variance(numberList):
    return sumOfDifferencesSquared(numberList)/count(numberList)
    
#variance = variance(differencesSquaredList,numberList)

def standardDeviation(numberList):
    variance1 = variance(numberList)
    return math.sqrt(variance1)
    
    
#print("The standard deviation is "+ str(standardDeviation(variance)) + "." )



def main():
    
    numberList = takeInputs()
    want = choice()
    
    if want == 1:
        print("The mean is "+ str(mean(numberList)) + ".")
    
    elif want == 2:
        #differencesList = differences(numberList)
        #differencesSquaredList = differencesSquared(numberList)
        variance1 = variance(numberList)
        print("The variance is " + str(variance1) + ".")
        
    elif want == 3:
        #differencesList = differences(numberList)
        #differencesSquaredList = differencesSquared(numberList)
        #variance1 = variance(numberList)
        standardDeviation1 = standardDeviation(numberList)
        print("The standard deviation is " + str(standardDeviation1) + ".")        
        
    else:
        print("We do not provide what you are looking for. Please restart the program and try again.")
        
        
        
main()