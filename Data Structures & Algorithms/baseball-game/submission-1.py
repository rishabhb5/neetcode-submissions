class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        prevRecord = 0

        for i in range(len(operations)):
            currOp = operations[i]
            if currOp != "+" and currOp != "D" and currOp != "C":
                stack.append(int(currOp)) # should be an int
            elif currOp == "+":
                stack.append(stack[-1] + stack[-2])
            elif currOp == "D":
                stack.append(stack[-1] * 2)
            else: # 'C'
                stack.pop()
        
        total = 0
        for i in range(len(stack)):
            score = stack.pop()
            total += score
        
        return total

        