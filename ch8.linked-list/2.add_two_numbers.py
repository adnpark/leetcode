# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
1. 링크드 리스트를 숫자로 변환한다. 
2. 숫자를 더한다. 
3. 더한 값을 문자열로 변환후 뒤집은 다음 다시 링크드 리스트로 변환해준다.
'''


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1num = self.listToNumber(l1)
        l2num = self.listToNumber(l2)
        print(l1num, l2num)
        sum = l1num + l2num
        return self.numberToList(sum)

    def listToNumber(self, list: Optional[ListNode]) -> int:
        num = 0
        decimal = 0
        while list is not None:
            num += list.val * 10**decimal
            decimal += 1
            list = list.next
        return num

    def numberToList(self, num: int) -> Optional[ListNode]:
        str_num = str(num)
        reversed = str_num[::-1]

        dummy = ListNode(0)
        ptr = dummy
        for digit in reversed:
            ptr.next = ListNode(int(digit))
            ptr = ptr.next
        return dummy.next
