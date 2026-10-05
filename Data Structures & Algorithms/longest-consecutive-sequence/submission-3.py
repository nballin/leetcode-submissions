class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #turn it into set to check for numbers
        #check for left neighbour to see if it is a start of a sequence
        #if not length = 0, and update length for every consectuive number that exists
        #return longest sequence

        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest