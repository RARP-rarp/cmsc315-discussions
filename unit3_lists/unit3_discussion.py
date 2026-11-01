"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # insertion will shift all elements >= index to the right by 1
    # insertion towards the beginning of a large list will cost more performance than towards the end
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # the if statement ensures the index is valid before popping, else returns None
    # without index validation and safe deletion, there could be an IndexError
    if -len(lst) <= index < len(lst):
        return lst.pop(index)
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # search needs to scan sequentially to find the first occurrence of the value
    # lists are not sorted, so cannot use binary search
    try:
        return lst.index(value)
    except ValueError:
        return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")
    # creating a list with ten values: 33, 30, 28, 27, 20, 17, 15, 10, 6, 3
    the_list = [33, 30, 28, 27, 20, 17, 15, 10, 6, 3]
    print(the_list)
    # inserting at the beginning
    insert_at(the_list, 0, 0)
    print(the_list)
    # inserting in the middle
    insert_at(the_list, 5, 0)
    print(the_list)
    # inserting at the end
    insert_at(the_list, 12, 0)
    print(the_list)


    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")
    print(the_list)
    # deleting an item at the beginning
    print(delete_at(the_list, 0))
    print(the_list)
    # deleting an item in the middle
    print(delete_at(the_list, 4))
    print(the_list)
    # deleting an item at the end
    print(delete_at(the_list, 10))
    print(the_list)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")
    # searching for a value that exists: 20
    print(f"The searched value is at the following index. If -1, then value not found. Index: "
          f"{search_value(the_list, 20)}")
    # searching for a value that does not exist: 19
    print(f"The searched value is at the following index. If -1, then value not found. Index: "
          f"{search_value(the_list, 19)}")


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")
    # deleting using an invalid index
    print("Deleting from an invalid index should return None. Example: ")
    print(delete_at(the_list, 10))
    # searching for a missing value was done in the previous section

    # making list empty:
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)
    delete_at(the_list, 0)

    # deleting from an empty list
    print("Deleting from an empty list should return None. Example: ")
    print(delete_at(the_list, 0))
    # inserting into an empty list
    print("Inserting into an empty list should show only that value. Example: ")
    insert_at(the_list, 10, 35)
    print(the_list)



if __name__ == "__main__":
    main()