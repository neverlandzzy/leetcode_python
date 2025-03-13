"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.


Example 1:

Input: pattern = "abba", s = "dog cat cat dog"

Output: true

Explanation:

The bijection can be established as:

'a' maps to "dog".
'b' maps to "cat".
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"

Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"

Output: false



Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""

# Related to LC291

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        str_lst = s.split()
        if len(pattern) != len(str_lst):
            return False

        pattern_to_str = {}
        str_to_pattern = {}

        for i in range(0, len(pattern)):
            if pattern[i] not in pattern_to_str:
                if str_lst[i] in str_to_pattern:
                    return False
                pattern_to_str[pattern[i]] = str_lst[i]
                str_to_pattern[str_lst[i]] = pattern[i]
            else:
                if pattern_to_str[pattern[i]] != str_lst[i] or str_to_pattern[str_lst[i]] != pattern[i]:
                    return False

        return True

    def run(self):
        print(self.wordPattern("abba", "dog cat cat dog"))
        print(self.wordPattern("abba", "dog cat cat fish"))
        print(self.wordPattern("aaaa", "dog cat cat dog"))
        print(self.wordPattern("abba", "dog dog dog dog"))


if __name__ == "__main__":
    Solution().run()
