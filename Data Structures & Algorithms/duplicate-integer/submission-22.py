class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


      #use hash: make a seen set
      #loop through list, check if seen, if so return True
      #if not seen, add to list and return False

      seen = set();
      for n in nums:
        if n in seen:
          return True;
        seen.add(n);
      return False;