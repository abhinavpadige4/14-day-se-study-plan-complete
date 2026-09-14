"""
LeetCode 217: Contains Duplicate
Difficulty: Easy
Topics: Array, Hash Table

Problem:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9

Approach 1: Hash Set
We use a hash set to track elements we've seen. As we iterate through the array,
if we encounter an element that's already in the set, we return True.
Otherwise, we add the element to the set and continue.
Time Complexity: O(n) - We traverse the array once
Space Complexity: O(n) - In worst case, we store all elements in the set

Approach 2: Sorting
We sort the array first, then check adjacent elements for duplicates.
Time Complexity: O(n log n) - Due to sorting
Space Complexity: O(1) or O(n) - Depending on sorting algorithm space complexity

Approach 3: Brute Force
We compare each element with every other element.
Time Complexity: O(n^2) - Nested loops
Space Complexity: O(1) - No extra space used
"""

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """
    Check if array contains duplicates using hash set approach.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

def contains_duplicate_sorting(nums: List[int]) -> bool:
    """
    Check if array contains duplicates using sorting approach.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    # Sort the array
    nums.sort()
    
    # Check adjacent elements for duplicates
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    
    return False

def contains_duplicate_brute_force(nums: List[int]) -> bool:
    """
    Check if array contains duplicates using brute force approach.
    
    Args:
        nums: List of integers
        
    Returns:
        True if any value appears at least twice, False otherwise
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: nums = {nums1}")
    print(f"Hash set approach: {contains_duplicate(nums1)}")
    print(f"Sorting approach: {contains_duplicate_sorting(nums1)}")
    print(f"Brute force approach: {contains_duplicate_brute_force(nums1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    nums2 = [1, 2, 3, 4]
    print(f"Input: nums = {nums2}")
    print(f"Hash set approach: {contains_duplicate(nums2)}")
    print(f"Sorting approach: {contains_duplicate_sorting(nums2)}")
    print(f"Brute force approach: {contains_duplicate_brute_force(nums2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"Input: nums = {nums3}")
    print(f"Hash set approach: {contains_duplicate(nums3)}")
    print(f"Sorting approach: {contains_duplicate_sorting(nums3)}")
    print(f"Brute force approach: {contains_duplicate_brute_force(nums3)}")
    print(f"Expected: True")
    print()
    
    # Test case 4: Single element
    nums4 = [1]
    print(f"Input: nums = {nums4}")
    print(f"Hash set approach: {contains_duplicate(nums4)}")
    print(f"Sorting approach: {contains_duplicate_sorting(nums4)}")
    print(f"Brute force approach: {contains_duplicate_brute_force(nums4)}")
    print(f"Expected: False")
    print()
    
    # Test case 5: No duplicates
    nums5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Input: nums = {nums5}")
    print(f"Hash set approach: {contains_duplicate(nums5)}")
    print(f"Sorting approach: {contains_duplicate_sorting(nums5)}")
    print(f"Brute force approach: {contains_duplicate_brute_force(nums5)}")
    print(f"Expected: False")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Generate test data
    def generate_test_data(size, has_duplicates=True):
        if has_duplicates:
            # Create array with guaranteed duplicates
            base = list(range(size // 2))
            # Add duplicates by repeating some elements
            extra = [random.choice(base) for _ in range(size // 2)]
            return base + extra
        else:
            # Create array with no duplicates
            return list(range(size))
    
    # Test with duplicates (should return True early)
    test_with_dup = generate_test_data(50000, has_duplicates=True)
    # Shuffle to make duplicates appear randomly
    random.shuffle(test_with_dup)
    
    # Test without duplicates (worst case for all algorithms)
    test_without_dup = generate_test_data(50000, has_duplicates=False)
    
    print("Performance comparison with duplicates (early exit expected):")
    # Time hash set approach
    start_time = time.time()
    result1 = contains_duplicate(test_with_dup)
    hash_set_time = time.time() - start_time
    
    # Time sorting approach
    start_time = time.time()
    result2 = contains_duplicate_sorting(test_with_dup.copy())  # Copy to avoid modifying original
    sorting_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = contains_duplicate_brute_force(test_with_dup[:1000])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Hash set approach: {hash_set_time:.6f} seconds")
    print(f"Sorting approach: {sorting_time:.6f} seconds")
    print(f"Brute force approach (1000 elements): {brute_force_time:.6f} seconds")
    print(f"All returned: {result1} (should be True)")
    print()
    
    print("Performance comparison without duplicates (worst case):")
    # Time hash set approach
    start_time = time.time()
    result1 = contains_duplicate(test_without_dup)
    hash_set_time = time.time() - start_time
    
    # Time sorting approach
    start_time = time.time()
    result2 = contains_duplicate_sorting(test_without_dup.copy())
    sorting_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = contains_duplicate_brute_force(test_without_dup[:1000])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Hash set approach: {hash_set_time:.6f} seconds")
    print(f"Sorting approach: {sorting_time:.6f} seconds")
    print(f"Brute force approach (1000 elements): {brute_force_time:.6f} seconds")
    print(f"All returned: {result1} (should be False)")