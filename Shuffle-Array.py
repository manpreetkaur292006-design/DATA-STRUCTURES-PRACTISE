
# LEETCODE PROBLEM :

# SHUFFLE AN ARRAY :

nums=[1,2,3,4,5,6]
def Shuffle(nums):
    length=len(nums)
    n1=[]
    n2=[]
    for i in range(0,int(length/2)):
        n1.append(nums[i])
    for j in range(int(length/2),length):
        n2.append(nums[j])
    newnums=[]
    for k in range(len(n1)):
        newnums.append(n1[k])
        newnums.append(n2[k])
    return newnums
print(Shuffle(nums))