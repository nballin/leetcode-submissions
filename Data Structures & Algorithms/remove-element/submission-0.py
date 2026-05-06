#output int k
#1. k=0 iterate i
#2. check if [i]!= val, rewrite num[k]
#3. if it does == val, k+=1
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0;
        for i in range(len(nums)):
            if nums[i]!= val:
                nums[k] = nums[i]
                k+=1
        return k
