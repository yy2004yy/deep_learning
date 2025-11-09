# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0) # 哨兵节点
        current = head     # 存放链表表头地址
        carry = 0          # 进位

        while l1 or l2 or carry:          # 当l1、l2都不为None且carry不为0的时候
            val1 = l1.val if l1 else 0    # l1的值
            val2 = l2.val if l2 else 0    # l2的值

            add_sum = val1 + val2 + carry # 求和
            carry = add_sum // 10         # 十位数（修正：使用//整除）
            digit = add_sum % 10          # 个位数

            current.next = ListNode(digit)  # 创建新节点
            current = current.next         # 移动current指针

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return head.next # 返回指向真实结果链表的头节点（.next的作用是跳过虚假表头0）

# 辅助函数：创建链表
def create_linked_list(arr):
    """根据数组创建链表"""
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# 辅助函数：打印链表
def print_linked_list(head):
    """打印链表的值"""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    print(" -> ".join(result))

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("测试示例1: l1 = [2,4,3], l2 = [5,6,4]")
    l1 = create_linked_list([2, 4, 3])  # 表示数字 342
    l2 = create_linked_list([5, 6, 4])  # 表示数字 465
    result1 = solution.addTwoNumbers(l1, l2)
    print("输入l1: ", end="")
    print_linked_list(l1)
    print("输入l2: ", end="")
    print_linked_list(l2)
    print("输出结果: ", end="")
    print_linked_list(result1)
    print("解释: 342 + 465 = 807\n")
    
    print("测试示例2: l1 = [0], l2 = [0]")
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result2 = solution.addTwoNumbers(l1, l2)
    print("输入l1: ", end="")
    print_linked_list(l1)
    print("输入l2: ", end="")
    print_linked_list(l2)
    print("输出结果: ", end="")
    print_linked_list(result2)
    print("解释: 0 + 0 = 0\n")
    
    print("测试示例3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]")
    l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])  # 表示数字 9999999
    l2 = create_linked_list([9, 9, 9, 9])           # 表示数字 9999
    result3 = solution.addTwoNumbers(l1, l2)
    print("输入l1: ", end="")
    print_linked_list(l1)
    print("输入l2: ", end="")
    print_linked_list(l2)
    print("输出结果: ", end="")
    print_linked_list(result3)
    print("解释: 9999999 + 9999 = 10009998\n")
    
    # 额外测试：不同长度的链表
    print("额外测试: l1 = [1], l2 = [9,9,9]")
    l1 = create_linked_list([1])          # 表示数字 1
    l2 = create_linked_list([9, 9, 9])    # 表示数字 999
    result4 = solution.addTwoNumbers(l1, l2)
    print("输入l1: ", end="")
    print_linked_list(l1)
    print("输入l2: ", end="")
    print_linked_list(l2)
    print("输出结果: ", end="")
    print_linked_list(result4)
    print("解释: 1 + 999 = 1000")