class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #need set (no dupes) to keep count of numbers seen
        #if number seen in hashmap -> false

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False