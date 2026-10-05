class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

      #organise words by asccii hashmap values
      #use default dict list for result

      #make count list all 0s 26 long (all chars) for each word in strs
      #for each c in s, to teh ascii conversion 

      #append the word s to this count in res (use tuple)

      #show the values of result

      res = defaultdict(list)

      for s in strs:
        count = [0] * 26

        for c in s:
          count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
      return list(res.values())
        