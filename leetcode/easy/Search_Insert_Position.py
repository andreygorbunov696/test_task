from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            index = nums.index(target)
            return index
        except:
            nums.append(target)
            nums = sorted(nums)
            index = nums.index(target)
            return index

sol = Solution()
nums = [1,3,5,6]
target = 2
print(sol.searchInsert(nums, target))