class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        final_str = ""
        for i in s:
            if i == "]":
                curStr = ""
                while stack and stack[-1] != "[":
                    res = stack.pop()
                    curStr+=res
                stack.pop()
                num = ""
                
                try:
                    while(stack):
                        int(stack[-1])
                        ele = stack.pop()
                        num += ele
                except Exception as e:
                    pass

                # print(num,curStr)
                for j in range(int(num[::-1])):
                    stack.append(curStr)
                        # print(curStr,stack)
            else:
                stack.append(i)
            
            # print(stack)

        for i in stack:
            final_str+=i[::-1]

        return final_str