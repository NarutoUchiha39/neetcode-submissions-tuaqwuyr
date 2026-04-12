class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        left = 0
        right = 0
        num = ""

        while((left<len(word)) and (right<len(abbr))):
            
            if abbr[right].isnumeric():
                if num=="" and abbr[right] == "0":
                    return False
                num+=abbr[right]
                right+=1
            elif num!="":
                num_ = int(num)
                left = left+num_
                if left > len(word)-1:
                    return False
                num = ""

            elif word[left] == abbr[right]:
                left+=1
                right+=1
            else:
                return False
        
        
        if left != len(word):
            if num == "":
                return False
            else:
                num_ = len(word[left:])
                num__ = int(num)
                if num_ == num__:
                    return True
                else:
                    return False
        return True
            
        