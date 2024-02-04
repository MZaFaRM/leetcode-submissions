class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = temp = ListNode(val=float("inf"))
        lists = [l for l in lists if l]

        while lists:
            min_index = 0
            for i in range(len(lists)):
                if lists[i] and lists[i].val < lists[min_index].val:
                    min_index = i
            temp.next = lists[min_index]
            temp = temp.next
            if lists[min_index].next:
                lists[min_index] = lists[min_index].next
            else:
                lists.pop(min_index)

        return head.next