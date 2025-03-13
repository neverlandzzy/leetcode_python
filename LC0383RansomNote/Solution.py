"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.
"""

import collections

class Solution:

    # Solution 1: use built-in function to calculate chars
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # counter type, if key is missing, value is 0.
        chars = collections.Counter(magazine)
        for c in ransomNote:
            if chars[c] <= 0:
                return False
            chars[c] -= 1

        return True

    # Solution 2
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    #     chars = {}
    #
    #     for c in magazine:
    #         if c in chars:
    #             chars[c] += 1
    #         else:
    #             chars[c] = 1
    #     for c in ransomNote:
    #         if c not in chars:
    #             return False
    #         if chars[c] <= 0:
    #             return False
    #         chars[c] -= 1
    #
    #     return True

    def run(self):
        print(self.canConstruct("a", "b"))
        print(self.canConstruct("aa", "bb"))
        print(self.canConstruct("aa", "aab"))


if __name__ == "__main__":
    Solution().run()
