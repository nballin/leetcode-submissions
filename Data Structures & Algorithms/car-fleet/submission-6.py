class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #if the cars within the distance have the same speed or less before target, they are in the sae fleet. 
        #calculate the speed itll take by finding distance/speed
        #append to the stack the speed after calculations 
        #pop from stack if less or equal
        #make sure to sort the input arr, but go from end (fastest is the threshold)

        pair = [[p,s] for p,s in zip(position, speed)]

        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
