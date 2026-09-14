"""
LeetCode 242: Valid Anagram
Difficulty: Easy
Topics: Hash Table, String, Sorting

Problem:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Approach 1: Sorting
We can sort both strings and compare them. If they are equal after sorting, they are anagrams.
Time Complexity: O(n log n) where n is the length of the strings
Space Complexity: O(log n) or O(n) depending on the sorting algorithm

Approach 2: Hash Table (Counter)
We count the frequency of each character in both strings and compare the counts.
If all character counts match, the strings are anagrams.
Time Complexity: O(n) - We traverse each string once
Space Complexity: O(1) - Since we only store counts for 26 lowercase English letters
"""

from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s using hash table approach.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    # Early exit if lengths are different
    if len(s) != len(t):
        return False
    
    # Count characters in both strings
    count_s = Counter(s)
    count_t = Counter(t)
    
    # Compare the counts
    return count_s == count_t

def is_anagram_sorting(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s using sorting approach.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    # Early exit if lengths are different
    if len(s) != len(t):
        return False
    
    # Sort both strings and compare
    return sorted(s) == sorted(t)

def is_anagram_array(s: str, t: str) -> bool:
    """
    Check if t is an anagram of s using fixed-size array approach.
    Most efficient for lowercase English letters.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if t is an anagram of s, False otherwise
    """
    # Early exit if lengths are different
    if len(s) != len(t):
        return False
    
    # Create frequency array for 26 lowercase letters
    freq = [0] * 26
    
    # Increment for characters in s, decrement for characters in t
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
        freq[ord(t[i]) - ord('a')] -= 1
    
    # Check if all frequencies are zero
    return all(count == 0 for count in freq)

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Input: s = '{s1}', t = '{t1}'")
    print(f"Hash map approach: {is_anagram(s1, t1)}")
    print(f"Sorting approach: {is_anagram_sorting(s1, t1)}")
    print(f"Array approach: {is_anagram_array(s1, t1)}")
    print(f"Expected: True")
    print()
    
    # Test case 2
    s2 = "rat"
    t2 = "car"
    print(f"Input: s = '{s2}', t = '{t2}'")
    print(f"Hash map approach: {is_anagram(s2, t2)}")
    print(f"Sorting approach: {is_anagram_sorting(s2, t2)}")
    print(f"Array approach: {is_anagram_array(s2, t2)}")
    print(f"Expected: False")
    print()
    
    # Test case 3: Empty strings
    s3 = ""
    t3 = ""
    print(f"Input: s = '{s3}', t = '{t3}'")
    print(f"Hash map approach: {is_anagram(s3, t3)}")
    print(f"Sorting approach: {is_anagram_sorting(s3, t3)}")
    print(f"Array approach: {is_anagram_array(s3, t3)}")
    print(f"Expected: True")
    print()
    
    # Test case 4: Single character
    s4 = "a"
    t4 = "a"
    print(f"Input: s = '{s4}', t = '{t4}'")
    print(f"Hash map approach: {is_anagram(s4, t4)}")
    print(f"Sorting approach: {is_anagram_sorting(s4, t4)}")
    print(f"Array approach: {is_anagram_array(s4, t4)}")
    print(f"Expected: True")
    print()
    
    # Performance comparison
    import time
    import random
    import string
    
    # Generate large test strings
    def generate_random_string(length):
        return ''.join(random.choices(string.ascii_lowercase, k=length))
    
    large_s = generate_random_string(100000)
    # Create an anagram by shuffling
    large_t = ''.join(random.sample(large_s, len(large_s)))
    
    # Time the hash map approach
    start_time = time.time()
    result1 = is_anagram(large_s, large_t)
    hash_map_time = time.time() - start_time
    
    # Time the sorting approach
    start_time = time.time()
    result2 = is_anagram_sorting(large_s, large_t)
    sorting_time = time.time() - start_time
    
    # Time the array approach
    start_time = time.time()
    result3 = is_anagram_array(large_s, large_t)
    array_time = time.time() - start_time
    
    print(f"Performance comparison (100k characters):")
    print(f"Hash map approach: {hash_map_time:.6f} seconds")
    print(f"Sorting approach: {sorting_time:.6f} seconds")
    print(f"Array approach: {array_time:.6f} seconds")
    print(f"All approaches returned: {result1} (should be True)")