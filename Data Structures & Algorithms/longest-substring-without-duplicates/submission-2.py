class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        maxl = 0
        start = 0

        for i in range(len(s)):
            if s[i] in chars and chars[s[i]] >= start:
                start = chars[s[i]] + 1
            chars[s[i]] = i
            maxl = max(maxl, i - start + 1)
        return maxl
