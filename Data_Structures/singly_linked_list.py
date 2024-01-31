class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, element_data):
        new_node = Node(element_data)
        existing_list_node = None

        if self.head is None:
            self.head = new_node
            existing_list_node = self.head
        else:
            existing_list_node = self.head
            while existing_list_node.next:
                existing_list_node = existing_list_node.next

            existing_list_node.next = new_node

        print(f"element {element_data} appended successfully")

        return

    def print_list(self):
        known_node = self.head
        print_list = None

        # Mistake Again. next is not required here. it should be known_node and not known_node.next in while
        while known_node is not None:
            if print_list is None:
                print_list = "head ->"
            
            print_list = str(print_list) + str(known_node.data) + "->"
            
            # Missed this line
            known_node = known_node.next
            if known_node is None:
                print_list = print_list[:-2]


        print(print_list)

if __name__ == "__main__":
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(99)
    singly_linked_list.append(100)
    singly_linked_list.append(101)

    singly_linked_list.print_list()

### Feedback (31st Jan 2024)
#     Your implementation of the SinglyLinkedList and Node classes is a good start, but there are a few areas that need some improvement for it to work correctly. Particularly, your print_list method needs some adjustments to correctly print all elements in the list. Let's go through the changes:

# In print_list Method: Currently, it only prints the head node's data and does not iterate through the entire list. You need a loop to traverse through each node until you reach the end of the list.

# Print Formatting: The current print format in print_list will print an arrow after every node, including the last one. You might want to adjust this so that the arrow is not printed after the last node.

# ----------------------------------------
# the rest of your code looks good for a basic implementation of a singly linked list. Here's a quick review:

# Node Class: Your Node class is well-defined with a constructor that initializes data and next. This is exactly what you need for a singly linked list node.

# SinglyLinkedList Class:

# The __init__ method correctly initializes an empty list with self.head set to None.
# The append method is implemented properly. It handles two cases:
# If the list is empty (self.head is None), it sets self.head to the new node.
# If the list is not empty, it traverses to the end of the list and attaches the new node there.
# Efficiency Consideration:

# In the append method, you are traversing the entire list to find the last node every time you want to append a new element. This is an O(n) operation, where n is the number of elements in the list. This is fine for a basic implementation, but for a more efficient approach, especially when dealing with longer lists, you might consider keeping a reference to the tail of the list. This would allow you to append new nodes in O(1) time.
# Print Statement in Append:

# Your use of a print statement within the append method to confirm successful appending is good for debugging and learning purposes. However, in a production environment or more advanced implementation, you might want to handle this differently, possibly using logging or returning a status.
    
#--------------------------------------------------
# Evaluating your code for a basic implementation of a singly linked list in Python, I would rate it around 7 out of 10. Here's the breakdown of the assessment:

# Correct Implementation (3/3): Your implementation of the singly linked list with the basic append and print_list functionalities is correct. The logic for adding new nodes and initializing the list is well done.

# Code Structure and Style (2/3): The structure of your classes (Node and SinglyLinkedList) is good. However, the print_list method in your original submission needed improvement to correctly print all elements. Also, the code could be enhanced in terms of readability and Pythonic practices, such as using more descriptive variable names.

# Efficiency (1/2): While your append method works correctly, it is not the most efficient for large lists, as it traverses the entire list to find the end each time. This is a common approach but can be optimized by maintaining a tail reference.

# Scalability and Robustness (1/2): Your implementation covers the basic requirements but lacks additional features that might be expected in a more robust implementation, such as handling edge cases and supporting more operations (like deletion, searching, or inserting at a specific position).

# Improvements for a higher score would include optimizing the append operation for efficiency, enhancing the print_list method, and adding more functionality and robustness to your linked list implementation. But overall, it's a solid start and demonstrates a good understanding of the basic concepts of linked lists in Python.






