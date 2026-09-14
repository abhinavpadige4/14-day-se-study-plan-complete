"""
LeetCode 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Topics: Array, Dynamic Programming, Greedy

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

Approach: Single Pass with Minimum Tracking
We track the minimum price seen so far and calculate potential profit at each step.
For each price, we calculate: profit = current_price - min_price_so_far
We keep track of the maximum profit encountered.

Time Complexity: O(n) - Single pass through the prices array
Space Complexity: O(1) - Only using constant extra space (min_price and max_profit)
"""

from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculate maximum profit from buying and selling stock once.
    
    Args:
        prices: List of stock prices where prices[i] is price on day i
        
    Returns:
        Maximum profit achievable (0 if no profit possible)
    """
    if not prices or len(prices) < 2:
        return 0
    
    # Initialize minimum price to first day's price
    min_price = prices[0]
    # Initialize maximum profit to 0
    max_profit = 0
    
    # Iterate through prices starting from day 2
    for price in prices[1:]:
        # Calculate potential profit if we sell today
        profit = price - min_price
        
        # Update max_profit if today's profit is better
        max_profit = max(max_profit, profit)
        
        # Update min_price if today's price is lower
        min_price = min(min_price, price)
    
    return max_profit

def max_profit_brute_force(prices: List[int]) -> int:
    """
    Brute force approach - O(n^2) time, O(1) space.
    Check all possible buy-sell pairs.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Maximum profit achievable
    """
    if not prices or len(prices) < 2:
        return 0
    
    max_profit = 0
    n = len(prices)
    
    # Check all possible buy-sell pairs (buy day < sell day)
    for i in range(n):
        for j in range(i + 1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    
    return max_profit

def max_profit_with_days(prices: List[int]) -> tuple:
    """
    Calculate maximum profit and return the buy/sell days as well.
    
    Args:
        prices: List of stock prices
        
    Returns:
        Tuple of (max_profit, buy_day, sell_day)
        Days are 0-indexed, return (-1, -1) if no profit possible
    """
    if not prices or len(prices) < 2:
        return 0, -1, -1
    
    min_price = prices[0]
    max_profit = 0
    buy_day = sell_day = 0
    min_price_day = 0
    
    for i in range(1, len(prices)):
        price = prices[i]
        profit = price - min_price
        
        if profit > max_profit:
            max_profit = profit
            buy_day = min_price_day
            sell_day = i
        
        if price < min_price:
            min_price = price
            min_price_day = i
    
    return max_profit, buy_day, sell_day

# Test cases
if __name__ == "__main__":
    # Test case 1
    prices1 = [7, 1, 5, 3, 6, 4]
    print(f"Input: prices = {prices1}")
    print(f"Single pass approach: {max_profit(prices1)}")
    print(f"Brute force approach: {max_profit_brute_force(prices1)}")
    profit, buy, sell = max_profit_with_days(prices1)
    print(f"With days: profit={profit}, buy day={buy} (price={prices1[buy]}), sell day={sell} (price={prices1[sell]})")
    print(f"Expected: 5 (buy at 1, sell at 6)")
    print()
    
    # Test case 2
    prices2 = [7, 6, 4, 3, 1]
    print(f"Input: prices = {prices2}")
    print(f"Single pass approach: {max_profit(prices2)}")
    print(f"Brute force approach: {max_profit_brute_force(prices2)}")
    profit, buy, sell = max_profit_with_days(prices2)
    print(f"With days: profit={profit}, buy day={buy}, sell day={sell}")
    print(f"Expected: 0 (no profitable transaction)")
    print()
    
    # Test case 3
    prices3 = [1, 2, 3, 4, 5]
    print(f"Input: prices = {prices3}")
    print(f"Single pass approach: {max_profit(prices3)}")
    print(f"Brute force approach: {max_profit_brute_force(prices3)}")
    profit, buy, sell = max_profit_with_days(prices3)
    print(f"With days: profit={profit}, buy day={buy} (price={prices3[buy]}), sell day={sell} (price={prices3[sell]})")
    print(f"Expected: 4 (buy at 1, sell at 5)")
    print()
    
    # Test case 4: Single price
    prices4 = [5]
    print(f"Input: prices = {prices4}")
    print(f"Single pass approach: {max_profit(prices4)}")
    print(f"Brute force approach: {max_profit_brute_force(prices4)}")
    profit, buy, sell = max_profit_with_days(prices4)
    print(f"With days: profit={profit}, buy day={buy}, sell day={sell}")
    print(f"Expected: 0 (need at least 2 days)")
    print()
    
    # Test case 5: Same prices
    prices5 = [3, 3, 3, 3, 3]
    print(f"Input: prices = {prices5}")
    print(f"Single pass approach: {max_profit(prices5)}")
    print(f"Brute force approach: {max_profit_brute_force(prices5)}")
    profit, buy, sell = max_profit_with_days(prices5)
    print(f"With days: profit={profit}, buy day={buy}, sell day={sell}")
    print(f"Expected: 0 (no price difference)")
    print()
    
    # Test case 6: Large increase at end
    prices6 = [3, 2, 6, 5, 0, 3]
    print(f"Input: prices = {prices6}")
    print(f"Single pass approach: {max_profit(prices6)}")
    print(f"Brute force approach: {max_profit_brute_force(prices6)}")
    profit, buy, sell = max_profit_with_days(prices6)
    print(f"With days: profit={profit}, buy day={buy} (price={prices6[buy]}), sell day={sell} (price={prices6[sell]})")
    print(f"Expected: 4 (buy at 0, sell at 3)")
    print()
    
    # Performance comparison
    import time
    import random
    
    # Generate large test array
    large_prices = [random.randint(1, 1000) for _ in range(100000)]
    
    # Time single pass approach
    start_time = time.time()
    result1 = max_profit(large_prices)
    single_pass_time = time.time() - start_time
    
    # Time brute force approach (will be very slow)
    start_time = time.time()
    result2 = max_profit_brute_force(large_prices[:1000])  # Much smaller array
    brute_force_time = time.time() - start_time
    
    print(f"Performance comparison (100k elements):")
    print(f"Single pass approach: {single_pass_time:.6f} seconds")
    print(f"Brute force approach (1000 elements): {brute_force_time:.6f} seconds")
    print(f"Speed improvement: {brute_force_time/single_pass_time:.0f}x faster")
    print(f"Results reasonable: {0 <= result1 <= max(large_prices)}")