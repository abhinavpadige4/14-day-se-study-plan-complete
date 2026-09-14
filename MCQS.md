# Multiple Choice Questions for 14-Day SE Study Plan

This file contains 30 MCQs covering all major topics from the 14-day study plan, with answers and explanations.

## Arrays & Strings (Questions 1-8)

### Question 1: Two Sum
What is the time complexity of the optimal solution for the Two Sum problem using a hash map?
A. O(n²)
B. O(n log n)
C. O(n)
D. O(1)

<details>
<summary>Answer</summary>
<p><strong>C. O(n)</strong></p>
<p>Explanation: We traverse the array once, and each hash map lookup/insertion is O(1) on average, resulting in O(n) time complexity.</p>
</details>

### Question 2: Valid Anagram
Which approach is most efficient for checking if two strings are anagrams when dealing with lowercase English letters only?
A. Sorting both strings
B. Using a hash map to count characters
C. Using a fixed-size array of 26 integers
D. Brute force comparison

<details>
<summary>Answer</summary>
<p><strong>C. Using a fixed-size array of 26 integers</strong></p>
<p>Explanation: For lowercase English letters, a fixed-size array of 26 integers is most efficient with O(n) time and O(1) space.</p>
</details>

### Question 3: Contains Duplicate
What happens in the hash set approach to Contains Duplicate when we encounter an element already in the set?
A. Continue to next element
B. Add it again to the set
C. Return True immediately
D. Remove it from the set

<details>
<summary>Answer</summary>
<p><strong>C. Return True immediately</strong></p>
<p>Explanation: If we find an element already in our "seen" set, we know a duplicate exists and can return True immediately.</p>
</details>

### Question 4: Product of Array Except Self
Why can't we use division in the Product of Array Except Self problem?
A. Division is too slow
B. The problem explicitly prohibits it
C. It fails when there are zeros in the array
D. Both B and C

<details>
<summary>Answer</summary>
<p><strong>D. Both B and C</strong></p>
<p>Explanation: The problem states we must solve it without division, and division fails when there are zeros (division by zero).</p>
</details>

### Question 5: Maximum Subarray
In Kadane's algorithm for Maximum Subarray, what does current_sum represent?
A. Maximum sum found so far
B. Maximum sum ending at current position
C. Minimum sum ending at current position
D. Sum of all elements processed

<details>
<summary>Answer</summary>
<p><strong>B. Maximum sum ending at current position</strong></p>
<p>Explanation: current_sum tracks the maximum subarray sum that ends at the current position, which we then use to update the global maximum.</p>
</details>

### Question 6: Climbing Stairs
Why is the Climbing Stairs problem equivalent to the Fibonacci sequence?
A. Both use dynamic programming
B. Each step depends on the previous two steps
C. Both have exponential time complexity
D. They use the same base cases

<details>
<summary>Answer</summary>
<p><strong>B. Each step depends on the previous two steps</strong></p>
<p>Explanation: To reach step n, you can come from step n-1 (1 step) or step n-2 (2 steps), giving the recurrence f(n) = f(n-1) + f(n-2), which is Fibonacci.</p>
</details>

### Question 7: Best Time to Buy and Sell Stock
What does min_price track in the stock profit problem?
A. The minimum profit possible
B. The lowest price seen so far
C. The price to buy at for maximum profit
D. The average price of all stocks

<details>
<summary>Answer</summary>
<p><strong>B. The lowest price seen so far</strong></p>
<p>Explanation: min_price tracks the lowest price encountered so far, allowing us to calculate the best profit if we sold at the current price.</p>
</details>

### Question 8: House Robber
In the House Robber problem, why can't we simply take every other house?
A. Houses have different values
B. Adjacent houses trigger alarms
C. The pattern might not be optimal
D. We need to rob consecutive houses

<details>
<summary>Answer</summary>
<p><strong>C. The pattern might not be optimal</strong></p>
<p>Explanation: Taking every other house (e.g., indices 0, 2, 4...) might miss a better solution like taking indices 1, 3, 5... or skipping differently based on house values.</p>
</details>

## Trees & Graphs (Questions 9-16)

### Question 9: Binary Tree Traversal
Which traversal visits nodes in the order: left subtree, root, right subtree?
A. Pre-order
B. In-order
C. Post-order
D. Level-order

<details>
<summary>Answer</summary>
<p><strong>B. In-order</strong></p>
<p>Explanation: In-order traversal visits left subtree first, then root, then right subtree (L-Root-R).</p>
</details>

### Question 10: Binary Search Tree
What property must a Binary Search Tree satisfy?
A. Left child < parent < right child
B. Left child > parent > right child
C. All left descendants < node < all right descendants
D. Both A and C

<details>
<summary>Answer</summary>
<p><strong>D. Both A and C</strong></p>
<p>Explanation: A BST requires that for each node, all elements in left subtree are less than the node, and all elements in right subtree are greater than the node.</p>
</details>

