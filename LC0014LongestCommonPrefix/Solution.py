"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or not strs[0]:
            return ""
        common_prefix = []

        for i in range(0, len(strs[0])):
            for j in range(1, len(strs)):
                char = strs[0][i]
                if i >= len(strs[j]) or char != strs[j][i]:
                    return "".join(common_prefix)
            common_prefix.append(strs[0][i])

        return "".join(common_prefix)

    def run(self):
        strs1 = ["flower", "flow", "flight"]
        strs2 = ["dog", "racecar", "car"]

        print(self.longestCommonPrefix(strs1))
        print(self.longestCommonPrefix(strs2))


if __name__ == "__main__":
    Solution().run()
