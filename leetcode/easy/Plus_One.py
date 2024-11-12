from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #len_digits = len(digits)
        #digits = "".join(str(element) for element in digits)        
        #return list(str(int(digits) + 1))
        multiplier = 1
        num = 0 
        for digit in reversed(digits):
            digit = digit * multiplier
            num = num + digit
            multiplier *= 10
            #print(digit)
            #print(multiplier)
        #print()
        #print(num + 1)
        #print(list(str(num+1)))
        return [int(x) for x in str(num+1)]#list(str(num+1))


sol = Solution()
digits = [9]
print(sol.plusOne(digits))