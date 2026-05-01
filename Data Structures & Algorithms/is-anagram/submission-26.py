#edge case: check if len(s) = len(t); return
#make hashmaps for both
#update count on each index in s and t: -> + 1 on each, with .get(retrieves key value)
#check if hash maps are equal 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      if len(s) != len(t):
        return False;

      countS, countT = {},{};
      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0);
        countT[t[i]] = 1 + countT.get(t[i], 0);

      return countS == countT;

      