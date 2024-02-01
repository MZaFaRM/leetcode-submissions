class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = j = head

        for _ in range(n):
            j = j.next

        if not j:
            return head.next

        while j.next:
            i = i.next
            j = j.next

        i.next = i.next.next
        return head