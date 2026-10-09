class Solution:
    def trap(self, height: List[int]) -> int:
        #using 2 ptr, minimum between the max l and r is the bottle neck
        #shift the smaller ptr, and update the max from what it is to the current height
        #append to result

        if not height: return 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if height[l] < height[r]:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res