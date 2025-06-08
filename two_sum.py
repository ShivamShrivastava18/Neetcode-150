# How it works:
# Use a dictionary to store {value: index} pairs as you iterate
# For each element, calculate the complement needed: diff = target - nums[i]
# Check if the complement exists in the hash map
# If found, return the stored index and current index
# If not found, store current element and its index
# Time/Space Complexity:
# Time: O(n) - single pass through the array
# Space: O(n) - hash map storage
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i in range (0,len(nums)):
            diff = target-nums[i]
            if diff in result:
                return [result[diff], i]
            else:
                result[nums[i]] = i
