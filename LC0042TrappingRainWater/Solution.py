"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9


Constraints:

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        result = 0

        left = 0
        right = n - 1
        left_height = height[left]
        right_height = height[right]

        while left + 1 < right:
            if left_height < right_height:
                left += 1
                if left_height > height[left]:
                    result += left_height - height[left]
                else:
                    left_height = height[left]
            else:
                right -= 1
                if right_height > height[right]:
                    result += right_height - height[right]
                else:
                    right_height = height[right]

        return result

    def run(self):
        height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        height2 = [4, 2, 0, 3, 2, 5]

        print(self.trap(height1))
        print(self.trap(height2))


if __name__ == "__main__":
    Solution().run()
