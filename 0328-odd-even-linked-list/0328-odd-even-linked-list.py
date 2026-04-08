# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        temp = head #100 odd
        t1 = temp.next #200 even
        t2 = t1

        while t1 and t1.next:
            temp.next = t1.next
            temp = temp.next

            t1.next = temp.next
            t1 = t1.next

        temp.next = t2
        return head