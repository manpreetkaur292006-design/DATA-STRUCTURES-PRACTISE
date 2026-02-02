

# STACK ADT IMPLEMENTATION AND REVERSING THE STRING USING STACK ILLUSTRATION


# 1. USING OOPS CONCEPTS


class StackADT:   # DEFINING THE CLASS 

    def __init__(self):   # DEFINING THE INIT METHOD
        self.data=[] 

    def isEmpty(self):    # DEFINING THE isEmpty METHOD
        return len(self.data)==0
        
    def push(self,n):    # DEFINING THE push METHOD
        return self.data.append(n)    # ADDING THE ELEMENT TO THE STACK
        
    def pop(self):   # DEFINING THE pop METHOD
        if self.isEmpty()==True:   # CHECKING THE STACK UNDERFLOW CONDITION
            return None
        return self.data.pop()   # REMOVING THE TOP ELEMENT FROM THE STACK
        
    def peek(self):  # DEFINING THE PEEK METHOD AND CHECKING THE TOP ELEMENT OF THE STACK
        if self.isEmpty()==True:   # CHECKING THE STACK UNDERFLOW CONDITION
            return None
        return self.data[-1]
    
    def display(self):  # DISPLAYING THE WHOLE STACK BY display METHOD
        return self.data
    
    def size(self):   # DEFINING THE size METHOD AND CALCULATING THE SIZE OF THE STACK
        return len(self.data)
    
def Reverse_string(s):  # DEFINING THE REVERSE STRING METHOD

    s1=StackADT()  # CREATING THE OBJECT OF THE CLASS

    for ch in s:
        s1.push(ch)  # ADDING ALL THE LETTERS OF THE STRING IN THE STACK

    rev=""

    while not(s1.isEmpty()):   # RUNNING THE WHILE LOOP TILL THE STACK IS EMPTY
        rev+=s1.pop()  # POPPING OUT THE ELEMENTS IN THE STACK AND ADDING THEM TO THE REV VARIABLE
    return rev   # RETURNING THE REVERSE OF THE STRING

def main():  # CREATING THE MAIN FUNCTION

    stk=StackADT()   # CREATING AN OBJECT OF THE CLASS

    while True:  # MAKING A MENU DRIVEN CODE USING WHILE LOOP

        # PRINTING ALL THE MENU OPTIONS

        print("*-------------------*")
        print("StackADT Menu...")
        print("1. push")
        print("2. pop")
        print("3. peek")
        print("4. isEmpty")
        print("5. display")
        print("6. size")
        print("7. Reverse a string using stack")
        print("8. Exit")

        choice = input("Enter your choice :").strip() # TAKING THE CHOICE FROM THE USER AS AN INPUT

        if choice=="1":  # PUSH OPERATION
            val=input("Enter your value :")
            stk.push(val)
            print(val ,"Pushed successfully !!")

        elif choice=="2":  # POP OPERATION
            if stk.isEmpty():
                print("Stack underflow !")
            else:
                print(stk.pop(),"Pop successful !!")
             
        elif choice=="3":  # PEEK OPERATION
            if stk.isEmpty():
                print("Stack underflow !")
            else:
                print(stk.peek(),"Is the TOP of the Stack .")

        elif choice=="4":   # ISEMPTY OPERATION
            print(stk.isEmpty())  # WILL RETURN TRUE OR FALSE

        elif choice=="5":  # DISPLAY OPERATION
            print(stk.display())

        elif choice=="6":  # SIZE OPERATION
            print(stk.size(), "is the size of the stack .")

        elif choice=="7": # REVERSE A STRING USING STACK OPERATION
            print("Reversing a string using stack.")
            ustr=input("Enter the string :")
            print("Reverse string :")
            print(Reverse_string(ustr))

        elif choice=="8":  # EXITING THE LOOP 
            print("Exiting.... Thanks for visiting !!")
            break

        else:   # HANDLING THE WRONG INPUTS BY THE USER
            print("Invalid input !!")
            print("Please enter a valid choice !!")

if __name__=="__main__":  
    main()  # CALLING THE MAIN FUNCTION



# 2. MENU DRIVEN CODE


stk=[]  # DECLARING AN EMPTY LIST 

while True:   # RUNNING THE WHILE LOOP

    print("------------------------------")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. isEmpty")
    print("5. Size")
    print("6. Display stack")
    print("7. Reversing a string using stack")
    print("0. Exit")
    print("------------------------------")

    choice=int(input("Enter your choice :"))   # TAKING CHOICE AS AN INPUT FROM THE USER

    if choice==1:   # PUSH OPERATION
        elt=input("Enter the element you want to add :") 
        stk.append(elt)
        print("Pushed value :",elt)

    elif choice==2:   # POP OPERATION
        popped=stk.pop()
        if popped==None:
            print("Stack underflow !")
        else:
            print("Popped value :",popped)

    elif choice==3:   # PEEK OPERATION
        top=stk[-1]
        if top==None:
            print("Empty stack.")
        else:
            print("Top of the stack :",top)

    elif choice==4:  # ISEMPTY OPERATION
        if len(stk)==0:
            print("Stack is Empty.")
        else:
            print("Stack is not Empty.")

    elif choice==5:   # SIZE OF THE STACK OPERATION
        size=len(stk)
        print("Size of the stack :",size)

    elif choice==6:   # PRINTING THE WHOLE STACK
        print("Stack :",stk)

    elif choice==7:   # REVERSE THE STRING OPERATION
        stk_st=[]
        str=input("Enter the string you want to reverse :")
        for ch in range(len(str)):
            stk_st.append(str[ch])
        rev_str=""
        while len(stk_st)!=0:
            rev_str=rev_str+stk_st.pop()
        print("Reverse of the string :",rev_str)

    elif choice==0:   # EXITING THE LOOP
        print("Exiting.....Thank you for visiting !!")
        print("Good Bye !!")
        break

    else:   # HANDLING THE WRONG INPUTS BY THE USER
        print("Invalid choice !!")
        print("Please try again and enter a valid choice...")
        

