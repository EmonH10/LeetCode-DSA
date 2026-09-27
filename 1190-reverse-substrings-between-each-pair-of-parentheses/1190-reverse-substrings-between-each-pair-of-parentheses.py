class Solution:
    def reverseParentheses(self, s: str) -> str:

        stack = []

        for i in range(0,len(s)):
            if s[i] != ')':
                stack.append(s[i])
            else:
                element = ""
                j = len(stack)-1
                while(stack[j] != '('):
                    element += stack.pop()
                    j-=1

                if stack[j] == '(':
                    stack.pop()

                for k in element:
                    stack.append(k)

        print(stack)

        return "".join(stack)