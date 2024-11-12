from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        #expectedNums = []
        #for num in nums:
            #print(num)
        #    if num not in expectedNums:
        #        expectedNums.append(num)
        #print(expectedNums)
        #return len(expectedNums) #len(nums) - len(expectedNums)
        nums = list(dict.fromkeys(nums))
        print(nums)

        

        """
        i = 1
        while i<len(nums):
            i += 1
            print(i)
            if nums[i] == nums[i-1]:
                count += 1
            else:
                nums[i-count]=nums[i]
        print(i)


        print(nums)

        int count=0;
        for(int i=1;i<nums.size();i++){
            if(nums[i]==nums[i-1])
                count++;
            else
                nums[i-count]=nums[i];    
        }
        """
        #n = len(nums) - len(expectedNums)
        #a = [i for i in range(n)]
        

salution = Solution()
nums = [0,0,1,1,1,2,2,3,3,4]
result = salution.removeDuplicates(nums)
print(result)

