class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for i in range(len(logs)):
            if len(stack) > 0:
                if logs[i] == "../":
                    stack.pop()
                elif logs[i] == "./":
                    stack[-1]
                else:
                    stack.append(logs[i])
            else:
                if logs[i] != "./" and logs[i] != "../":
                    stack.append(logs[i])
        
        return len(stack)
                