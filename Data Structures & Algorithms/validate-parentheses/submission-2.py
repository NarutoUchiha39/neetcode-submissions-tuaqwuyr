class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for index,element in enumerate(s):
            if element == "{" or element == "[" or element == "(":
                stack.append(element)
            elif stack and ((element == "}" and stack[-1] == "{" )
             or (element == "]" and stack[-1] == "[") 
             or element == ")" and stack[-1] =="("):
                stack.pop()
            else:
                return False

        return True and len(stack)==0



