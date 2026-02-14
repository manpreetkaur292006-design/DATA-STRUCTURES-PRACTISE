
# LEETCODE PROBLEM :

# TWO SUM:

nums=[2,7,11,15]
target=9
def two_sum(nums,target):
    s=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            s=nums[i]+nums[j]
            if s==target:
                return [i,j]
            else:
                continue
print(two_sum(nums,target))