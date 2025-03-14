"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        index = 0
        len_h = len(haystack)
        len_n = len(needle)

        while i < len_h and j < len_n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = 0
                index += 1
                i = index

        return index if j == len_n else -1

    def run(self):
        print(self.strStr("sadbutsad", "sad"))
        print(self.strStr("leetcode", "leeto"))


if __name__ == "__main__":
    Solution().run()
