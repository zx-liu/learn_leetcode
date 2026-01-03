"""
Given a string s, find the length of the longest substring without duplicate characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
from typing import Dict


class Solution:

    # basic version
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_len: int = len(s)

        i = 0
        # {char: index}
        current_string: Dict[str, int] = {}
        max_substring_len: int = -1
        while i < string_len:
            # current substring has hit repetition, stop
            if s[i] in current_string:
                # update max
                max_substring_len = max(len(current_string), max_substring_len)
                # reset pointer to the next character of the one in current string
                i = current_string[s[i]] + 1
                # reset substring
                current_string = {}
            else:
                # keep appending
                current_string[s[i]] = i
                i += 1

        # final check
        max_substring_len = max(len(current_string), max_substring_len)

        return max_substring_len
