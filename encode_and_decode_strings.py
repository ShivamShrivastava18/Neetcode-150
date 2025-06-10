# Encoding Strategy:
# Format: "length#string" for each string
# Example: ["hello","world"] → "5#hello5#world"
# Why this works:
# Handles special characters: Strings can contain any characters (including "#")
# Empty strings: "" becomes "0#"
# No ambiguity: Length prefix tells you exactly how many characters to read
# Decoding Logic:
# Find the "#" delimiter to extract the length
# Read exactly that many characters after "#"
# Move pointer to start of next encoded string
# Time/Space Complexity:
# Encode: O(n) where n = total characters
# Decode: O(n)
# Space: O(n) for result storage


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) +"#"+s
        return res

    def decode(self, s: str) -> List[str]:
        res,i=[], 0
        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1 : j+1+length])
            i = j+1+length
        return res
