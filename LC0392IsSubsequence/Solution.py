"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false


Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.


Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 10^9, and you want to check one by one to
see if t has its subsequence. In this scenario, how would you change your code?
"""


class Solution:
    # Solution 1: Time: O(|T|), |T| is the length of the target string
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        n1 = len(s)
        n2 = len(t)

        if n1 > n2:
            return False

        while i < n1 and j < n2:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

            if j == n2:
                break

        return i == n1

    def run(self):
        print(self.isSubsequence("abc", "ahbgdc"))
        print(self.isSubsequence("axc", "ahbgdc"))


if __name__ == "__main__":
    Solution().run()
