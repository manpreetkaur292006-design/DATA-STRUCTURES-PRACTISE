class StackADT:
    def __init__(self):
        self.data=[]
    def isEmpty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def push(self,n):
        if self.isEmpty()==True:
            return "Stack underflow !"
        else:
            return self.data.append(n)
    def pop(self):
        if self.isEmpty()==True:
            return "Stack underflow !"
        else:
            return self.data.pop()
    def peek(self):
        return self.data[-1]
    def display(self):
        return self.data
    def size(self):
        return len(self.data)
    
def Reverse_string(s):
    s1=StackADT()
    for ch in s:
        s1.push(ch)
    rev=""
    while not(s1.isEmpty()):
        rev+=s1.pop()
    return rev

def main():
    stk=StackADT()
    while True:
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
        choice = int(input("Enter your choice :")).strip()
        if choice==1:
            val=input("Enter your value :")
            stk.push(val)
            print(val ,"Pushed successfully !!")
        elif choice==2:
            print(stk.pop(),"Pop successful !!")
        elif choice==3:
            print(stk.peek(),"Is the TOP of the Stack .")
        elif choice==4:
            print(stk.isEmpty())
        elif choice==5:
            print(stk.display())
        elif choice==6:
            print(stk.size(), "is the size of the stack .")
        elif choice==7:
            print("Reversing a string using stack.")
            string=input("Enter the string :")
            print("Reverse string :")
            print(Reverse_string(string))
        elif choice==8:
            print("Exiting.... Thanks for visiting !!")
            break
        else:
            print("Invalid input !!")
            print("Please enter a valid choice !!")
            
if __name__=="__main__":
    main()
