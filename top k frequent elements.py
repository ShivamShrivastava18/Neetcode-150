# How it works:
# Frequency counting: res[n] = 1 + res.get(n,0) builds a frequency map
# Min-heap: Maintains only the k most frequent elements
# Size control: When heap exceeds k elements, removes the least frequent
# Result extraction: Returns the numbers from the final heap

# Time/Space Complexity:
# Time: O(n log k) where n = array length
# Space: O(n) for frequency map + O(k) for heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        count = 0
        for n in nums:
            res[n] = 1+ res.get(n,0)
        heap=[]
        for num, freq in res.items():
            heapq.heappush(heap, (freq, num))
            if len(heap)>k:
                heapq.heappop(heap)
        return [num for freq, num in heap]
