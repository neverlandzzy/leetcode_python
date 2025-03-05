"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-10^9 <= nums[i] <= 10^9


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        major = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == major:
                count += 1
            else:
                if count == 0:
                    major = nums[i]
                    count = 1
                else:
                    count -= 1

        return major

    def run(self):
        nums1 = [3, 2, 3]
        nums2 = [2, 2, 1, 1, 1, 2, 2]

        print(self.majorityElement(nums1))
        print(self.majorityElement(nums2))


if __name__ == "__main__":
    Solution().run()
