# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            temp=temp.next
            count+=1
        temp=head
        if count%2 :
            count = count//2
        else :
            count = (count+1)//2

        while temp and count > 0:
            temp = temp.next
            count-=1
        return temp