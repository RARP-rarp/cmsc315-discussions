"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # In the recursive method, insertion to the left should be a smaller value, and to the right = larger
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Create a new node when a position is found.
        if node is None:
            return Node(value)
        # Insert smaller values into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Insert larger values into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # Return the updated node reference.
        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # The BST search is efficient by looking at sorted values, reducing the search space by subtrees at each step
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # initializes an empty list
        values = []
        # starts recursion from self.root
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is not None:
            # Visit the left subtree, giving sorted smallest values
            self._inorder_recursive(node.left, values)
            # Visit the current node, giving sorted next smallest value
            values.append(node.value)
            # Visit the right subtree, giving sorted next smallest values
            self._inorder_recursive(node.right, values)



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")
    bst = BST()
    numbers_to_insert = [5000, 3000, 7000, 2000, 4000, 6000, 8000]
    # While inserting, if values are distributed in the specific order of middle (50), then middles of the two
    # halves (30, 70), etc., this insertion style sorts the values into subtrees, which makes the search efficient by
    # maximizing the amount of search space reduced for each search step.
    for val in numbers_to_insert:
        bst.insert(val)
    print(f"Inserted values: {numbers_to_insert}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")
    sorted_bst = bst.inorder()
    # traversal already sorts, because of our logic in recursively traversing left, current, then right trees.
    print(f"\nIn-order Traversal (Sorted): {sorted_bst}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.
    # The search traverses the trees and eliminates subtrees at each step depending on if the value is higher or lower.
    print(f"Searching for 1000. Found returns True. Not Found returns False. Returned: {bst.search(1000)}")
    print(f"Searching for 2000. Found returns True. Not Found returns False. Returned: {bst.search(2000)}")
    print(f"Searching for 3000. Found returns True. Not Found returns False. Returned: {bst.search(3000)}")
    print(f"Searching for 9000. Found returns True. Not Found returns False. Returned: {bst.search(9000)}")

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    # Traverse an empty tree, which return an empty list because nothing was inserted to fill the list
    bst2=BST()
    print(f"Traversing an empty tree returns: {bst2.inorder()}")



if __name__ == "__main__":
    main()