from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        hashmap = {}
        hashmap_s = Counter(t)
        length = float("inf")
        cur_str = ""
        left = 0

        for i in range(len(s)):
            right = i
            while(right < len(s)):
                if(s[right] in hashmap_s):
                    if(hashmap.get(s[right],0) == 0):
                        hashmap[s[right]] = hashmap.get(s[right],0) + 1
                    elif(hashmap[s[right]] < hashmap_s[s[right]]):
                        hashmap[s[right]] = hashmap.get(s[right],0) + 1
                
                if(hashmap == hashmap_s):
                    if((right-i)+1 < length):
                        cur_str = s[i:right+1]
                        length = len(s[i:right+1])
                right+=1
            
            hashmap.clear()


        return cur_str




        