class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #output: indeces of i and j
        #1. start with each one iterate , target - [i], does it exist in map? add if not
        #2. if it does exist, return current index, and index of number found
        ##doing this with brute force is heavy on the TC


        prevMap = {} # val : index
        for i, n in enumerate(nums):
          diff = target - n;
          if diff in prevMap:
            return [prevMap[diff], i]
          prevMap[n] = i