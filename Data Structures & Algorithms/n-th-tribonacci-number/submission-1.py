class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        n0 = 0
        n1 = 1
        n2 = 1

        for i in range(3,n+1):
            sum1 = n0 + n1 + n2
            temp = n1
            n1 = n2
            n0 = temp
            n2 = sum1

        return n2 
        