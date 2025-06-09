# Algorithm Breakdown:
# Dictionary structure: defaultdict(list) automatically creates empty lists for new keys
# Frequency signature: Creates a 26-element array counting each letter (a-z)
# Character mapping: ord(c)-ord("a") converts 'a'→0, 'b'→1, etc.
# Grouping key: Uses tuple(count) as the dictionary key since lists aren't hashable
# Return format: res.values() returns all grouped anagram lists
# Time/Space Complexity:
# Time: O(n × m) where n = number of strings, m = average string length
# Space: O(n × m) for storing all strings and frequency arrays
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")] +=1
            res[tuple(count)].append(s)
        return res.values()
            
        
