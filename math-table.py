
# MULTIPLICATION TABLE :

# write a program that takes a positive interger n as an input 
# and prints its multiplication table from 1 to 10. format each line
# as "n x i = product" .

n=int(input("Enter any number :"))
print(f"Table of {n}")
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

