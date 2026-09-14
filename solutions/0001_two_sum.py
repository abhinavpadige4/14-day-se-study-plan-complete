"""
LeetCode 1: Two Sum
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Approach:
We use a hash map to store the complement of each number (target - num) as we iterate through the array.
For each number, we check if it exists in our hash map. If it does, we've found our pair.
Otherwise, we store the complement of the current number for future lookup.

Time Complexity: O(n) - We traverse the list once, and each hash table operation is O(1) on average.
Space Complexity: O(n) - In the worst case, we store n elements in the hash map.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers in the array that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List containing indices of the two numbers that add up to target
    """
    # Hash map to store number -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement we need to reach target
        complement = target - num
        
        # If complement exists in our map, we found the solution
        if complement in num_map:
            return [num_map[complement], i]
        
        # Otherwise, store the current number's index for future lookup
        num_map[num] = i
    
    # According to problem constraints, we should always find a solution
    # This line should never be reached, but included for completeness
    return []

# Alternative brute force approach for comparison
def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach - O(n^2) time, O(1) space
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")
    print(f"Expected: [0, 1]")
    print()
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")
    print(f"Expected: [1, 2]")
    print()
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")
    print(f"Expected: [0, 1]")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Large test case for performance comparison
    large_nums = list(range(10000))
    large_target = 19999  # 9999 + 10000
    
    # Time the hash map approach
    start_time = time.time()
    result1 = two_sum(large_nums, large_target)
    hash_map_time = time.time() - start_time
    
    # Time the brute force approach (will be much slower)
    start_time = time.time()
    result2 = two_sum_brute_force(large_nums[:1000], large_target)  # Smaller array for brute force
    brute_force_time = time.time() - start_time
    
    print(f"Hash map approach time: {hash_map_time:.6f} seconds")
    print(f"Brute force approach time (1000 elements): {brute_force_time:.6f} seconds")
    print(f"Speed improvement: {brute_force_time/hash_map_time:.0f}x faster")