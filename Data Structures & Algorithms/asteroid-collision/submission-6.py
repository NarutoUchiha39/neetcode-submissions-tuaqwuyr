from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []

        for index,element in enumerate(asteroids):

            last = None
            while stack and (stack[-1] > 0 and element < 0):
                if(stack and abs(stack[-1]) < abs(element)):
                        stack.pop()
                elif(stack and abs(stack[-1]) > abs(element)):
                     break
                elif(stack and abs(element) == abs(stack[-1])):
                    last = stack.pop()
                    break

            if last and abs(last) == abs(element):
                 continue
            
            if (stack and ((element >0 and stack[-1] >0) or (element <0 and stack[-1]<0) or ((element >0 and stack[-1]<0)))) :
                 stack.append(element)

            elif(not stack):
                stack.append(element)

            # print(stack)

        return stack
