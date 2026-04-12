from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

       hashmap_1 = Counter(t)
       hashmap_2 = {}
       have = 0
       need = len(hashmap_1)
       length = float("inf")

       right = 0
       left = 0
       res = [-1,-1]

       while(right < len(s)):

        hashmap_2[s[right]] = 1+hashmap_2.get(s[right],0)

        if(s[right] in hashmap_1 and hashmap_1[s[right]] == hashmap_2[s[right]]):
            have += 1

        while( have == need  ):
            if( (right - left + 1) < length ):
                length = right - left + 1
                res[0] = left
                res[1] = right

            hashmap_2[s[left]] -= 1
            if(s[left] in hashmap_1 and hashmap_1[s[left]] > hashmap_2[s[left]]):
                have -=1
            left += 1
        right += 1

       return s[res[0]:res[1]+1] if length != float("inf") else ""


            



        




        