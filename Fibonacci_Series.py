class solution:
    def fibonacci(self, n:int)->int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        ans = [0,1]
        for i in range(2 , n+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans
sol = solution()
print(sol.fibonacci(6))
