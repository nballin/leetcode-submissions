class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list);

      for s in strs: #making an array of 26 (for each of 26 letters)
        count = [0] * 26; #a...z

        for c in s:
          count[ord(c) - ord("a")] += 1; #starts indec at 0 to 25, and not 97 - 122

        res[tuple(count)].append(s);

      return list(res.values());