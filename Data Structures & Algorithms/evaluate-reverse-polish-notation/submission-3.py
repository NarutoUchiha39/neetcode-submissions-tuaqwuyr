class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        stack_op = []
        for i in range(len(tokens)):
            if(len(tokens[i]) >1 and (tokens[i][0] == "-" or tokens[i][0] == "-")):
                stack.append(tokens[i])

            elif(tokens[i].isalnum()):
                stack.append(tokens[i])
            else:
                top = int(stack[-1])
                second = int(stack[-2])


                if(tokens[i] == "+"):
                    stack.pop()
                    stack.pop()
                    res = top + second
                    stack.append(res)
                elif(tokens[i] == "-"):
                    stack.pop()
                    stack.pop()
                    res = second - top
                    stack.append(res)
                
                elif(tokens[i] == "*"):
                    stack.pop()
                    stack.pop()
                    res = second * top
                    stack.append(res)

                elif(tokens[i] == "/"):
                    stack.pop()
                    stack.pop()
                    res = int(second / top)
                   
                    stack.append(res)
        return stack.pop()
                

        