class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #build output arr
        #add to stack, check if temp bigger or smaller, pop previous value if bigger, keep in stack if smaller
        #will end up in monotonic decreasing order
        #find distance in index between the days and add to list
        res = [0] * len(temperatures)
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #pair of first value in stack, and temp is first val in pair 0
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res