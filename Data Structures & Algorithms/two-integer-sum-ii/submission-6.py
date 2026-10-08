class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #because it's ordered, some number combinations might be too big or too smal f rthe target, so we can adjust 2 ptr from both ends 
        #if current sum is > target then decrease bigger number (r-=1)
        #if curSum < target then increase smaller nuber (l += 1)
        #if none of those then obviously equal, return l and r (add one to both cause its 1 point index)
        #guaranteed a result, bet add return and empty arr anyeays as final

        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else: 
                return [l+1, r+1]
        return []