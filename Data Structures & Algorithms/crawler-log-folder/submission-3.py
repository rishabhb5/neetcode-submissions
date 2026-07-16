class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for i in range(len(logs)):
            if logs[i] != "../" and logs[i] != "./":
                stack.append(logs[i])
            else:
                if len(stack) > 0 and logs[i] == "../":
                    if logs[i] != "./":
                        stack.pop()
        
        return len(stack)