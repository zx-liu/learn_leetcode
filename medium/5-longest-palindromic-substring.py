"""
Given a string s, return the longest palindromic substring in s.
A string is palindromic if it reads the same forward and backward.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(string: str):
            if len(string) == 0 or len(string) == 1:
                return True

            middle: int = int(len(string) / 2)
            if len(string) % 2 == 0:
                first_half: str = string[:middle]
                second_half: str = string[middle:]

            else:
                first_half: str = string[:middle]
                second_half: str = string[middle + 1:]

            return first_half[::-1] == second_half

        current_max_len: int = 0
        current_max_substring: str = ""

        s_len: int = len(s)
        for i in range(s_len):
            # no need to continue if the rest of the string is short
            if i + current_max_len >= s_len:
                break

            # don't need to check strings that shorter than current max
            # append 1 letter at a time, until the end of string s
            for j in range(i + 1, s_len + 1):
                start_string = s[i:current_max_len + j]
                if is_palindrome(start_string):
                    current_max_substring = start_string

            current_max_len = len(current_max_substring)

        return current_max_substring
