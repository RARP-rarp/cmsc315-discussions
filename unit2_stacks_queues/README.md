# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explored two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implemented stack operations
- Implemented queue operations
- Understood LIFO and FIFO behavior
- Created edge cases

## Requirements

Completed all TODO sections:

1. Implemented stack operations.
2. Implemented queue operations.
3. Demonstrated LIFO behavior.
4. Demonstrated FIFO behavior.
5. Created and tested edge cases.
6. Created a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, added this reflection to the initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

Reflection

In software development, a stack works with last-in-first out (LIFO) behavior, i.e. the last entry put in the stack is the first entry that gets taken out of the stack. Good examples of this are undo buttons, which keep track of the last performed action so that it can be undone first, and browser back buttons, which keep track of the last visited site so that the user can return to that site first. A queue, however, works with first-in-first out (FIFO) behavior, i.e. the first entry put in the queue is the first entry that gets taken out of the queue. A good example of this is a line at an amusement park, in which the first person to get in line is the first person to get on the ride. These were the examples in my mind as I designed the stack and the queue for this discussion.

In Python, I created a list to represent a stack. The list's memory allocation grows as more items are added. More specifically, when an element is added to the list when the list is full, more memory space is allocated and the list's length increases automatically. Normally, the time complexity of appending to a list is O(1), but upon hitting the max length, appending can be O(N) (Pozo, 2026). This works for LIFO (the undo button) just fine. However, a deque in Python also supports automatically increasing memory allocation as elements are added, as long as I do not specify the max length. A deque structure acts as a doubly-linked list, that allows popping from the left end of the deque normally at an O(1) time complexity, whereas a list would perform normally at an O(N) time complexity (Pozo, 2026). Since this left-popping is great for my implementation of FIFO (the amusement park line), I used a deque to represent a queue.

While completing this assignment, I learned how to organize sequenced data in a data structure tailored for efficiency. A challenge for me was my misunderstanding of OneDrive folder settings, but learning how they work in a home user environment was worth the time spent.

Repository

The GitHub repository is located here: https://github.com/RARP-rarp/cmsc315-discussions

Use of Assistance Tools

On October 25, 2026, the generative artificial intelligence tool Google Gemini (Gemini 1.5 Flash, Google LLC) was used to assist in formatting and verifying bibliographic references according to AMA style guidelines.

References

Goodrich MT, Tamassia R, Goldwasser MH. CMSC 315: Data Structures and Analysis. Zyante Inc; February 2026. Accessed October 25, 2026. https://www.zybooks.com

Pozo Ramos L. Python's deque: Implement efficient queues and stacks. Real Python. Published January 12, 2026. Accessed October 25, 2026. https://realpython.com/python-deque/