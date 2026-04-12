class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right <len(s):
                if s[left] == s[right]:
                    if len(res) < right-left+1:
                        res = s[left:right+1]
                    left -=1
                    right+=1
                else:
                    break

            left = i
            right = i+1
            while left >= 0 and right <len(s):
                if s[left] == s[right]:
                    if len(res) < right-left+1:
                        res = s[left:right+1]
                    left -=1
                    right+=1
                else:
                    break

        return res