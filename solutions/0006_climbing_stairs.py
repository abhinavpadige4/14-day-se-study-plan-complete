"""
LeetCode 70: Climbing Stairs
Difficulty: Easy
Topics: Dynamic Programming, Memoization, Fibonacci

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45

Approach: Dynamic Programming
This problem follows the Fibonacci sequence pattern.
Let dp[i] be the number of ways to reach step i.
We can reach step i from either:
- Step i-1 (taking 1 step), or
- Step i-2 (taking 2 steps)
So: dp[i] = dp[i-1] + dp[i-2]

Base cases:
- dp[0] = 1 (one way to stay at ground level)
- dp[1] = 1 (one way to reach first step)
- dp[2] = 2 (two ways: 1+1 or 2)

Time Complexity: O(n) - Single pass to fill dp array
Space Complexity: O(n) - DP array of size n+1
Can be optimized to O(1) space by only storing last two values.
"""

from typing import List

def climb_stairs(n: int) -> int:
    """
    Calculate distinct ways to climb stairs using optimized DP (O(1) space).
    
    Args:
        n: Number of steps to climb
        
    Returns:
        Number of distinct ways to reach the top
    """
    if n <= 2:
        return n
    
    # We only need to keep track of the last two values
    # a = dp[i-2], b = dp[i-1]
    a, b = 1, 2
    
    # Calculate from step 3 to step n
    for _ in range(3, n + 1):
        # dp[i] = dp[i-1] + dp[i-2]
        a, b = b, a + b
    
    return b

def climb_stairs_dp_array(n: int) -> int:
    """
    Calculate distinct ways to climb stairs using DP array (O(n) space).
    
    Args:
        n: Number of steps to climb
        
    Returns:
        Number of distinct ways to reach the top
    """
    if n <= 2:
        return n
    
    # dp[i] = number of ways to reach step i
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: 1 way to stay at ground
    dp[1] = 1  # Base case: 1 way to reach first step
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]

def climb_stairs_memoization(n: int) -> int:
    """
    Calculate distinct ways to climb stairs using memoization (top-down DP).
    
    Args:
        n: Number of steps to climb
        
    Returns:
        Number of distinct ways to reach the top
    """
    memo = {}
    
    def dfs(steps):
        if steps in memo:
            return memo[steps]
        if steps <= 2:
            return steps
        
        memo[steps] = dfs(steps - 1) + dfs(steps - 2)
        return memo[steps]
    
    return dfs(n)

def climb_stairs_brute_force(n: int) -> int:
    """
    Calculate distinct ways to climb stairs using brute force recursion.
    Exponential time complexity - only for small n.
    
    Args:
        n: Number of steps to climb
        
    Returns:
        Number of distinct ways to reach the top
    """
    if n <= 2:
        return n
    return climb_stairs_brute_force(n - 1) + climb_stairs_brute_force(n - 2)

# Test cases
if __name__ == "__main__":
    # Test case 1
    n1 = 2
    print(f"Input: n = {n1}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n1)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n1)}")
    print(f"Memoization: {climb_stairs_memoization(n1)}")
    print(f"Brute force: {climb_stairs_brute_force(n1)}")
    print(f"Expected: 2")
    print()
    
    # Test case 2
    n2 = 3
    print(f"Input: n = {n2}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n2)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n2)}")
    print(f"Memoization: {climb_stairs_memoization(n2)}")
    print(f"Brute force: {climb_stairs_brute_force(n2)}")
    print(f"Expected: 3")
    print()
    
    # Test case 3
    n3 = 5
    print(f"Input: n = {n3}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n3)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n3)}")
    print(f"Memoization: {climb_stairs_memoization(n3)}")
    print(f"Brute force: {climb_stairs_brute_force(n3)}")
    print(f"Expected: 8")
    print()
    
    # Test case 4
    n4 = 10
    print(f"Input: n = {n4}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n4)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n4)}")
    print(f"Memoization: {climb_stairs_memoization(n4)}")
    print(f"Brute force: {climb_stairs_brute_force(n4)}")
    print(f"Expected: 89")
    print()
    
    # Test case 5: Edge case
    n5 = 1
    print(f"Input: n = {n5}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n5)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n5)}")
    print(f"Memoization: {climb_stairs_memoization(n5)}")
    print(f"Brute force: {climb_stairs_brute_force(n5)}")
    print(f"Expected: 1")
    print()
    
    # Test case 6: Larger value
    n6 = 45  # Maximum constraint
    print(f"Input: n = {n6}")
    print(f"Optimized DP (O(1) space): {climb_stairs(n6)}")
    print(f"DP array (O(n) space): {climb_stairs_dp_array(n6)}")
    print(f"Memoization: {climb_stairs_memoization(n6)}")
    # Skip brute force for n=45 as it would take too long
    print(f"Brute force: Skipped (too slow for n=45)")
    print(f"Expected: 1836311903")
    print()
    
    # Performance comparison
    import time
    
    # Test with medium-sized input
    test_n = 40
    
    # Time optimized DP approach
    start_time = time.time()
    result1 = climb_stairs(test_n)
    optimized_time = time.time() - start_time
    
    # Time DP array approach
    start_time = time.time()
    result2 = climb_stairs_dp_array(test_n)
    dp_array_time = time.time() - start_time
    
    # Time memoization approach
    start_time = time.time()
    result3 = climb_stairs_memoization(test_n)
    memoization_time = time.time() - start_time
    
    # Time brute force approach (will be slow for n=40)
    start_time = time.time()
    result4 = climb_stairs_brute_force(test_n)
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (n={test_n}):")
    print(f"Optimized DP (O(1) space): {optimized_time:.6f} seconds")
    print(f"DP array (O(n) space): {dp_array_time:.6f} seconds")
    print(f"Memoization: {memoization_time:.6f} seconds")
    print(f"Brute force: {brute_force_time:.6f} seconds")
    print(f"All DP approaches match: {result1 == result2 == result3}")
    print(f"Brute force matches DP: {result1 == result4}")