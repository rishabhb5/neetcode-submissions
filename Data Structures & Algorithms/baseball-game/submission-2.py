class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        
        for i in operations:
            calc = 0
            if i == "+":
                calc = int(stack[-1]) + int(stack[-2])
                stack.append(calc)
            elif i == "D":
                calc = int(stack[-1]) * 2
                stack.append(calc)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))
        
        return sum(stack)