class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            # find length prefix before '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1  # skip '#'
            res.append(s[j:j+length])
            i = j + length
        return res