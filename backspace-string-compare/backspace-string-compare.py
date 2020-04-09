class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def applyingBackspace(string):
            stack = []
            for char in string:
                if(char != '#'):
                    stack.append(char)
                else:
                    if(len(stack) > 0):
                        stack.pop()
            
            return ''.join(stack)

        first_s = applyingBackspace(S)
        second_s = applyingBackspace(T)
        
        return first_s == second_s