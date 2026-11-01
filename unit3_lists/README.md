# Unit 3 Discussion: List Operations

## Overview

This assignment examined insertion, deletion, and searching in Python lists.

## Learning Objectives

- Inserted values into a list
- Deleted values from a list
- Searched for values in a list
- Analyzed list behavior and performance

## Requirements

1. Tested insertion at the beginning, middle, and end.
2. Tested deletion at the beginning, middle, and end.
3. Searched for existing and missing values.
4. Demonstrated edge cases.
5. Created a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
   In Python, lists are useful data structures that have specific strengths and weaknesses. Selecting the right data structure for the job is important to prevent surprise performance losses during implementation. Lists can work well in smaller datasets or when LIFO behavior is the norm. A good real-world example that fits this assignment is a deck of cards. The list represents the deck of cards. Each card is represented by a value between 1 and 52. The methods allow for removing or inserting cards from/to the deck, as well as searching for a specific card in the deck.
   In addition to learning about Python's lists, I encountered some challenges. One challenge was constructing the right environments for the edge cases to be tested properly. Instead of using more elaborate tests, I simply used print statements as needed.
   List operations can impact performance in real-world applications. For example, insertion towards the beginning of a large list will cost more performance than towards the end, since insertion shifts all higher indexes to the right. Search methods are typically linear search algorithms instead of binary search algorithms, which costs performance. This is due to lists being unsorted.
   I was able to push to the GitHub repository at https://github.com/RARP-rarp/cmsc315-discussions