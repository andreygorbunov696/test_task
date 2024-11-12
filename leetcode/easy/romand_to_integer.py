class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        n = table.get(s[-1])
        result = 0
        for i in reversed(s):
            if table.get(i) < n:
                result -= table.get(i)
            else:
                result += table.get(i)
            n = table.get(i)
        return result

sol = Solution()
print(sol.romanToInt('III'))