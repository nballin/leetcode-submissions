class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_list = list(s)
        char_list.sort()
        char_list2 = list(t)
        char_list2.sort()

        return char_list == char_list2