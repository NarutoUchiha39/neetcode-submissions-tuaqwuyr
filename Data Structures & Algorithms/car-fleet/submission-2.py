class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        res = [[position[i],(target - position[i])/speed[i],1] for i in range(len(position))]

        res.sort(key=lambda x: x[0]) # Sorting helps to know whats the closest element that can be taken in a fleet. Otherwise, an incomming element can overtake any element in the stack and will be hard to find. Will find a way to do it without sorting later

        stack = []
        fleet = 0

        if(len(position) == 1):
            return 1

        for index,element in enumerate(res):
            last = None
            if(not stack): # When Stack is empty
                stack.append(element)
            else:
                while (stack and stack[-1][1]<=element[1]): # On encountering slower element, pop the faster and replace with slower
                    stack.pop()
                    last = element
                if(stack and stack[-1][1]>element[1]): #If you encounter faster element append it. We do it in case in future a slower element comes and can replace the faster element
                    stack.append(element)
                elif (not stack) and last: # When the incomming slower element causes all the elements in the stack to be poped, we still need the slower element
                    stack.append(element)

            # print(stack,fleet,element)

        if(last == element): # Used when all elements are popped and the last slow element is there. It needs to be popped as well
            stack.pop()

        return 1+len(stack)  if last else len(stack)# 1 because all the elements that can be in one fleet are popped and the elements that are not compatible will be in stack

# [[0, 5.0, 1], [2, 2.6666666666666665, 1], [4, 6.0, 1]]
