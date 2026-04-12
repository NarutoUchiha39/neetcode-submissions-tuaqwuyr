class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        hashmap1 = {}
        hashmap2 = {}
        if(len(s1) > len(s2)):
            return False
        
        for i in range( len(s1) ):
            hashmap1[s1[i]] = 1 + hashmap1.get(s1[i],0)
            hashmap2[s2[i]] = 1 + hashmap2.get(s2[i],0)

        left = 0
        if(hashmap1 == hashmap2):
            return True
        
        for i in range(len(s1),len(s2)):
            c = s2[i]
            hashmap2[s2[i]] = 1 + hashmap2.get(s2[i],0)
            hashmap2[s2[left]] = hashmap2[s2[left]] - 1

            if(hashmap2[s2[left]] == 0):
                del hashmap2[s2[left]]
            if(hashmap2 == hashmap1):
                return True
            
            left += 1


        return False


