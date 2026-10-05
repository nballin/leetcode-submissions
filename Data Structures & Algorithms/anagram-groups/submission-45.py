class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      #comparing final hash values
      #get hash letter count for each word

      #make res a default dict list 
      #make count an empty 0s list 26 long (to keep count on letters)
      #for each word, count c using ascii values
      
      #in res list, add the word where the key is that count 

      res = defaultdict(list)

      for s in strs:
        count = [0] * 26

        for c in s:
          count[ord(c) - ord("a")] += 1

        res[tuple(count)].append(s)
      return list(res.values())
        