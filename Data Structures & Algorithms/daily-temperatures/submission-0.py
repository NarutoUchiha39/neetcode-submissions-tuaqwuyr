class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minStack = []
        res = [0 for i in range(len(temperatures))]

        for index,element in enumerate(temperatures):
    
            while minStack:
                if element > minStack[-1][0]:
                    ele = minStack.pop(-1)
                    res[ele[1]] = index-ele[1]
                else:
                    break
            minStack.append([element,index])
            # print(minStack,res)
        
        return res
                    