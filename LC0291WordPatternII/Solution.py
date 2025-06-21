"""
Given a pattern and a string s, return true if s matches the pattern.

A string s matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.



Example 1:

Input: pattern = "abab", s = "redblueredblue"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "red"
'b' -> "blue"
Example 2:

Input: pattern = "aaaa", s = "asdasdasdasd"
Output: true
Explanation: One possible mapping is as follows:
'a' -> "asd"
Example 3:

Input: pattern = "aabb", s = "xyzabcxzyabc"
Output: false


Constraints:

1 <= pattern.length, s.length <= 20
pattern and s consist of only lowercase English letters.
"""


class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        mapping = {}
        used_strings = set()
        return self.helper(pattern, s, mapping, used_strings, 0, 0)

    def helper(self, pattern: str, s: str, mapping: dict, used_strings: set, str_index: int, pattern_index: int) -> bool:
        if str_index == len(s) and pattern_index == len(pattern):
            return True
        if str_index == len(s) or pattern_index == len(pattern):
            return False

        c = pattern[pattern_index]
        if c in mapping:
            matched = mapping[c]
            if not s.startswith(matched, str_index):
                return False
            return self.helper(pattern, s, mapping, used_strings, str_index + len(matched), pattern_index + 1)

        for i in range(str_index, len(s)):
            matched = s[str_index: i + 1]
            if matched in used_strings:
                continue

            mapping[c] = matched
            used_strings.add(matched)

            if self.helper(pattern, s, mapping, used_strings, i + 1, pattern_index + 1):
                return True

            del mapping[c]
            used_strings.remove(matched)

        return False


    def run(self):
        print(self.wordPatternMatch("abab", "redblueredblue"))
        print(self.wordPatternMatch("aaaa", "asdasdasdasd"))
        print(self.wordPatternMatch("aabb", "xyzabcxzyabc"))


if __name__ == "__main__":
    Solution().run()
