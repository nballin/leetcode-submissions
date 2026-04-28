class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

      #1. edge case len = len, if ! ret F
      #2. make hashmaps
      #3. iterate through word, update letter count using .get (0 default if doesnt exist)
      #4. compare count

      if len(s) != len(t):
        return False;

      countS, countT = {}, {};

      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0);
        countT[t[i]] = 1 + countT.get(t[i], 0);

      return countS == countT;