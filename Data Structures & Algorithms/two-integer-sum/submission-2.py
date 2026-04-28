class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)): #loop every index
            for j in range(i+1, len(nums)): #every index after i
                if nums[i] + nums[j] == target:
                    return [i,j]