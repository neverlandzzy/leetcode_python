"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display
this pattern in a fixed font for better legibility)

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

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines = [[] for _ in range(numRows)]

        i = 0
        n = len(s)
        while i < n:
            for k in range(0, numRows):
                if i < n:
                    lines[k].append(s[i])
                    i += 1

            for k in range(numRows - 2, 0, -1):
                if i < n:
                    lines[k].append(s[i])
                    i += 1
        for j in range(1, len(lines)):
            lines[0].extend(lines[j])
        return "".join(lines[0])

    def run(self):
        print(self.convert("PAYPALISHIRING", 3))
        print(self.convert("PAYPALISHIRING", 4))
        print(self.convert("A", 1))


if __name__ == "__main__":
    Solution().run()
