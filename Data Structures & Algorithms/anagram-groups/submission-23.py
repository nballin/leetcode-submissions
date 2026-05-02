#output -> res(list)
#result is a default dictionary (so empty)
#we want to iteratle through every word s, and every char c in word s
#we make a count list of 26 slots
#for each letter in word, we increment by one. In an anagra, it will be the same lsit outputed
#its ascii chars, so so ord - ord(a)
#result -> tuple so its immutable 
#retrurn the values on res as a list
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list);

      for s in strs:
        count = [0] * 26;

        for c in s:
          count[ord(c) - ord("a")] += 1;

        res[tuple(count)].append(s);

      return list(res.values());
