from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        print(nums1, m, nums2, n)
        print(nums1[:m])
        print(nums2[:n])
        nums1 = sorted(nums1[:m] + nums2[:n])
        
        print(nums1)
sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
sol.merge(nums1, m, nums2, n)
