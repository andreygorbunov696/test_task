from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        print(s)
        print(indices)
        result = ''
        temp = {}
        for x, i in enumerate(indices):
            temp[str(i)] = s[x]
        for i in sorted(indices):
            result += temp[str(i)]
        print(result)

sol = Solution()
s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
sol.restoreString(s, indices)