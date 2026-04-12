class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = defaultdict(int)
        if bills[0] >5:
            return False

        for i in range(len(bills)):
            # print(bank)
            if bills[i]>5:
                change = bills[i] - 5
                
                need_5 = change//5
                need_10 = change//10
                need_20 = change//20
                    
                if need_10 >0:
                    if bank[10] >0:
                        bank[10] -= need_10
                        left = change -10
                        if left != 0:
                            bank[5] -= left//5
                            if bank[5] <0:
                                return False
                    else:
                        bank[5] -= need_5
                        if bank[5] <0:
                            return False
                
                else:
                    bank[5] -= need_5
                    if bank[5] <0:
                            return False

            bank[bills[i]] +=1

        return True