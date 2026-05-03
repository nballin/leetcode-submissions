class Solution:
# we want to add the length of the word + delimiter + actual word so that we can decode it later
# output = str ""
# update the res string for each word and return
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res 

# res = list with pointer starting at 0
# make an internal pointer j for each word thati is at starting at i
# check if value of j at s is #, if it is, j+=1 to move pointer
# j stops at #, so calutulate length of the word
# get the word excluding the length and delimiter
# append to res list
# move i to start past that word
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res
