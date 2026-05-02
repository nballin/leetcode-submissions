
#returning a list -> return list(...)
#make a default dictionary
#loop through every word, and every character in word
#make an empty list of 0s (26)
#since it is a letter based question, start index at 0. C - "a" using ord ->shows index of current letter
#res arr is count (make it a tuple) and append the current word into it
#return this list'a values
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      res = defaultdict(list);

      for s in strs: #making an array of 26 (for each of 26 letters)
        count = [0] * 26; #a...z

        for c in s:
          count[ord(c) - ord("a")] += 1; #starts indec at 0 to 25, and not 97 - 122

        res[tuple(count)].append(s);

      return list(res.values());
