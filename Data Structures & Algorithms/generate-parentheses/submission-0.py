class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def DFS(temp,openB,closeB):
            
            if( closeB > openB or openB > n ):
                return 

            elif(openB == n and closeB == n):
                res.append(temp)
                return

            temp += "("
            openB += 1

            DFS(temp,openB,closeB)
            temp = temp[:-1] + ")"
            openB -= 1
            closeB += 1

            DFS(temp,openB,closeB)

        DFS("",0,0)

        return res
            
            

            


            

        