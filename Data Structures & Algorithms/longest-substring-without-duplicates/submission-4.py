class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        hashmap = {}
        max1 = 0

        for i in range(len(s)):
            
            if(s[i] in hashmap):
                index = hashmap[s[i]] + 1
                max1 = max(max1,len(hashmap))
                for k in range(left,hashmap[s[i]]+1):
                    del hashmap[s[k]]
                left = index

            hashmap[s[i]] = i
        
        return max(max1,len(hashmap))

        