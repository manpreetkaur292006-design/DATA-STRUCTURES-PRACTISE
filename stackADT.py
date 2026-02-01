
# STACK ADT IMPLEMENTATION AND REVERSING THE STRING USING STACK ILLUSTRATION

class StackADT:   # DEFINING THE CLASS 

    def __init__(self):   # DEFINING THE INIT METHOD
        self.data=[] 

    def isEmpty(self):    # DEFINING THE isEmpty METHOD
        if len(self.data)==0:
            return True
        else:
            return False
        
    def push(self,n):    # DEFINING THE push METHOD
        if self.isEmpty()==True:   # CHECKING THE STACK UNDERFLOW CONDITION
            return "Stack underflow !"
        else:
            return self.data.append(n)    # ADDING THE ELEMENT TO THE STACK
        
    def pop(self):   # DEFINING THE pop METHOD
        if self.isEmpty()==True:   # CHECKING THE STACK UNDERFLOW CONDITION
            return "Stack underflow !"
        else:
            return self.data.pop()   # REMOVING THE TOP ELEMENT FROM THE STACK
        
    def peek(self):  # DEFINING THE PEEK METHOD AND CHECKING THE TOP ELEMENT OF THE STACK
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

        choice = int(input("Enter your choice :")).strip() # TAKING THE CHOICE FROM THE USER AS AN INPUT

        if choice==1:  # PUSH OPERATION
            val=input("Enter your value :")
            stk.push(val)
            print(val ,"Pushed successfully !!")

        elif choice==2:  # POP OPERATION
            print(stk.pop(),"Pop successful !!")
             
        elif choice==3:  # PEEK OPERATION
            print(stk.peek(),"Is the TOP of the Stack .")

        elif choice==4:   # ISEMPTY OPERATION
            print(stk.isEmpty())  # WILL RETURN TRUE OR FALSE

        elif choice==5:  # DISPLAY OPERATION
            print(stk.display())

        elif choice==6:  # SIZE OPERATION
            print(stk.size(), "is the size of the stack .")

        elif choice==7: # REVERSE A STRING USING STACK OPERATION
            print("Reversing a string using stack.")
            string=input("Enter the string :")
            print("Reverse string :")
            print(Reverse_string(string))

        elif choice==8:  # EXITING THE LOOP 
            print("Exiting.... Thanks for visiting !!")
            break

        else:   # HANDLING THE WRONG INPUTS BY THE USER
            print("Invalid input !!")
            print("Please enter a valid choice !!")

if __name__=="__main__":  
    main()  # CALLING THE MAIN FUNCTION
