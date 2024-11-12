class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
        #if needle in haystack:
        #    return 0
        #return -1

sol = Solution()
haystack = "hello"
needle = "ll"
print(sol.strStr(haystack, needle))