class BST:
    def __init__(self,num) -> None:
        self.num = num
        self.frequency = 1
        self.left = None
        self.right = None


class KthLargest:

    def inorder(self, res: List, node: BST):
        if not node:
            return

        # print(node.num)

        self.inorder(res, node.left)

        for _ in range(node.frequency):
            res.append(node.num)

        self.inorder(res, node.right)

    def insert(self,num):
        if not self.root:
            self.root = BST(num)
            return

        temp = self.root

        while True:
            num1 = temp.num
            # print(num1)

            if(num > num1):
                if(temp.right):
                    temp = temp.right
                else:
                    temp.right = BST(num)
                    return
            
            elif(num < num1):
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = BST(num)
                    return
            
            else:
                # print(num1)
                temp.frequency += 1
                return

    
    def __init__(self, k: int, nums: List[int]):
        self.root = None
        self.k = k
        for i in nums:
            self.insert(i)
            # print("=====>")
        temp = self.root
        res = []
        self.inorder(res,temp)
        # print(self.k,"=====>")

    def add(self, val: int) -> int:
        temp = self.root
        res = []
        self.insert(val)
        self.inorder(res,self.root)
        index = min(self.k,len(res))
        return res[-index]
