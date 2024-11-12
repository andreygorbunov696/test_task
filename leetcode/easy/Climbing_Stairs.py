

class Solution:
    def climbStairs(self, n: int) -> int:
        def fibonacci_iterative(x):
            if x <= 0:
                return 0
            elif x == 1:
                return 1
            
            a, b = 0, 1
            for _ in range(2, x + 1):
                a, b = b, a + b
            return b
        
        return fibonacci_iterative(n+1)

sol = Solution()
n = 4
print(sol.climbStairs(n))

"""def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Пример использования
print(fibonacci_iterative(10))  # Вывод: 55"""