"""
LeetCode 53: Maximum Subarray
Difficulty: Easy
Topics: Array, Dynamic Programming, Greedy

Problem:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum = 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Approach: Kadane's Algorithm
We iterate through the array while maintaining two variables:
1. current_sum: Maximum sum ending at the current position
2. max_sum: Overall maximum sum found so far

At each element, we decide whether to:
- Start a new subarray at the current element, or
- Extend the previous subarray by including the current element

We choose whichever gives us a larger current_sum.

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(1) - Only using constant extra space
"""

from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Find the subarray with the largest sum using Kadane's algorithm.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
    
    # Initialize both to the first element
    max_sum = current_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for num in nums[1:]:
        # Either start new subarray at current element, or extend previous subarray
        current_sum = max(num, current_sum + num)
        # Update max_sum if current_sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_brute_force(nums: List[int]) -> int:
    """
    Brute force approach - O(n^3) time, O(1) space.
    Check all possible subarrays.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
    
    max_sum = float('-inf')
    n = len(nums)
    
    # Check all possible subarrays
    for i in range(n):
        for j in range(i, n):
            # Calculate sum of subarray nums[i:j+1]
            current_sum = sum(nums[i:j+1])
            max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_subarray_dp(nums: List[int]) -> int:
    """
    Dynamic Programming approach - O(n) time, O(n) space.
    dp[i] represents maximum subarray sum ending at index i.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
    
    n = len(nums)
    # dp[i] = max subarray sum ending at index i
    dp = [0] * n
    dp[0] = nums[0]
    
    for i in range(1, n):
        # Either start new subarray at i, or extend previous subarray
        dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    return max(dp)

def max_subarray_with_indices(nums: List[int]) -> tuple:
    """
    Find the subarray with the largest sum and return both sum and indices.
    
    Args:
        nums: List of integers
        
    Returns:
        Tuple of (max_sum, start_index, end_index)
    """
    if not nums:
        return 0, -1, -1
    
    max_sum = current_sum = nums[0]
    start = end = temp_start = 0
    
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            # Start new subarray at current position
            current_sum = nums[i]
            temp_start = i
        else:
            # Extend previous subarray
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: nums = {nums1}")
    print(f"Kadane's algorithm: {max_subarray(nums1)}")
    print(f"DP approach: {max_subarray_dp(nums1)}")
    print(f"Brute force approach: {max_subarray_brute_force(nums1)}")
    sum_val, start, end = max_subarray_with_indices(nums1)
    print(f"With indices: sum={sum_val}, subarray=[{start}:{end+1}] = {nums1[start:end+1]}")
    print(f"Expected: 6 (subarray [4,-1,2,1])")
    print()
    
    # Test case 2
    nums2 = [1]
    print(f"Input: nums = {nums2}")
    print(f"Kadane's algorithm: {max_subarray(nums2)}")
    print(f"DP approach: {max_subarray_dp(nums2)}")
    print(f"Brute force approach: {max_subarray_brute_force(nums2)}")
    sum_val, start, end = max_subarray_with_indices(nums2)
    print(f"With indices: sum={sum_val}, subarray=[{start}:{end+1}] = {nums2[start:end+1]}")
    print(f"Expected: 1 (subarray [1])")
    print()
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"Input: nums = {nums3}")
    print(f"Kadane's algorithm: {max_subarray(nums3)}")
    print(f"DP approach: {max_subarray_dp(nums3)}")
    print(f"Brute force approach: {max_subarray_brute_force(nums3)}")
    sum_val, start, end = max_subarray_with_indices(nums3)
    print(f"With indices: sum={sum_val}, subarray=[{start}:{end+1}] = {nums3[start:end+1]}")
    print(f"Expected: 23 (subarray [5,4,-1,7,8])")
    print()
    
    # Test case 4: All negative numbers
    nums4 = [-2, -1, -3]
    print(f"Input: nums = {nums4}")
    print(f"Kadane's algorithm: {max_subarray(nums4)}")
    print(f"DP approach: {max_subarray_dp(nums4)}")
    print(f"Brute force approach: {max_subarray_brute_force(nums4)}")
    sum_val, start, end = max_subarray_with_indices(nums4)
    print(f"With indices: sum={sum_val}, subarray=[{start}:{end+1}] = {nums4[start:end+1]}")
    print(f"Expected: -1 (subarray [-1])")
    print()
    
    # Test case 5: All positive numbers
    nums5 = [1, 2, 3, 4, 5]
    print(f"Input: nums = {nums5}")
    print(f"Kadane's algorithm: {max_subarray(nums5)}")
    print(f"DP approach: {max_subarray_dp(nums5)}")
    print(f"Brute force approach: {max_subarray_brute_force(nums5)}")
    sum_val, start, end = max_subarray_with_indices(nums5)
    print(f"With indices: sum={sum_val}, subarray=[{start}:{end+1}] = {nums5[start:end+1]}")
    print(f"Expected: 15 (subarray [1,2,3,4,5])")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Generate large test array with mix of positive and negative numbers
    large_nums = [random.randint(-1000, 1000) for _ in range(100000)]
    
    # Time Kadane's algorithm
    start_time = time.time()
    result1 = max_subarray(large_nums)
    kadane_time = time.time() - start_time
    
    # Time DP approach
    start_time = time.time()
    result2 = max_subarray_dp(large_nums)
    dp_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = max_subarray_brute_force(large_nums[:100])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (100k elements):")
    print(f"Kadane's algorithm: {kadane_time:.6f} seconds")
    print(f"DP approach: {dp_time:.6f} seconds")
    print(f"Brute force approach (100 elements): {brute_force_time:.6f} seconds")
    print(f"Kadane's and DP results match: {result1 == result2}")
    print(f"Results are reasonable: {-1000*len(large_nums) <= result1 <= 1000*len(large_nums)}")