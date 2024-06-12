"""Problem: https://leetcode.com/problems/fibonacci-number/description/"""


class Solution(object):
    def fib(self, n):
        f0 = 0
        f1 = 1
        for i in range(2,n):
            if i % 2 == 0:
                f0 = f0 + f1
            else:
                f1 = f0 + f1
        return f0 + f1 if n > 0 else 0

print(Solution().fib(0))
