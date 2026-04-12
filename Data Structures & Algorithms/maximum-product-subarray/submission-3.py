class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = float("-inf")
        product = 1
        high = 1 
        low =  1

        for index,element in enumerate(nums):
            # print(high)
            product = high * element
            high = max(product,low*element,element)
            low = min(low*element,product,element)
            max_num = max(high,max_num)

        return max_num