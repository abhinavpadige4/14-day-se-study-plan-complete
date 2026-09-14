"""
LeetCode 198: House Robber
Difficulty: Medium
Topics: Dynamic Programming, Array

Problem:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400

Approach: Dynamic Programming
Let dp[i] be the maximum amount of money that can be robbed from houses[0:i] (first i houses).
For each house i, we have two choices:
1. Rob house i: Then we cannot rob house i-1, so total = nums[i] + dp[i-2]
2. Skip house i: Then we can rob house i-1, so total = dp[i-1]
We choose the maximum of these two options.

Recurrence relation:
dp[i] = max(nums[i] + dp[i-2], dp[i-1])

Base cases:
- dp[0] = nums[0] (only one house)
- dp[1] = max(nums[0], nums[1]) (choose the richer of two houses)

Time Complexity: O(n) - Single pass through the array
Space Complexity: O(n) - DP array of size n
Can be optimized to O(1) space by only storing last two values.
"""

from typing import List

def rob(nums: List[int]) -> int:
    """
    Calculate maximum amount that can be robbed without alerting police.
    Uses optimized DP with O(1) space.
    
    Args:
        nums: List of money in each house
        
    Returns:
        Maximum amount that can be robbed
    """
    if not nums:
        return 0
    
    n = len(nums)
    
    # Handle base cases
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    # We only need to keep track of the last two values
    # prev2 = dp[i-2], prev1 = dp[i-1]
    prev2 = nums[0]                    # dp[0]
    prev1 = max(nums[0], nums[1])      # dp[1]
    
    # Calculate from house 2 to house n-1
    for i in range(2, n):
        # dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        current = max(nums[i] + prev2, prev1)
        # Shift values for next iteration
        prev2 = prev1
        prev1 = current
    
    return prev1

def rob_dp_array(nums: List[int]) -> int:
    """
    Calculate maximum amount that can be robbed using DP array.
    
    Args:
        nums: List of money in each house
        
    Returns:
        Maximum amount that can be robbed
    """
    if not nums:
        return 0
    
    n = len(nums)
    
    # Handle base cases
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
    
    # dp[i] = max amount that can be robbed from first i houses
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    return dp[-1]

def rob_brute_force(nums: List[int]) -> int:
    """
    Brute force approach using recursion - O(2^n) time, O(n) space (call stack).
    
    Args:
        nums: List of money in each house
        
    Returns:
        Maximum amount that can be robbed
    """
    def rob_from(index):
        if index >= len(nums):
            return 0
        # Either rob current house and skip next, or skip current house
        return max(
            nums[index] + rob_from(index + 2),  # Rob current house
            rob_from(index + 1)                 # Skip current house
        )
    
    return rob_from(0)

def rob_with_houses(nums: List[int]) -> tuple:
    """
    Calculate maximum amount and return which houses to rob.
    
    Args:
        nums: List of money in each house
        
    Returns:
        Tuple of (max_amount, list_of_house_indices_to_rob)
    """
    if not nums:
        return 0, []
    
    n = len(nums)
    
    if n == 1:
        return nums[0], [0]
    if n == 2:
        if nums[0] >= nums[1]:
            return nums[0], [0]
        else:
            return nums[1], [1]
    
    # dp[i] = max amount from first i houses
    dp = [0] * n
    # choice[i] = True if we rob house i, False otherwise
    choice = [False] * n
    
    dp[0] = nums[0]
    choice[0] = True
    
    dp[1] = max(nums[0], nums[1])
    choice[1] = nums[1] > nums[0]
    
    for i in range(2, n):
        rob_current = nums[i] + dp[i-2]
        skip_current = dp[i-1]
        
        if rob_current > skip_current:
            dp[i] = rob_current
            choice[i] = True
        else:
            dp[i] = skip_current
            choice[i] = False
    
    # Reconstruct the solution
    max_amount = dp[-1]
    houses_to_rob = []
    i = n - 1
    
    while i >= 0:
        if choice[i]:
            houses_to_rob.append(i)
            i -= 2  # Skip adjacent house
        else:
            i -= 1  # Move to previous house
    
    houses_to_rob.reverse()  # Reverse to get ascending order
    return max_amount, houses_to_rob

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Optimized DP (O(1) space): {rob(nums1)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums1)}")
    print(f"Brute force: {rob_brute_force(nums1)}")
    amount, houses = rob_with_houses(nums1)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums1[i] for i in houses]}")
    print(f"Expected: 4 (rob houses 0 and 2: 1 + 3)")
    print()
    
    # Test case 2
    nums2 = [2, 7, 9, 3, 1]
    print(f"Input: nums = {nums2}")
    print(f"Optimized DP (O(1) space): {rob(nums2)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums2)}")
    print(f"Brute force: {rob_brute_force(nums2)}")
    amount, houses = rob_with_houses(nums2)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums2[i] for i in houses]}")
    print(f"Expected: 12 (rob houses 0, 2, 4: 2 + 9 + 1)")
    print()
    
    # Test case 3
    nums3 = [2, 1, 1, 2]
    print(f"Input: nums = {nums3}")
    print(f"Optimized DP (O(1) space): {rob(nums3)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums3)}")
    print(f"Brute force: {rob_brute_force(nums3)}")
    amount, houses = rob_with_houses(nums3)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums3[i] for i in houses]}")
    print(f"Expected: 4 (rob houses 0 and 3: 2 + 2, or houses 1 and 2: 1 + 1)")
    print()
    
    # Test case 4: Single house
    nums4 = [5]
    print(f"Input: nums = {nums4}")
    print(f"Optimized DP (O(1) space): {rob(nums4)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums4)}")
    print(f"Brute force: {rob_brute_force(nums4)}")
    amount, houses = rob_with_houses(nums4)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums4[i] for i in houses]}")
    print(f"Expected: 5 (rob house 0)")
    print()
    
    # Test case 5: Two houses
    nums5 = [1, 3]
    print(f"Input: nums = {nums5}")
    print(f"Optimized DP (O(1) space): {rob(nums5)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums5)}")
    print(f"Brute force: {rob_brute_force(nums5)}")
    amount, houses = rob_with_houses(nums5)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums5[i] for i in houses]}")
    print(f"Expected: 3 (rob house 1)")
    print()
    
    # Test case 6: All zeros
    nums6 = [0, 0, 0, 0, 0]
    print(f"Input: nums = {nums6}")
    print(f"Optimized DP (O(1) space): {rob(nums6)}")
    print(f"DP array (O(n) space): {rob_dp_array(nums6)}")
    print(f"Brute force: {rob_brute_force(nums6)}")
    amount, houses = rob_with_houses(nums6)
    print(f"With houses: amount={amount}, rob houses {houses} = {[nums6[i] for i in houses]}")
    print(f"Expected: 0 (no money anywhere)")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Generate large test array (within constraints)
    large_nums = [random.randint(0, 400) for _ in range(10000)]
    
    # Time optimized DP approach
    start_time = time.time()
    result1 = rob(large_nums)
    optimized_time = time.time() - start_time
    
    # Time DP array approach
    start_time = time.time()
    result2 = rob_dp_array(large_nums)
    dp_array_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = rob_brute_force(large_nums[:20])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (10k elements):")
    print(f"Optimized DP (O(1) space): {optimized_time:.6f} seconds")
    print(f"DP array (O(n) space): {dp_array_time:.6f} seconds")
    print(f"Brute force approach (20 elements): {brute_force_time:.6f} seconds")
    print(f"DP approaches match: {result1 == result2}")
    print(f"Results reasonable: {0 <= result1 <= sum(large_nums)}")