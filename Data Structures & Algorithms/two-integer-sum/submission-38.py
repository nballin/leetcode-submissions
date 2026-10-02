class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #go through array (get both i and n)
        #calculate diff
        #see fo diff exists. 
        #if not add. 
        #use set (no dupes)
        #add if not already existing

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        