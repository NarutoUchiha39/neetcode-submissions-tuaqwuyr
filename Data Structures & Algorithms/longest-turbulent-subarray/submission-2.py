class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        last_symbol = ""
        i = 0
        j = 0
        max_len = float("-inf")
        while j < len(arr)-1:
            print(i,j,last_symbol,max_len)
            if arr[j] > arr[j+1]:
                if last_symbol == "" or last_symbol == "<":
                    last_symbol = ">"
                    max_len = max(max_len,j-i+2)
                else:
                    i = j
            
            elif arr[j+1] > arr[j]:
                if last_symbol == "" or last_symbol == ">":
                    last_symbol = "<"
                    max_len = max(max_len,j-i+2)
                else:
                    i = j

            elif arr[j] == arr[j+1]:
                i = j+1

            j+=1

        print(i,j,max_len)
        return max_len if max_len != float("-inf") else 1