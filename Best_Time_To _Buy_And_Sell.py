class solution:
    def best_time(self , prices:list[int])->int:
        maxp = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
result = solution()
print(result.best_time([7,1,2,3,6,3]))
            
