"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        n = len(nums)

        for i in range(0, n):
            max_jump = max(max_jump, i + nums[i])

            if max_jump >= n - 1:
                return True

            if max_jump <= i:
                return False

        return False

    def run(self):
        nums1 = [2, 3, 1, 1, 4]
        nums2 = [3, 2, 1, 0, 4]

        print(self.canJump(nums1))
        print(self.canJump(nums2))


if __name__ == "__main__":
    Solution().run()
