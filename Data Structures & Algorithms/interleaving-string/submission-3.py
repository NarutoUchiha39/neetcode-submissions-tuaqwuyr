from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def DFS(index1,index2,index3):
            if (index3 == len(s3)):
                print(index2,index1)
                if index2 != len(s2) or index1!=len(s1):
                    return False
                return True
            if (index1 < len(s1) and index2 < len(s2)) and (s3[index3] == s1[index1]) and (s3[index3] == s2[index2]):
                return DFS(index1+1,index2,index3+1) or DFS(index1,index2+1,index3+1)
            
            elif (index1 <len(s1)) and s3[index3] == s1[index1]:
                return DFS(index1+1,index2,index3+1)
            elif (index2 <len(s2)) and s3[index3] == s2[index2]:
                
                return DFS(index1,index2+1,index3+1)
            
            else:
                return False
        return DFS(0,0,0)



        