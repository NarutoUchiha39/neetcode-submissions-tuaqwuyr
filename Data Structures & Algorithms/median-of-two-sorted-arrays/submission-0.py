class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A:List[int] = nums1
        B:List[int] = nums2
        SumLen:int = len(A)+len(B)

        if(len(nums1)>len(nums2)):
            A,B = B,A
        
        l:int = 0
        r:int = len(A)-1
        mid:int = (len(A)+len(B))//2

        while True:
            i = (l+r)//2
            j = mid - i - 2

            LEFTA = A[i] if i>=0 else float("-inf")
            LEFTB = B[j] if j>=0 else float("-inf")

            RIGHTA = A[i+1] if (i+1) < len(A) else float("inf")
            RIGHTB = B[j+1] if (j+1) < len(B) else float("inf")

            if(LEFTA <= RIGHTB and LEFTB <= RIGHTA):
                if(SumLen%2):
                    return min(RIGHTA,RIGHTB)
                return (max(LEFTA,LEFTB)+min(RIGHTA,RIGHTB))/2
            if(LEFTA>RIGHTB):
                r = i-1
            else:
                l = i+1
