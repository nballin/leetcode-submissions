class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #output: true or false if anagram 
        #edgecase: if length not equal then false

        #make hashmap of key letter:count for both S and t 
        #if length is same, then it doesnt matter: can use range s
        #count at[] = +1 .get (retrieves value or adds default 0)
        #check if the hash s == t

      if len(s) != len(t):
        return False;

      countS, countT = {}, {};

      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0);
        countT[t[i]] = 1 + countT.get(t[i], 0);

      return countS == countT;


