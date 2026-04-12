from copy import deepcopy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        global_list = []
        set1 = set()

        def DFS(index, temp_list, temp,temp_sum ):

            if(temp == target):
                temp1 = deepcopy(temp_sum)
                temp1.sort()
                tup = tuple(temp1)

                if(tup not in set1):
                    set1.add(tup)
                    global_list.append(deepcopy(temp_sum))
                
                return  

            elif(index >= len(temp_list)):
                return


            temp_sum.append(temp_list[index])
            temp += temp_list[index]
            DFS(index+1,temp_list,temp,temp_sum)

            temp -= temp_list[index]
            temp_sum.pop()
            DFS(index+1,temp_list,temp,temp_sum)

        DFS(0,candidates,0,[])
        return global_list


        