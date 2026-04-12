class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [ i for i in range(n) ]
        lengthDSU = [ 1 for i in range(n) ]

        def DSU():

            def findPar(ele1):

                def parent(par1):
                    if(par[par1] == par1):
                        return par1
                    element =  par[ par[par1] ]
                    return parent( element )

                return parent(ele1)
                
            for i in edges:
                ele1 = i[0]
                ele2 = i[1]
                par1 = findPar(ele1)
                par2 = findPar(ele2)

                if(par1 == par2):
                    lengthDSU[par1] += 1

                elif(par1 != par2):
                    if(lengthDSU[par1] > lengthDSU[par2]):
                        lengthDSU[par1] += lengthDSU[par2]
                        par[par2] = par1
                    
                    else:
                        lengthDSU[par2] += lengthDSU[par1]
                        par[par1] = par2

        DSU()
        count  = 0 
        for i in range(len(par)):
            if(par[i] == i):
                count += 1
        return count





                



        
        