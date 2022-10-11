# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Modify the “solution” function in the question8.py. (Analyze your time complexity)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        else:
            return False


s1 = "anagram"
t1 = "nagaram"
output1 = Solution().isAnagram(s1, t1)
s2 = "rat"
t2 = "car"
output2 = Solution().isAnagram(s2, t2)
print(output1)
print(output2)
# Since the string is only examined once, the time complexity is O(n).
