"""Problem: https://leetcode.com/problems/base-7/description/"""


class Solution(object):
    def convertToBase7(self, num):
        temp = abs(num)
        result = ""
        while(True):
            if(temp < 7):
                result += str(temp)
                break
            result += str(temp % 7)
            temp //= 7
        if num < 0:
            result += '-'
        return result[::-1]


print(Solution().convertToBase7(100))
print(Solution().convertToBase7(-7))
print(Solution().convertToBase7(-3))
