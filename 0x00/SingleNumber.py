"""Problem: https://leetcode.com/problems/single-number/description/ """


class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for j in nums:
            result ^= j
        print(result)


Solution().singleNumber([2,2,1])
Solution().singleNumber([4,1,2,1,2])
Solution().singleNumber([1])
Solution().singleNumber([1, 7, 2, 6, 7, 1, 2])
