from utils import ListNode

def has_cycle(head: ListNode) -> bool:
    try:
        slow = head
        fast = head.next

        while slow != fast:
            slow = slow.next
            fast = fast.next.next

        return True
    except:
        return False