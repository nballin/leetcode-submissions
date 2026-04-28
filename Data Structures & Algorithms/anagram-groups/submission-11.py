class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newList = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            newList[key].append(word)
        return list(newList.values())