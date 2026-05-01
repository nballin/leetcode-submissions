class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

      #Make a hash set for seen numbers 
      #check if seen, return true, if not add
      #return false 
      
      seen = set();

      for n in nums:
        if n in seen:
          return True;
        seen.add(n);
      return False;
