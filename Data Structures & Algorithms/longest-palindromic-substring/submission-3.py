class Solution:
    def longestPalindrome(self, s: str) -> str:

        left = 0
        pointer = 0
        substring = ""
        while pointer < len(s):
            right = pointer
            left = pointer
            cursub = ""

            while left >= 0 and right <len(s) and s[right] == s[left]:
                # print(s[left]," ",s[right]," ",left," ",right)
                cursub = s[left:right+1]
                right +=1       
                left -=1

            if len(cursub) > len(substring):
                substring = cursub
            
            left = pointer
            right = pointer+1
            if right == left+1:
                while left >= 0 and right <len(s) and s[right] == s[left]:
                    # print("Even ",s[left]," ",s[right]," ",left," ",right)
                    cursub = s[left:right+1]
                    right +=1       
                    left -=1
                    
            if len(cursub) > len(substring):
                substring = cursub
            
            pointer += 1
        
        return substring
            
                

                    
