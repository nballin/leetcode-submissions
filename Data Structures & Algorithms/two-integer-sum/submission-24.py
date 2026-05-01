class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #as we gor through numbers, - it from target, check if the number is there, then return 
      #make hash dictionary 
      #loop through index and number (use enumerate)
      #calucate diff = target - n
      #if diff in seen, then return index of number in seen hash, and return index we are at right
      #if not add the number and index to the hash 

      seen = {}; #value : index

      for i, n in enumerate(nums):
        diff = target - n;
        if diff in seen:
          return [seen[diff], i]
        seen[n] = i;