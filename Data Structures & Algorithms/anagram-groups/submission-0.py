from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for i in range(len(strs)):
            
            tuple1 = tuple(sorted(strs[i]))
            if(tuple1 in hashmap):
                hashmap[tuple1].append(strs[i])
            else:
                hashmap[tuple1] = [strs[i]]
        
        list1 = [hashmap[i] for i in hashmap]
        
        return list1

        