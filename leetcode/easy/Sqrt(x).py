class Solution:
    def mySqrt(self, x: int) -> int:
        print(x)
        print()
        k = 0
        n = 1
        result = 0
        while n < x:
            k += 1
            n = k * k 
            
            print(k, n)
        print()
        if n == x:
            return k
        return k - 1


sol = Solution()
x = 10
print(sol.mySqrt(x))