class solution:
    def climb(self, n:int)->int:
        one,two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one

sol = solution()
print(sol.climb(8))
            
