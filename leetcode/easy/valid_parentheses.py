class Solution:
    def isValid(self, s: str) -> bool:
        symbols = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for i in s:
            print(i)
            if i not in symbols:
                stack.append(i)
            else:
                if stack[-1] == symbols[i]:
                    stack.pop()
                else:
                    return False
        return not stack

sol = Solution()
s = "()[]{}"
print(sol.isValid(s))
print()


