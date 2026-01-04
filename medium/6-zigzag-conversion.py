"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
from typing import List


class Solution:
    # naive version
    def convert(self, s: str, numRows: int) -> str:
        # special easy case
        if numRows == 1:
            return s

        num_cols: int = len(s)
        zig_zag_pattern: List[List[str]] = [["" for _ in range(num_cols)] for _ in range(numRows)]

        # initial state. Pointer at (-1, 0) and movement is going down
        row: int = -1
        col: int = 0
        prev_move: str = "straight_down"

        for char in s:
            if prev_move == "straight_down":
                next_row: int = row + 1
                next_col: int = col

                # goes outside the 2D array
                if next_row == numRows:
                    next_row = row - 1
                    next_col = col + 1
                    prev_move = "diagonal_up"

            elif prev_move == "diagonal_up":
                next_row = row - 1
                next_col = col + 1

                if next_row < 0:
                    next_row: int = row + 1
                    next_col: int = col
                    prev_move = "straight_down"
            else:
                raise ValueError()

            row = next_row
            col = next_col

            zig_zag_pattern[row][col] = char

        return "".join(["".join(char_row) for char_row in zig_zag_pattern])

a = Solution()
a.convert("ABC", 1)