"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:

1 <= s.length <= 1^4
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.


Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
"""

# Similar to LC186
class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words = []

        n = len(s)

        i = n - 1
        while i >= 0:
            if i >= 0 and s[i] == " ":
                i -= 1
            else:
                j = i
                while j > 0 and s[j - 1] != " ":
                    j -= 1

                if len(reversed_words) > 0:
                    reversed_words.append(" ")

                reversed_words.append(s[j: i + 1])
                i = j - 1

        return "".join(reversed_words)

    def run(self):
        print(self.reverseWords("the sky is blue"))
        print(self.reverseWords("  hello world  "))
        print(self.reverseWords("a good   example"))


if __name__ == "__main__":
    Solution().run()
