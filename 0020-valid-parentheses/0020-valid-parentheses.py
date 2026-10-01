class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] 

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            
            elif len(stack)>0 and i == ')' and stack[-1] == '(':
                stack.pop()
            elif len(stack)>0 and i == '}' and stack[-1] == '{':
                stack.pop() 
            elif len(stack)>0 and i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)


        if len(stack) == 0:
            return True

        return False

        