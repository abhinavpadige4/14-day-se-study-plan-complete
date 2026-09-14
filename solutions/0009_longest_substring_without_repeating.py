"""
LeetCode 3: Longest Substring Without Repeating Characters
Difficulty: Medium
Topics: Hash Table, String, Sliding Window

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.

Approach: Sliding Window with Hash Map
We use a sliding window approach with two pointers (left and right) and a hash map to track the last seen index of each character.
As we expand the right pointer, if we encounter a character that's already in our current window, we move the left pointer to just after the last occurrence of that character.
We keep track of the maximum window size encountered.

Time Complexity: O(n) - Each character is visited at most twice (once by right pointer, once by left pointer)
Space Complexity: O(min(m, n)) - Where m is the size of the charset (e.g., 26 for lowercase English letters)
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    if not s:
        return 0
    
    # Hash map to store the last index where each character was seen
    char_index_map = {}
    max_length = 0
    left = 0  # Left pointer of the sliding window
    
    # Expand the window with the right pointer
    for right in range(len(s)):
        current_char = s[right]
        
        # If the character is already in our current window, move left pointer
        if current_char in char_index_map and char_index_map[current_char] >= left:
            # Move left pointer to just after the last occurrence of current_char
            left = char_index_map[current_char] + 1
        
        # Update the last seen index of the current character
        char_index_map[current_char] = right
        
        # Update max_length if current window is larger
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    
    return max_length

def length_of_longest_substring_brute_force(s: str) -> int:
    """
    Brute force approach - O(n^3) time, O(min(n, m)) space.
    Check all possible substrings.
    
    Args:
        s: Input string
        
    Returns:
        Length of the longest substring without repeating characters
    """
    if not s:
        return 0
    
    max_length = 0
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            # Check if substring has all unique characters
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

# Test cases
if __name__ == "__main__":
    # Test case 1
    s1 = "abcabcbb"
    print(f"Input: s = '{s1}'")
    print(f"Sliding window approach: {length_of_longest_substring(s1)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s1)}")
    print(f"Expected: 3 (substring 'abc')")
    print()
    
    # Test case 2
    s2 = "bbbbb"
    print(f"Input: s = '{s2}'")
    print(f"Sliding window approach: {length_of_longest_substring(s2)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s2)}")
    print(f"Expected: 1 (substring 'b')")
    print()
    
    # Test case 3
    s3 = "pwwkew"
    print(f"Input: s = '{s3}'")
    print(f"Sliding window approach: {length_of_longest_substring(s3)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s3)}")
    print(f"Expected: 3 (substring 'wke')")
    print()
    
    # Test case 4: Empty string
    s4 = ""
    print(f"Input: s = '{s4}'")
    print(f"Sliding window approach: {length_of_longest_substring(s4)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s4)}")
    print(f"Expected: 0")
    print()
    
    # Test case 5: Single character
    s5 = "a"
    print(f"Input: s = '{s5}'")
    print(f"Sliding window approach: {length_of_longest_substring(s5)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s5)}")
    print(f"Expected: 1 (substring 'a')")
    print()
    
    # Test case 6: All unique characters
    s6 = "abcdef"
    print(f"Input: s = '{s6}'")
    print(f"Sliding window approach: {length_of_longest_substring(s6)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s6)}")
    print(f"Expected: 6 (substring 'abcdef')")
    print()
    
    # Test case 7: No repeating characters until the end
    s7 = "abcadefg"
    print(f"Input: s = '{s7}'")
    print(f"Sliding window approach: {length_of_longest_substring(s7)}")
    print(f"Brute force approach: {length_of_longest_substring_brute_force(s7)}")
    print(f"Expected: 6 (substring 'bcadef' or 'cadefg')")
    print()
    
    # Performance comparison
    import time
    import random
    import string
    
    # Generate test string with some repeats
    def generate_test_string(length, repeat_prob=0.3):
        result = []
        for i in range(length):
            if random.random() < repeat_prob and i > 0:
                # Repeat a random previous character
                result.append(random.choice(result))
            else:
                # Add a new random character
                result.append(random.choice(string.ascii_lowercase))
        return ''.join(result)
    
    test_string = generate_test_string(50000)
    
    # Time sliding window approach
    start_time = time.time()
    result1 = length_of_longest_substring(test_string)
    sliding_window_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result2 = length_of_longest_substring_brute_force(test_string[:100])  # Much smaller
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison:")
    print(f"Sliding window approach (50k chars): {sliding_window_time:.6f} seconds")
    print(f"Brute force approach (100 chars): {brute_force_time:.6f} seconds")
    print(f"Results match for small string: {length_of_longest_substring('abcabcbb') == length_of_longest_substring_brute_force('abcabcbb')}")