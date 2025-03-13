"""
Given a character array s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.

Your code must solve the problem in-place, i.e. without allocating extra space.



Example 1:

Input: s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
Example 2:

Input: s = ["a"]
Output: ["a"]


Constraints:

1 <= s.length <= 10^5
s[i] is an English letter (uppercase or lowercase), digit, or space ' '.
There is at least one word in s.
s does not contain leading or trailing spaces.
All the words in s are guaranteed to be separated by a single space.
"""
from typing import List

# Similar to LC151
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[::] = s[::-1]
        n = len(s)
        start = 0
        for i in range(0, n + 1):
            if i == n or s[i] == " ":
                s[start:i] = s[start:i][::-1]
                start = i + 1


    def run(self):
        s1 = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
        s2 = ["a"]

        self.reverseWords(s1)
        self.reverseWords(s2)

        print(s1)
        print(s2)


if __name__ == "__main__":
    Solution().run()
