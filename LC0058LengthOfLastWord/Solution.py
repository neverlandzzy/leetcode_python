"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 10^4
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    # Solution 1: built-in function
    # def lengthOfLastWord(self, s: str) -> int:
    #     return len(s.split().pop())

    # Solution 2:
    # def lengthOfLastWord(self, s: str) -> int:
    #     i = len(s) - 1
    #     j = i
    #     while i >= 0:
    #         if s[i] == " ":
    #             i -= 1
    #         else:
    #             j = i
    #             while j >= 0:
    #                 if s[j] != " ":
    #                     j -= 1
    #                 else:
    #                     break
    #
    #             break
    #
    #     return i - j

    # Solution 3: Easy to understand
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                counter += 1

            if counter > 0 and s[i] == " ":
                break

        return counter


    def run(self):
        print(self.lengthOfLastWord("Hello World"))
        print(self.lengthOfLastWord("   fly me   to   the moon  "))
        print(self.lengthOfLastWord("luffy is still joyboy"))


if __name__ == "__main__":
    Solution().run()
