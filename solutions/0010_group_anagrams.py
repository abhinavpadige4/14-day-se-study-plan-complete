"""
LeetCode 49: Group Anagrams
Difficulty: Medium
Topics: Hash Table, String, Sorting

Problem:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Approach: Hash Map with Sorted String Keys
We can group anagrams by anagrams by using a hash map where the key is the sorted version of each string.
All anagrams will have the same sorted string, so they will map to the same key in our hash map.

Time Complexity: O(n * k log k) - Where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n * k) - For storing all the strings in the hash map buckets
"""

from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams together using sorted string as hash map key.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of lists where each inner list contains anagrams
    """
    # Hash map: sorted_string -> list of original strings that are anagrams
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Sort the string to create the key
        # All anagrams will have the same sorted string
        sorted_s = ''.join(sorted(s))
        # Add the original string to the group for this sorted key
        anagram_groups[sorted_s].append(s)
    
    # Return all the groups as a list of lists
    return list(anagram_groups.values())

def group_anagrams_counting(strs: List[str]) -> List[List[str]]:
    """
    Group anagrams using character count as key (more efficient for long strings).
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of lists where each inner list contains anagrams
    """
    # Hash map: character_count_tuple -> list of original strings
    anagram_groups = defaultdict(list)
    
    for s in strs:
        # Create character count array for 26 lowercase letters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Convert list to tuple so it can be used as dict key
        anagram_groups[tuple(count)].append(s)
    
    return list(anagram_groups.values())

def group_anagrams_brute_force(strs: List[str]) -> List[List[str]]:
    """
    Brute force approach - O(n^2 * k log k) time, O(n) space.
    Compare each string with every other string.
    
    Args:
        strs: List of strings to group
        
    Returns:
        List of lists where each inner list contains anagrams
    """
    if not strs:
        return []
    
    # Track which strings have been grouped
    used = [False] * len(strs)
    groups = []
    
    for i in range(len(strs)):
        if used[i]:
            continue
        
        # Start a new group with strs[i]
        current_group = [strs[i]]
        used[i] = True
        
        # Find all anagrams of strs[i]
        for j in range(i + 1, len(strs)):
            if not used[j] and sorted(strs[i]) == sorted(strs[j]):
                current_group.append(strs[j])
                used[j] = True
        
        groups.append(current_group)
    
    return groups

# Test cases
if __name__ == "__main__":
    # Test case 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: strs = {strs1}")
    result1 = group_anagrams(strs1)
    result1_alt = group_anagrams_counting(strs1)
    result1_brute = group_anagrams_brute_force(strs1)
    print(f"Hash map (sorted) approach: {sorted([sorted(group) for group in result1])}")
    print(f"Hash map (counting) approach: {sorted([sorted(group) for group in result1_alt])}")
    print(f"Brute force approach: {sorted([sorted(group) for group in result1_brute])}")
    print(f"Expected: [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']] (any order)")
    print()
    
    # Test case 2
    strs2 = [""]
    print(f"Input: strs = {strs2}")
    result2 = group_anagrams(strs2)
    result2_alt = group_anagrams_counting(strs2)
    result2_brute = group_anagrams_brute_force(strs2)
    print(f"Hash map (sorted) approach: {result2}")
    print(f"Hash map (counting) approach: {result2_alt}")
    print(f"Brute force approach: {result2_brute}")
    print(f"Expected: [['']]")
    print()
    
    # Test case 3
    strs3 = ["a"]
    print(f"Input: strs = {strs3}")
    result3 = group_anagrams(strs3)
    result3_alt = group_anagrams_counting(strs3)
    result3_brute = group_anagrams_brute_force(strs3)
    print(f"Hash map (sorted) approach: {result3}")
    print(f"Hash map (counting) approach: {result3_alt}")
    print(f"Brute force approach: {result3_brute}")
    print(f"Expected: [['a']]")
    print()
    
    # Test case 4: No anagrams
    strs4 = ["a", "b", "c"]
    print(f"Input: strs = {strs4}")
    result4 = group_anagrams(strs4)
    result4_alt = group_anagrams_counting(strs4)
    result4_brute = group_anagrams_brute_force(strs4)
    print(f"Hash map (sorted) approach: {sorted([sorted(group) for group in result4])}")
    print(f"Hash map (counting) approach: {sorted([sorted(group) for group in result4_alt])}")
    print(f"Brute force approach: {sorted([sorted(group) for group in result4_brute])}")
    print(f"Expected: [['a'], ['b'], ['c']] (any order)")
    print()
    
    # Test case 5: All same letters
    strs5 = ["abc", "bca", "cab", "bac", "acb", "cba"]
    print(f"Input: strs = {strs5}")
    result5 = group_anagrams(strs5)
    result5_alt = group_anagrams_counting(strs5)
    result5_brute = group_anagrams_brute_force(strs5)
    print(f"Hash map (sorted) approach: {sorted([sorted(group) for group in result5])}")
    print(f"Hash map (counting) approach: {sorted([sorted(group) for group in result5_alt])}")
    print(f"Brute force approach: {sorted([sorted(group) for group in result5_brute])}")
    print(f"Expected: [['abc', 'bca', 'cab', 'bac', 'acb', 'cba']] (all together)")
    print()
    
    # Performance comparison
    import time
    import random
    import string
    
    # Generate test data
    def generate_test_strings(count, avg_length):
        words = []
        base_words = [''.join(random.choices(string.ascii_lowercase, k=avg_length)) 
                     for _ in range(count // 3)]  # Unique base words
        
        for word in base_words:
            # Add the original word
            words.append(word)
            # Add some anagrams (shuffled versions)
            for _ in range(2):
                shuffled = ''.join(random.sample(word, len(word)))
                words.append(shuffled)
            # Add some completely different words
            words.append(''.join(random.choices(string.ascii_lowercase, k=avg_length)))
        
        # Shuffle the list
        random.shuffle(words)
        return words[:count]
    
    test_strs = generate_test_strings(1000, 8)
    
    # Time hash map (sorted) approach
    start_time = time.time()
    result1 = group_anagrams(test_strs)
    hashmap_sorted_time = time.time() - start_time
    
    # Time hash map (counting) approach
    start_time = time.time()
    result2 = group_anagrams_counting(test_strs)
    hashmap_counting_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result3 = group_anagrams_brute_force(test_strs[:50])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (1000 strings):")
    print(f"Hash map (sorted) approach: {hashmap_sorted_time:.6f} seconds")
    print(f"Hash map (counting) approach: {hashmap_counting_time:.6f} seconds")
    print(f"Brute force approach (50 strings): {brute_force_time:.6f} seconds")
    print(f"Both hash map approaches produce same number of groups: {len(result1) == len(result2)}")