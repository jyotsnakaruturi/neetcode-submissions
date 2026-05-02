from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)  # Convert list to set for O(1) lookup
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:  # Only start counting from the smallest number in a sequence
                length = 1
                current = num

                while current + 1 in num_set:  # Expand sequence
                    current += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length
