class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       
        res = set()
        nums.sort()

        for l in range(len(nums)):
            r = len(nums) -1
            l1 = l+1
            while(l1<r):
                Sum = nums[l1]+nums[l]+nums[r]
                if((l,l1,r) in res):
                    continue
                if(((l,l1,r) not in res) and Sum == 0):
                    res.add((nums[l],nums[l1],nums[r]))
                    l1+=1
                    r-=1

                if(Sum>0):
                    r-=1
                elif(Sum<0):
                    l1+= 1

        return [list(i) for i in res]
            