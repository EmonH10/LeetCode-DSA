class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for element in tokens:
            if element != "+" and element != "-" and element != "*" and element != "/":
                stack.append(element)
            else:
                operation = element
                first = int(stack.pop())
                second = int(stack.pop())
                if operation == "+":
                    result = second+first
                elif operation == '-':
                    result = second-first
                elif operation == "*":
                    result = second*first
                elif operation == "/":
                    result = int(second/first)
          
                
                stack.append(result)

        return int(stack[-1])
        