class Solution:
    def isPali(self,s,i,j):

            while(i < j):
                if(s[i] != s[j]):
                    return False
                i+=1
                j-=1
            return True

    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []

        
        def DFS(index):
            if(index >= len(s) ):
                res.append(part.copy())
                return

            for j in range(index,len(s)):
                if(self.isPali(s,index,j)):
                    part.append(s[index:j+1])
                    DFS(j+1)
                    part.pop()

        DFS(0)
        return res