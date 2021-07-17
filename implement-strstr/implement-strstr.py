class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == None:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1