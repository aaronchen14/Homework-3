# Given a string s, find the length of the longest substring without repeating characters.
# You can expect the string length is less than 100, and only contains English letters.
# Example 1: Input: s = "abcabcbb" Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Modify the “solution” class in question4.py, you may design your input to test it.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        input_size = len(s)
        unique_char = ""
        key_exiting = False
        for x in s:
            if x not in unique_char and key_exiting is False:
                unique_char += x
            else:
                key_exiting = True
        unique_size = len(unique_char)
        return unique_size


s_input = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s_input))
