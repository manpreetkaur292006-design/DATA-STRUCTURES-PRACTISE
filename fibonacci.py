
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

print()

# WRITING THE SAME CODE USING THE LOOP
n=0
m=1
t=int(input("Enter the number of terms:"))
s=0
print(n,m,end=" ")
for i in range(t-2):
    s=m+n
    print(s,end=" ")
    n=m
    m=s

