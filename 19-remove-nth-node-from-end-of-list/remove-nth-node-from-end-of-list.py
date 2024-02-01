class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = i = j = ListNode(next=head)

        for _ in range(n):
            j = j.next

        while j.next:
            i = i.next
            j = j.next

        i.next = i.next.next
        return dummy.next