class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        for i in reversed(s):
            
            if i == '':
                print(i, False)
            else:
                return len(i)
        return False
        return len(s.split(' ')[-1])

sol = Solution()
s = '   fly me   to   the moon  '
print(sol.lengthOfLastWord(s))