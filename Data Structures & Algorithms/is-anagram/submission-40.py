class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #== the hashmaps valur of letter count in words.
        countS, countT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS ==countT