class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #output = T or F
        #. edge case: if length !==, return false
        #1. sort string, compare 

        if len(s) != len(t):
          return False;
        return sorted(s) == sorted(t);