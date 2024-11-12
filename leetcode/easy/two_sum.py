from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num_first in enumerate(nums):
            #print(i, num_first)
            for j, num_seccond in enumerate(nums):
                if i != j:
                    #print(j, num_seccond)
                    num_sum = num_first + num_seccond
                    if num_sum == target:
                        #print(num_sum)
                        #print([i, j])
                        return [i, j]

           # print() 



salution = Solution()

num = [2,7,11,15]
target = 9
print(salution.twoSum(num, target))