"""Problem: https://leetcode.com/problems/add-binary/description/"""


class Solution(object):
    def addBinary(self, a, b):
        m = max(len(a), len(b))
        a = a.zfill(m)[::-1]
        b = b.zfill(m)[::-1]

        result = ""
        carry = "0"
        for i, j in zip(b, a):
            x = int(j) + int(i) + int(carry)
            if 0 < x < 2:
                result += '1'
                carry = '0'
            elif x == 0:
                result += '0'
            elif x % 2 == 0:
                result += '0'
                carry = '1'
            else:
                result += '1'
                carry = '1'
        if carry == '1':
            result += '1'
        return result[::-1]

print(Solution().addBinary("11", "1"))
print(Solution().addBinary("1010", "1011"))
print(Solution().addBinary("0", "0"))
