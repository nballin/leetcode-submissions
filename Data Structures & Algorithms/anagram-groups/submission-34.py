class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       #use ascii valuesa as sict key (defaultdict(lsit))
       #make count for each word (26)
       #make count for each letter in word (use ascii to distinguish word into binary almost)
       #add word to said key (make it a tuple so it can be used as key)
       #return list values

        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        
        return list(res.values())