### Question 11: Maximum Depth of Binary Tree
How do we calculate the maximum depth of a binary tree recursively?
A. max(depth(left), depth(right))
B. 1 + max(depth(left), depth(right))
C. depth(left) + depth(right)
D. 1 + depth(left) + depth(right)

<details>
<summary>Answer</summary>
<p><strong>B. 1 + max(depth(left), depth(right))</strong></p>
<p>Explanation: The depth of a tree is 1 (for the root) plus the maximum depth of its left and right subtrees.</p>
</details>

### Question 12: Validate Binary Search Tree
Why is it insufficient to only check that left child < parent < right child for each node?
A. It's too computationally expensive
B. It doesn't account for grandchildren values
C. It only works for balanced trees
D. The tree might not be binary

<details>
<summary>Answer</summary>
<p><strong>B. It doesn't account for grandchildren values</strong></p>
<p>Explanation: A node might be valid compared to its immediate children but invalid compared to deeper descendants (e.g., a left child's right grandchild could be greater than the root).</p>
</details>

### Question 13: Number of Islands
What algorithm is typically used to solve the Number of Islands problem?
A. Dijkstra's algorithm
B. Binary search
C. Depth-First Search or Breadth-First Search
D. Topological sort

<details>
<summary>Answer</summary>
<p><strong>C. Depth-First Search or Breadth-First Search</strong></p>
<p>Explanation: We use DFS or BFS to explore and mark all connected land ('1's) as visited when we encounter an island.</p>
</details>

### Question 14: Clone Graph
What data structure is commonly used to track visited nodes when cloning a graph?
A. Stack
B. Queue
C. Hash map
D. Array

<details>
<summary>Answer</summary>
<p><strong>C. Hash map</strong></p>
<p>Explanation: A hash map (original_node -> cloned_node) is used to track which nodes we've already cloned to handle cycles and avoid infinite loops.</p>
</details>

### Question 15: Course Schedule
What does detecting a cycle in the Course Schedule problem indicate?
A. All courses can be completed
B. Some courses have no prerequisites
C. It's impossible to finish all courses
D. Courses can be taken in any order

<details>
<summary>Answer</summary>
<p><strong>C. It's impossible to finish all courses</strong></p>
<p>Explanation: A cycle in the prerequisite graph means there's a circular dependency (A requires B, B requires C, C requires A), making it impossible to complete all courses.</p>
</details>

### Question 16: Pacific Atlantic Water Flow
Why do we start DFS/BFS from the oceans rather than from each cell?
A. It's more efficient (O(mn) vs O(m²n²))
B. Oceans have higher elevation
C. Water flows from high to low elevation
D. Both A and C

<details>
<summary>Answer</summary>
<p><strong>D. Both A and C</strong></p>
<p>Explanation: Starting from oceans and flowing uphill (reverse flow) is more efficient than checking each cell's path to both oceans.</p>
</details>

## Dynamic Programming (Questions 17-22)

### Question 17: Longest Increasing Subsequence
What does dp[i] represent in the LIS problem?
A. Length of LIS ending at index i
B. Length of LIS starting at index i
C. Length of LIS in subarray nums[0:i]
D. Minimum last element of LIS of length i

<details>
<summary>Answer</summary>
<p><strong>A. Length of LIS ending at index i</strong></p>
<p>Explanation: In the standard DP approach, dp[i] stores the length of the longest increasing subsequence that ends exactly at index i.</p>
</details>

### Question 18: Edit Distance
What are the three operations allowed in the Edit Distance problem?
A. Insert, Delete, Replace
B. Insert, Delete, Copy
C. Insert, Replace, Swap
D. Delete, Replace, Merge

<details>
<summary>Answer</summary>
<p><strong>A. Insert, Delete, Replace</strong></p>
<p>Explanation: The Edit Distance problem allows three operations: insert a character, delete a character, or replace a character.</p>
</details>

### Question 19: Word Break
What optimization can we apply to the Word Break problem to improve efficiency?
A. Memoization
B. Limiting dictionary word length
C. Sorting the dictionary
D. Both A and B

<details>
<summary>Answer</summary>
<p><strong>D. Both A and B</strong></p>
<p>Explanation: We can use memoization to avoid recomputing results and limit checks to words of length ≤ max word length in dictionary.</p>
</details>

### Question 20: Coin Change
Why is the greedy approach incorrect for the Coin Change problem?
A. It's too slow
B. It doesn't work for all coin systems
C. It uses too much memory
D. It only works for sorted coins

<details>
<summary>Answer</summary>
<p><strong>B. It doesn't work for all coin systems</strong></p>
<p>Explanation: Greedy fails for coin systems like [1, 3, 4] when making 6: greedy picks 4+1+1 (3 coins) but optimal is 3+3 (2 coins).</p>
</details>

### Question 21: Dynamic Programming Principles
What are the two key properties that indicate a problem can be solved with DP?
A. Overlapping subproblems and optimal substructure
B. Memoization and tabulation
C. Recursion and iteration
D. Greedy choice and backtracking

<details>
<summary>Answer</summary>
<p><strong>A. Overlapping subproblems and optimal substructure</strong></p>
<p>Explanation: DP applies when a problem has overlapping subproblems (same subproblems solved multiple times) and optimal substructure (optimal solution contains optimal solutions to subproblems).</p>
</details>

### Question 22: Space Optimization in DP
When can we optimize DP space from O(n) to O(1)?
A. When we only need the previous value
B. When we only need the last two values
C. When the recurrence depends on a fixed number of previous states
D. Always

<details>
<summary>Answer</summary>
<p><strong>C. When the recurrence depends on a fixed number of previous states</strong></p>
<p>Explanation: We can optimize to O(1) space when dp[i] depends only on a fixed number of previous states (e.g., dp[i-1] and dp[i-2]), allowing us to reuse variables.</p>
</details>

## System Design (Questions 23-26)

### Question 23: URL Shortener
What is the primary challenge in designing a URL shortener like bit.ly?
A. Generating unique short codes
B. Handling massive scale of redirects
C. Storing the original URLs
D. All of the above

<details>
<summary>Answer</summary>
<p><strong>D. All of the above</strong></p>
<p>Explanation: A URL shortener must generate unique codes, handle billions of redirects efficiently, and store mappings reliably.</p>
</details>

### Question 24: Rate Limiter
Which algorithm is commonly used for rate limiting?
A. Leaky bucket
B. Token bucket
C. Fixed window counter
D. All of the above

<details>
<summary>Answer</summary>
<p><strong>D. All of the above</strong></p>
<p>Explanation: Leaky bucket, token bucket, and fixed window counter are all common rate limiting algorithms with different trade-offs.</p>
</details>

### Question 25: Chat System Design
What technology enables real-time communication in a chat application?
A. HTTP polling
B. WebSockets
C. REST APIs
D. GraphQL

<details>
<summary>Answer</summary>
<p><strong>B. WebSockets</strong></p>
<p>Explanation: WebSockets provide full-duplex communication channels over a single TCP connection, enabling real-time bidirectional communication.</p>
</details>

### Question 26: System Design Trade-offs
What is the CAP theorem in distributed systems?
A. Consistency, Availability, Partition tolerance
B. Cost, Accuracy, Performance
C. Cache, Async, Parallel
D. Compile, Assemble, Package

<details>
<summary>Answer</summary>
<p><strong>A. Consistency, Availability, Partition tolerance</strong></p>
<p>Explanation: The CAP theorem states that in a distributed system, you can only guarantee at most two of the three properties: Consistency, Availability, and Partition tolerance.</p>
</details>

## Python FastAPI & SQL (Questions 27-28)

### Question 27: FastAPI
What is the primary advantage of using Pydantic models in FastAPI?
A. Faster execution
B. Automatic data validation and serialization
C. Built-in authentication
D. Database integration

<details>
<summary>Answer</summary>
<p><strong>B. Automatic data validation and serialization</strong></p>
<p>Explanation: Pydantic models automatically validate incoming data against defined schemas and serialize outgoing data, reducing boilerplate code.</p>
</details>

### Question 28: SQL Joins
Which JOIN returns all records when there is a match in either left or right table?
A. INNER JOIN
B. LEFT JOIN
C. RIGHT JOIN
D. FULL OUTER JOIN

<details>
<summary>Answer</summary>
<p><strong>D. FULL OUTER JOIN</strong></p>
<p>Explanation: FULL OUTER JOIN returns all records when there is a match in either left or right table, filling unmatched sides with NULLs.</p>
</details>

## React, TypeScript, Docker & CI/CD (Questions 29-30)

### Question 29: React Hooks
What is the primary purpose of the useEffect hook in React?
A. Managing local state
B. Handling side effects in functional components
C. Creating reusable components
D. Optimizing rendering performance

<details>
<summary>Answer</summary>
<p><strong>B. Handling side effects in functional components</strong></p>
<p>Explanation: useEffect lets you perform side effects in functional components, such as data fetching, subscriptions, or manually changing the DOM.</p>
</details>

### Question 30: Docker
What does the COPY instruction do in a Dockerfile?
A. Copies files from host to container image
B. Exposes network ports
C. Sets environment variables
D. Defines the command to run when container starts

<details>
<summary>Answer</summary>
<p><strong>A. Copies files from host to container image</strong></p>
<p>Explanation: The COPY instruction copies new files, directories or remote file URLs from <src> and adds them to the filesystem of the image at the path <dest>.</p>
</details>