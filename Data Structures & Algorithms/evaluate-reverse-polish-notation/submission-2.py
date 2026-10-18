class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                x = stack.pop()
                y = stack.pop()
                if tokens[i] == '+':
                    result = x + y
                elif tokens[i] == '-':
                    result = y - x
                elif tokens[i] == '*':
                    result = int(x * y)
                else:
                    result = int(y/x)
                stack.append(result)

        return stack[-1]