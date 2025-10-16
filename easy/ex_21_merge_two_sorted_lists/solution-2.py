# =========================================================
# This solution does not change the original lists.
# =========================================================

from utils import ListNode

def mergeTwoLists(list1: ListNode, list2: ListNode):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    dummy = new_head = ListNode()
    p1, p2 = list1, list2
    while p1 and p2:
        if p1.val < p2.val:
            dummy.next = ListNode(p1.val)
            p1 = p1.next
        else:
            dummy.next = ListNode(p2.val)
            p2 = p2.next
        dummy = dummy.next

    while p1:
        dummy.next = ListNode(p1.val)
        p1 = p1.next
        dummy = dummy.next

    while p2:
        dummy.next = ListNode(p2.val)
        p2 = p2.next
        dummy = dummy.next

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
