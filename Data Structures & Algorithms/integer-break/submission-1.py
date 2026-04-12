class Solution:
    def integerBreak(self, n: int) -> int:
        list1 = [0 for _ in range(n)]
        def DFS(x):
            if list1[x-1] != 0:
                # print("oof")
                return list1[x-1]
            if x == 0:
                return 1

            maximum = float("-inf")
            for i in range(1,len(list1)):
                if (x>=i):
                    res = DFS(x-i)
                    maximum = max(res*i,maximum)
            
            list1[x-1] = maximum
            return maximum
        
        res=DFS(n)
        # print(list1)
        return res

                    
        


        
        