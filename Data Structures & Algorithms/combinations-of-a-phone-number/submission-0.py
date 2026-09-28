class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        res = []

        def reccur(index,curStr):
            print(curStr,len(curStr))
            
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            if(index > len(digits)):
                return

            for i in dict1[digits[index]]:
                reccur(index+1,curStr+i)

        if not digits:
            return []
        reccur(0,"")
        return res

    


