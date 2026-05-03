class Solution:
#output: res = "" (Str)
#1. loop through each word in list
#2. string of the length of word + the delimiting # + the actual word. 
## we need to convert the length int into a string
# return encoded string
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (str(len(s)) + "#" + s)
        return res

#output: res = list
#make pointer i for res list starting at 0
#keep iterating i till end of string
#make internal pointer j that checks until #
#the length int is everything between i and j of s
#append to result from 1st character of word up to last
#move i to start of next encoded word
#return the res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j + 1 + length
        return res

