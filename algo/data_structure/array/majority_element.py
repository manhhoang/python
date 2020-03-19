# Time:  O(n)
# Space: O(1)
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution:

    @staticmethod
    def majority_element1(nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in range(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]

    @staticmethod
    def majority_element2(nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(collections.Counter(nums).items(), key=lambda a: a[1], reverse=True)[0][0]


if __name__ == "__main__":
    print(Solution.majority_element1([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))
    print(Solution.majority_element2([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))
