class solution:
    def rotate(self, nums:list[int],k:int)->None:
        n = len(nums)
        rotated_array = [0] * n
        for i in range(n):
            rotated_array[(i+k)% n] = nums[i]
        nums[:] = rotated_array[:]
        return nums[:]
        
sol = solution()
print(sol.rotate([1,2,23,3,4,5,6,7],3))
