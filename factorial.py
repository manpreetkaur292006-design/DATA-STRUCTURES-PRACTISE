
# FACTORIAL OF A NUMBER - RECURSSIVE APPROACH

def factorial(n):

    if n==0 or n==1:   # BASE CASE
        return n
    
    else:  # RECURSSION
        return n*factorial(n-1)
    
n=int(input("Enter any number :"))  # TAKING AN INTEGER AS AN INPUT FROM THE USER

print("Factorial :")
print(factorial(n))  # CALLING THE FUNCTION AND PRINTING ITS VALUE