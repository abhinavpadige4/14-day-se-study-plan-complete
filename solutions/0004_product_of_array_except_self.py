"""
LeetCode 238: Product of Array Except Self
Difficulty: Medium
Topics: Array, Prefix Sum

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
- 2 <= nums.length <= 10^5
- -30 <= nums[i] <= 30
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Approach: Prefix and Suffix Products
We can solve this in O(n) time without division by using two passes:
1. First pass (left to right): Calculate prefix products - product of all elements to the left of each index
2. Second pass (right to left): Calculate suffix products - product of all elements to the right of each index
3. Result: For each index, answer[i] = prefix[i] * suffix[i]

To optimize space, we can use the output array to store prefix products first,
then multiply by suffix products in the second pass.

Time Complexity: O(n) - Two passes through the array
Space Complexity: O(1) excluding the output array, or O(n) including it
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    """
    Calculate product of array except self using prefix/suffix approach.
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is product of all elements except the one at that index
    """
    n = len(nums)
    # Initialize result array with 1s
    result = [1] * n
    
    # First pass: calculate prefix products and store in result
    # result[i] will contain product of all elements to the left of i
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Second pass: multiply by suffix products
    # We'll traverse from right to left, maintaining suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

def product_except_self_with_division(nums: List[int]) -> List[int]:
    """
    Alternative approach using division (not allowed per problem constraints,
    but included for educational purposes).
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is product of all elements except the one at that index
    """
    # Calculate total product
    total_product = 1
    zero_count = 0
    
    for num in nums:
        if num == 0:
            zero_count += 1
        else:
            total_product *= num
    
    # Handle cases with zeros
    if zero_count > 1:
        # More than one zero means all products will be zero
        return [0] * len(nums)
    elif zero_count == 1:
        # Exactly one zero means only position with zero gets non-zero product
        result = []
        for num in nums:
            if num == 0:
                result.append(total_product)
            else:
                result.append(0)
        return result
    else:
        # No zeros, we can safely divide
        return [total_product // num for num in nums]

def product_except_self_brute_force(nums: List[int]) -> List[int]:
    """
    Brute force approach - O(n^2) time, O(1) space (excluding output).
    
    Args:
        nums: List of integers
        
    Returns:
        List where each element is product of all elements except the one at that index
    """
    n = len(nums)
    result = []
    
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        result.append(product)
    
    return result

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 4]
    print(f"Input: nums = {nums1}")
    print(f"Prefix/suffix approach: {product_except_self(nums1)}")
    print(f"Division approach: {product_except_self_with_division(nums1)}")
    print(f"Brute force approach: {product_except_self_brute_force(nums1)}")
    print(f"Expected: [24, 12, 8, 6]")
    print()
    
    # Test case 2
    nums2 = [-1, 1, 0, -3, 3]
    print(f"Input: nums = {nums2}")
    print(f"Prefix/suffix approach: {product_except_self(nums2)}")
    print(f"Division approach: {product_except_self_with_division(nums2)}")
    print(f"Brute force approach: {product_except_self_brute_force(nums2)}")
    print(f"Expected: [0, 0, 9, 0, 0]")
    print()
    
    # Test case 3: All zeros
    nums3 = [0, 0, 0, 0]
    print(f"Input: nums = {nums3}")
    print(f"Prefix/suffix approach: {product_except_self(nums3)}")
    print(f"Division approach: {product_except_self_with_division(nums3)}")
    print(f"Brute force approach: {product_except_self_brute_force(nums3)}")
    print(f"Expected: [0, 0, 0, 0]")
    print()
    
    # Test case 4: Single zero
    nums4 = [0, 1, 2, 3]
    print(f"Input: nums = {nums4}")
    print(f"Prefix/suffix approach: {product_except_self(nums4)}")
    print(f"Division approach: {product_except_self_with_division(nums4)}")
    print(f"Brute force approach: {product_except_self_brute_force(nums4)}")
    print(f"Expected: [6, 0, 0, 0]")
    print()
    
    # Test case 5: Negative numbers
    nums5 = [-2, -3, -4]
    print(f"Input: nums = {nums5}")
    print(f"Prefix/suffix approach: {product_except_self(nums5)}")
    print(f"Division approach: {product_except_self_with_division(nums5)}")
    print(f"Brute force approach: {product_except_self_brute_force(nums5)}")
    print(f"Expected: [12, 8, 6]")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Generate large test array
    large_nums = [random.randint(-10, 10) for _ in range(100000)]
    
    # Time the prefix/suffix approach
    start_time = time.time()
    result1 = product_except_self(large_nums)
    prefix_suffix_time = time.time() - start_time
    
    # Time the division approach (for comparison)
    start_time = time.time()
    result2 = product_except_self_with_division(large_nums)
    division_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = product_except_self_brute_force(large_nums[:100])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (100k elements):")
    print(f"Prefix/suffix approach: {prefix_suffix_time:.6f} seconds")
    print(f"Division approach: {division_time:.6f} seconds")
    print(f"Brute force approach (100 elements): {brute_force_time:.6f} seconds")
    print(f"First 5 results match: {result1[:5] == result2[:5] == result3[:5]}")
    print(f"All results non-negative: {all(x >= 0 for x in result1[:10])}")  # Just checking first 10