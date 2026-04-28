class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        #output: T/F if duplicates
        #can brute force, would take long

        #for i range length of nums = starting 0 to last index 
        #then check the range j from i+1 (second index) until len(nums) (last)
        #check if ==
        #return true or false

        for i in range(len(nums)):
          for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
              return true
        return false


