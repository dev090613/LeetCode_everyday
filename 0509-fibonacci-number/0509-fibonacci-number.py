# 방법1: Recursion/ O(2^n), O(N)
class Solution:
    def fib(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1:
        #     return 1
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# 방법2: Bottom-Up Approach using Tabulation/ O(N), O(N)
# 방법3: Top-Down Approach using Memoization
# 방법4: Iterative Bottom-Up Approach
# 방법5: Matrix Exponentiation
# 방법6: Math