

# QUESTION :

# WRITE A RECURSIVE FUNCTION TO COMPUTE FACTORIAL(N) FOR N > = O.
# USE CORRECT BASE CASE 0! = 1. IF N IS NEGATIVE , PRINT INVALID.


# ANSWER :

def factorial(n):
    if n<0:
        return "Invalid !!"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter any number :"))
print(factorial(n))


# QUESTION :

# GIVEN AN ARRAY OF INTEGERS, COUNT HOW MANY NUMBERS ARE EVEN AND HOW MANY ARE ODD.
# RETURN THE COUNT OF EVEN NUMBERS FOLLOWED BY THE COUNT OF ODD NUMBERS.


# ANSWER :

