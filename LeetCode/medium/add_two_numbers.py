# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):

        list_node = self
        while list_node is not None:
            print(list_node.val, end="->")
            list_node = list_node.next
        print("None")

class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        result = ListNode()

        while l1 is not None:            
            print(f"l1.val: {l1.val}")
            print(f"l2.val: {l2.val}")
            result.val = l1.val + l2.val
            l1 = l1.next
            l2 = l2.next

            print(f"result.val : {result.val}")
            print(f"result.next : {result.next}")

            result.next = ListNode(val=0, next=None)
            result = result.next

        result.print_list()
        return result




if __name__ == "__main__":

    # case1
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]

    list_node1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3, next=None)))
    list_node2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4, next=None)))

    list_node1.print_list()
    list_node2.print_list()

    solution = Solution()
    solution.addTwoNumbers(list_node1, list_node2)


    print(f"list_node1.val : {list_node1.val}")
    print(f"list_node1.next : {list_node1.next}")

    print(f"list_node1 : {list_node1}")
    print(f"list_node2 : {list_node2}")

    # exit()
    
    # solution = Solution()

    # # case1
    # l1 = [2, 4, 3]
    # l2 = [5, 6, 4]

    # solution.addTwoNumbers(l1, l2)

    # # case2
    # l1 = [0]
    # l2 = [0]

    # solution.addTwoNumbers(l1, l2)

    # # case3
    # l1 = [9,9,9,9,9,9,9]
    # l2 = [9,9,9,9]

    # solution.addTwoNumbers(l1, l2)