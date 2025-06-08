(* Uses a list to track seen elements
Time complexity: O(n²) - because i in dupl is O(n) for each element
Space complexity: O(n) *)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupl = []
        for i in nums:
            if i in dupl:
                return True
            else:
                dupl.append(i)
        return False
            
        
