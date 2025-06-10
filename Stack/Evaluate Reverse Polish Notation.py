from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return 0
        stack = []
        for element in tokens:
            if element[-1].isnumeric():
                stack.append(int(element))
            else:
                b = stack.pop()
                a = stack.pop()
                if element == "+":
                    res = a + b
                elif element == "-":
                    res = a - b
                elif element == "*":
                    res = a * b
                elif element == "/":
                    res = a / b
                stack.append(int(res))
        return int(stack[0])
