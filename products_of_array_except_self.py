# How it works:
# For each position, remove the element temporarily
# Calculate product of remaining elements
# Restore the element and move to next position
# #Space/Time Complexity:
# Time complexity: O(n²) due to nested loops plus O(n) for pop() and insert()
# Space complexity: O(1) extra space (good!)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i=0
        
        for i in range(0, len(nums)):
            mult=1
            num = nums.pop(i)
            for j in nums:
                mult*=j
            res.append(mult)
            nums.insert(i,num)
        return res
