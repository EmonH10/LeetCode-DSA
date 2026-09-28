class Solution:
    def maxDepth(self, s: str) -> int:

        stack = []
        maximum = 0

        for element in s:
            
            if element == '(':
                stack.append(element)
                maximum = max(maximum,len(stack))

            elif element == ')':
                stack.pop()

        return maximum


                
        