# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        resultList = ListNode()
        head = resultList

        while True:
            if list1 and (not list2 or list1.val <= list2.val):
                resultList.next = list1
                list1 = list1.next
            elif list2:
                resultList.next = list2
                list2 = list2.next
            else:
                return head.next
            resultList = resultList.next
                

        