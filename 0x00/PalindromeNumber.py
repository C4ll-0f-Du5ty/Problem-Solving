"""Problem: https://leetcode.com/problems/palindrome-number/description/"""

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
