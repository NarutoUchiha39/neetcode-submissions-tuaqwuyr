class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxf = 0
        max1 = 0
        l = 0
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1+ hashmap.get(s[i],0)
            maxf = max(maxf,hashmap[s[i]])
            while( (i - l + 1) - maxf > k ):
                hashmap[s[l]] -=1
                l+=1
        
            max1 = max(max1,(i-l+1))

        return max1




        