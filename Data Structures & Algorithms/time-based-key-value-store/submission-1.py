class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        all_values = self.hashmap[key]
        low = 0
        high = len(all_values)-1
        sol = float("-inf")

        while(low<=high):
            mid = (high+low)//2
            if(all_values[mid][0]<=timestamp):
                sol = max(mid,sol)
                low=mid+1
            else:
                high = mid-1
            

        return "" if sol == float("-inf") else all_values[sol][-1]