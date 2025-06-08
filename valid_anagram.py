# How it works:
# Sorts both strings into alphabetical order
# Compares the sorted results
# Anagrams will have identical sorted strings
# Time/Space Complexity:
# Time: O(n log n) due to sorting
# Space: O(n) for the sorted strings
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s=sorted(s)
        t=sorted(t)
        if s==t:
            return True
        else:
            return False
