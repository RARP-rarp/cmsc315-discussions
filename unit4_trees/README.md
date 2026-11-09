# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
   While completing this assignment, I learned about binary search trees (BSTs) and their ability to search extremely quickly compared to linear search algorithms. If the sorting occurs when inserting elements into a BST, the BST can produce a search that eliminates almost half of the remaining unsearched tree per step, reducing logarithmically. In the real-world example of employee IDs, it does seem to be tricky to force the IDs being added to be in the right order, though.It could be resorted each time a new employee ID is added, but that is far from the optimal solution. Perhaps the sorting could occur during processor and memory downtime.
   When implementing the program, there were a few challenges. One challenge was finding the right combination of comments and print statements to explain what was occurring in the code. Another challenge was how to explain what occurred during traversal of an empty BST. It seems that I may have been overthinking those two issues.