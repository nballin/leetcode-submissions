class Solution:

    def encode(self, strs: List[str]) -> str:
        #make res = ""
        #add to string the length, delimiter, then word
        #return res
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #make a res list with ptr i 
        #for i in bound of string length
        #set j = i (new ptr)
        #check if [j] in string s is not "#" and increment j or calculate legnth of worth (ptr i to j)
        #if #, then append to result the start of word (char after #) and up to length
        #set i to nexct word start
        # return res
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res