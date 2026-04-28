class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

      seen = set();

      for n in nums:
        if n in seen:
          return True;
        seen.add(n)
      return False

#lets use hashset to make in an O(1) for better TC
#1. make a set for seen numbers
#2. loops through n in nums and check if it is in the seen numbers set
#3. if not, then add it to the set

