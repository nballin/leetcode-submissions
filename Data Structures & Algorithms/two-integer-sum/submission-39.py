class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #getting both value in i so enumarate(nums)
        #calc diff 
        #check if diff in seen or else seen at [n] = i
        #if seen then return (seen[diff], i)

        seen = {}

        for i, n in enumerate(nums):
          diff = target - n
          if diff in seen:
            return[seen[diff], i]
          seen[n] = i
        