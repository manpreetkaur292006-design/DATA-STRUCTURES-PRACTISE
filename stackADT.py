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

