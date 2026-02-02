
# QUESTION : FIND THE SUM OF ALL THE DIGITS IN A NUMBER 

# SOLUTION :

# 1. MATHEMATICAL APPROACH :

n=int(input("Enter any number :"))
if len(str(n))==1:
    print(n)
else:
    temp=n
    sum=0
    while temp>0:
        sum+=temp%10
        temp=temp//10
    print("Sum of all the digits of the number is :",sum)


# 2. SECOND APPROACH :

def sum_digit(m):
    if len(str(m))==1:
        return m
    else:
        s=0
        str_m=str(m)
        len_m=len(str_m)
        for i in range(len_m):
            s+=int(str(str_m[i]))
        return s
    
m = int(input("Enter any number :"))
print(sum_digit(m))