class solution:
    def union(self,a,b):
        unionset = set(a+b)
        return unionset
sol = solution()
print(sol.union([1,2,3,4,5],[1,2,6,7,8]))
