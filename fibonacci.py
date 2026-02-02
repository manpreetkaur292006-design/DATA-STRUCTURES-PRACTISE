
# PRINTING THE FIBONNACCI SERIES - RECURSSIVE APPROACH

def fib(n):
    if n<=1:   # BASE CASE
        return n
    else:    # RECURSION
        return fib(n-1)+fib(n-2)
    
terms=int(input("Enter the number of terms :"))  # TAKING THE NUMBER OF TERMS AS AN INPUT FROM THE USER

if terms<=0:   # HANDLING THE NEGATIVE INPUTS
    print("Please enter a positive integer")

else:   # PRINTING THE SERIES USING FOR LOOP
    for i in range(terms):
        print(fib(i),end=" ")

