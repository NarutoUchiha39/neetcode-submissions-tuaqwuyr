class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        list1 = []

        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            
        for i in hashmap:
            list1.append([hashmap[i],i])

        list1.sort(key = lambda x:x[0],reverse=True)
        ans = []

        for i in range(k):
            ans.append(list1[i][1])

        return ans



        