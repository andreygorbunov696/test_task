from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #print(strs)
        m = min(strs, key=len)
        #print(type(m))
        result = []
        for x, i in enumerate(m):
            status = True
            print(i)
            for n in strs:
                print(n)
                if i != n[x]:
                    status = False
                    break
            print(status)
            print()
            if status:
                result.append(i)
            else:
                break
        result = "".join(result)
        #print(result)
        return result

sol = Solution()
strs = ["cir","car"]
print(sol.longestCommonPrefix(strs))