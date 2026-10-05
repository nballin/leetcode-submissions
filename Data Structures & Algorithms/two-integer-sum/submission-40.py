class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #given an input arr, find diffence and see if the difference is in nums
      #if it is, return the in seen where diff is, and the current i in nums we checked
      #if it is not in nums, add it to seen. 

      seen = {}

      for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
          return[seen[diff], i]
        seen[n] = i