class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(price)
            return 1
        
        copy = []
        days = 1
        while self.stack:
            if price >= self.stack[-1]:
                ele = self.stack.pop()
                copy.append(ele)
                days += 1 
            else:
                break
        
        self.stack.extend(copy)
        self.stack.append(price)
        # print(self.stack)
        return days
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)