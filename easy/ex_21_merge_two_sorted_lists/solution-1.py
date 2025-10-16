# =========================================================
# This solution changes the original lists.
# =========================================================

from utils import ListNode


def mergeTwoLists(list1: ListNode, list2: ListNode):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = new_head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            dummy.next = list1
            list1 = list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        dummy = dummy.next

    if list1:
        dummy.next = list1
    elif list2:
        dummy.next = list2

    return new_head.next


# -----------------------------------------------------------
ln1 = ListNode(1)
ln1.next = ListNode(5)
ln1.next.next = ListNode(10)

ln2 = ListNode(2)
ln2.next = ListNode(3)
ln2.next.next = ListNode(7)
ln2.next.next.next = ListNode(12)
ln2.next.next.next.next = ListNode(15)

sorted_list = mergeTwoLists(ln1, ln2)
ListNode.print_linked_list(sorted_list)
ListNode.print_linked_list(ln1)
ListNode.print_linked_list(ln2)

