"""Problem: https://leetcode.com/problems/plus-one/description/"""


class Solution(object):
    def plusOne(self, digits):
        s = ""
        for d in digits:
            s += str(d)
        s = str(int(s) + 1)
        return list(int(c) for c in s)

print(Solution().plusOne([3, 9]))
