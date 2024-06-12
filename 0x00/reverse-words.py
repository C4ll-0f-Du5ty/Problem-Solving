"""Problem: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/"""


class Solution(object):
    def reverseWords(self, s):
        words =s.split(" ")
        l = len(words)
        result = ""
        for w in words:
            l -= 1
            result += str(w)[::-1] + (" " if l > 0 else "")
        return(result)
        


print(Solution().reverseWords("Let's take LeetCode contest"))
print(Solution().reverseWords("Mr Ding"))
