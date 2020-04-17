class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        joker = []
        s_len = len(s)
        
        for i in range(s_len):
            if s[i] == ')':
                if(len(stack) > 0):
                    stack.pop()
                elif(len(joker) > 0):
                    joker.pop()
                else:
                    return False
            elif s[i] == '(':
                stack.append(i)
            else:
                joker.append(i)
        
        while len(stack) > 0 and len(joker) > 0:
            if(stack[-1] > joker[-1]):
                return False
            stack.pop()
            joker.pop()
            
        return True if len(stack) == 0 else False        
