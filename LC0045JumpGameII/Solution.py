"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        next_pos = 0
        max_pos = 0
        jump = 0
        n = len(nums)

        for i in range(0, n):
            if next_pos >= n - 1:
                return jump

            if max_pos < i:
                return -1
            max_pos = max(max_pos, i + nums[i])
            if next_pos == i:
                jump += 1
                next_pos = max_pos

        return jump

    def run(self):
        nums1 = [2, 3, 1, 1, 4]
        nums2 = [2, 3, 0, 1, 4]

        print(self.jump(nums1))
        print(self.jump(nums2))


if __name__ == "__main__":
    Solution().run()
