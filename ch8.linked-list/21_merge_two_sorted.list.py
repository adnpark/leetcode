# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Recursion을 이용한 풀이 1
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


# Recursion을 이용한 풀이 2
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

'''
1. return l1 and l1.next = mergeTwoLists(l1.next, l2) => [1, mergeTwoLists(l1.next, l2)]
2. result of mergeTwoLists(l1.next, l2) is that return l2 and l2.next = mergeTwoLists(l1, l2.next) => [1, 1, mergeTwoLists(l1, l2.next)]
3. result of mergeTwoLists(l1, l2.next) is return l1 and l1.next = mergeTwoLists(l1.next, l2) => [1, 1, 2, mergeTwoLists(l1.next, l2)]
...
'''


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val <= l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2


# 반복문을 이용한 풀이


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node that will serve as the head of the result
        dummy = ListNode(-1)
        prev = dummy

        while l1 and l2:
            if l1.val <= l2.val:  # l1, l2 값을 비교하여 더 낮은 값을 prev.next에 append, 그리고 붙인 값은 날리기
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next  # prev 노드 포인터 next로 옮겨두기, 즉 항상 리스트의 끝에서 시작할 수 있도록 만들기

        # after the loop ends, one of l1 and l2 can still have some nodes;
        # append those nodes to result
        prev.next = l1 if l1 is not None else l2

        return dummy.next
