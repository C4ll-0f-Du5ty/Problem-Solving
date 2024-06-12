"""Problem: https://leetcode.com/problems/contains-duplicate/description/"""


class Solution(object):
    def containsDuplicate(self, nums):
        l = set()
        for i in nums:
            if i in l:
                return True
            l.add(i)
        return False


print(Solution().containsDuplicate([1,2,3,1]))
print(Solution().containsDuplicate([1,2,3,4]))
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
