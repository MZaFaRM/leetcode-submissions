# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        while True:
            if not (temp and temp.next):
                return head
            elif temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
