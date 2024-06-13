class solution:
    def contains_duplicate(self, nums:list[int])-> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
sol = solution()

print(sol.contains_duplicate([1,2,2,3,4,5]))
    
