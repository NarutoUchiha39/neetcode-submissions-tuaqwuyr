class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        DictSet = set(dictionary)
        DP = {}

        def DFS(index):
            if(index == len(s)):
                return 0
            if(index in DP):
                return DP[index]
                
            res = 1+DFS(index+1)
            for i in range(index,len(s)):
                if(s[index:i+1] in DictSet):
                    res = min(res,DFS(i+1))
            
            DP[index] = res
            return res
        
        return DFS(0)

        