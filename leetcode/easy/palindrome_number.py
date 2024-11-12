class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        k = reversed(x)
        #for row in reversed(x):
        #    k += row

        print(x)
        print(str(k))
        if x == k:
            return True
        return False

salution = Solution()

print(salution.isPalindrome(313))