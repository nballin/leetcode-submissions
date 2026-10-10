class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #pretty much when c makes it to an operator, take the previous numbers out, operate, them append back
        #for - and division, b then a
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                 a,b = stack.pop(), stack.pop()
                 stack.append(int(b/a))
            else:
                stack.append(int(c))
        return stack[0]