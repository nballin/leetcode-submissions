class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #use arraw of ascii as code to make the words into numbers
        #use defaultdict()
        #ord = ascii

        #make a count for each word in arr
        #make a count for each letter in word

        #res is a tuple (immutable) and should output values

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())