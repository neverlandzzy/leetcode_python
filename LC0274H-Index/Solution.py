"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.



Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
Example 2:

Input: citations = [1,3,1]
Output: 1


Constraints:

n == citations.length
1 <= n <= 5000
0 <= citations[i] <= 1000
"""

from typing import List


class Solution:
    # Solution 1: Sort, Time: O(nlogn), Space: O(1)
    # def hIndex(self, citations: List[int]) -> int:
    #     citations.sort()
    #     n = len(citations)
    #
    #     for i in range(0, n):
    #         if citations[i] >= n - i:
    #             return n - i
    #
    #     return 0

    # Solution 2: Bucket Sort, Time: O(n), Space: O(n)
    # e.g. 3, 0, 6, 1, 5
    # bucket: index: 0, 1, 2, 3, 4, 5
    #         val:   1, 1, 0, 1, 0, 2

    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)

        for c in citations:
            if c >= n:
                buckets[n] += 1
            else:
                buckets[c] += 1

        sum = 0

        for i in range(n, -1, -1):
            sum += buckets[i]
            if sum >= i:
                return i

        return 0

    def run(self):
        citations1 = [3, 0, 6, 1, 5]
        citations2 = [1, 3, 1]

        print(self.hIndex(citations1))
        print(self.hIndex(citations2))


if __name__ == "__main__":
    Solution().run()
