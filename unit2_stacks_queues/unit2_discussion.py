"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque

class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack_list = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        self.stack_list.append(value) # adds the value to the top of the stack. values are removed from the top.

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        if len(self.stack_list) > 0:
            return self.stack_list.pop()
        else:
            print('Stack is empty, cannot pop from an empty stack')

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if len(self.stack_list) > 0:
            return self.stack_list[-1]
        else:
            print('Stack is empty, cannot peek at an empty stack')

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        if len(self.stack_list) == 0:
            return True
        else:
            return False

class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue_deque = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        self.queue_deque.append(value) # adds the value to the back of the queue. values are removed from the front.

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        if len(self.queue_deque) > 0:
            return self.queue_deque.popleft()
        else:
            print('Queue is empty, cannot pop from an empty queue')

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        if len(self.queue_deque) > 0:
            return self.queue_deque[0]
        else:
            print('Queue is empty, cannot retrieve a value from an empty queue')

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        if len(self.queue_deque) == 0:
            return True
        else:
            return False

def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
test_stack = Stack()
print("Created stack. Stack is empty.")
test_stack.push(1)
test_stack.push(2)
test_stack.push(3)
test_stack.push(4)
print(f"After pushing 1, 2, 3, and 4, the stack pops 4, which is LIFO. Popped value is {test_stack.pop()}")
print("      test popping from an empty stack,")
test_stack.pop()
test_stack.pop()
test_stack.pop()
print("Popped 3 times. Starting final pop when stack is empty:")
test_stack.pop()
print("      test peeking at an empty stack,")
print("Peeking when stack is empty:")
test_stack.peek()
print("      and verify a single-item stack becomes empty after removal.")
test_stack1 = Stack()
test_stack1.push(5)
print(f"Created a new stack with 1 element. Removed that 1 element. Element removed is: {test_stack1.pop()}")
print(f"True or False. Stack is empty: {test_stack1.is_empty()}")
# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
test_queue = Queue()
print("Created queue. Queue is empty.")
test_queue.enqueue(1)
test_queue.enqueue(2)
test_queue.enqueue(3)
test_queue.enqueue(4)
print(f"After enqueuing 1, 2, 3, and 4, the queue dequeues 1, which is FIFO. Dequeued value is {test_queue.dequeue()}")
print("      test dequeuing from an empty queue,")
test_queue.dequeue()
test_queue.dequeue()
test_queue.dequeue()
print("Dequeued 3 times. Starting final dequeue when queue is empty:")
test_queue.dequeue()
print("      test viewing the front of an empty queue,")
test_queue.front()
print("      and verify a single-item queue becomes empty after removal.")
test_queue1 = Queue()
test_queue1.enqueue(6)
print(f"Created a new queue with 1 element. Removed that 1 element. Element removed is: {test_queue1.dequeue()}")
print(f"True or False. Queue is empty: {test_queue1.is_empty()}")

if __name__ == "__main__":
    main()