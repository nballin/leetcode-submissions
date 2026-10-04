class Solution:

    def encode(self, strs: List[str]) -> str:
        #make result string
        #for all s in str -> res += str(len(s)) + "#" + s

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        # we basically want 2 ptrs, one to start and one to keep position in input str
        #start res, i = [], 0 
        #while i in bound so < len(str)
        #j = i introducing new ptr starting at first char
        #while str[j] != #
        #length is i to j 
        #append to res first character after # delimiter to last
        #set i to nect word start (after delimiter)
        #return res

        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])

            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res