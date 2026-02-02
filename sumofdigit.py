

# QUESTION : FIND THE SUM OF ALL THE DIGITS IN A NUMBER 


# SOLUTION :


# 1. MATHEMATICAL APPROACH :


n=int(input("Enter any number :"))  # TAKING INPUT FROM THE USER

if len(str(n))==1:  # HANDLING THE SINGLE DIGIT INPUT
    print(n)

else:   # ELSE CALCULATING THE SUM
    temp=n  # CREATING A COPY OF N
    sum=0

    while temp>0:  # RUNNING WHILE LOOP 
        sum+=temp%10  # ADDING THE REMAINDER OF %10 TO SUM TO GET THE OUTPUT
        temp=temp//10  # TRUNCATING THE DECIMALS BY CALCULATING THE FLOOR DIVISION

    print("Sum of all the digits of the number is :",sum)  # PRINTING THE SUM



# 2. SECOND APPROACH :


def sum_digit(m):  # DECLARING A FUNCTION

    if len(str(m))==1:  # HANDLING THE SINGLE DIGIT
        return m 
    
    else:  # ELSE CALCULATING THE SUM
        s=0  
        str_m=str(m) 
        len_m=len(str_m)  # CALCUATING THE NUMBER OF DIGITS IN THE INPUTTED NUMBER

        for i in range(len_m):  # RUNNING THE LOOP TILL THE LENGTH OF THE NUMBER
            s+=int(str(str_m[i]))  # ADDING THE SINGLE DIGIT TO THE VARIABLE S
        return s
    
m = int(input("Enter any number :"))   # TAKING AN INPUT FROM THE USER
print(sum_digit(m))  # CALLING THE FUNCTION AND PRINTING IT