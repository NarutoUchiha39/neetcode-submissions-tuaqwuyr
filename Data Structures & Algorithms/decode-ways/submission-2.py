class Solution:
    def numDecodings(self, s: str) -> int:

        def countWays(x):
    
            if x == len(s):
                return 1
            
            if s[x] == '0':
                return 0

            res = countWays(x+1)
            if(x<len(s)-1):
                if (s[x] == '1'or (s[x] == "2" and int(s[x+1])<7)):
                    res += countWays(x+2)
            
            return res


        return countWays(0)


                
        
        