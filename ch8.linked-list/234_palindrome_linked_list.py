# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        deq = deque()
        current_node = head
        while current_node is not None:
            deq.append(current_node.val)
            current_node = current_node.next

        for index, item in enumerate(deq):
            left = deq[index]
            right = deq[0 - (index + 1)]
            if index >= len(deq) // 2:
                break
            if left != right:
                return False
        return True


# 리스트 변환 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: List = []

        if not head:
            return True

        node = head
        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():  # pop()을 이용해 리스트의 앞뒤 원소를 제거하면서 비교
                return False
        return True

# 데크를 이용한 최적화 풀이


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        q: Deque = collections.deque()

        if not head:
            return True

        node = head
        # 데크 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 펠린드롬 판별
        while len(q) > 1:
            if q.popLeft() != q.pop():  # O(n)이 걸리는 pop()과 달리 deque의 popLeft()는 O(1)의 복잡도를 가짐
                return False
        return True


# 런너를 이용한 우아한 풀이
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next  # 역순으로 left half 리스트 만들기
        if fast:  # list 길이가 홀수인 경우 중간 값은 비교에서 제외하기
            slow = slow.next

        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev  # rev가 None이 아니라면 위 조건 확인에서 실패했다는 의미
