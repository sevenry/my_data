#366 斐波那契
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        a=[0,1]
        if n ==1:return a[0]
        if n==2:return a[1]
        elif n>2:
            for i in range(2,n+1):
                new=a[i-2]+a[i-1]
                a.append(new)
                
            return a[n-1]

#452 删除链表中的元素 null why 放入链表
class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        new = []
        for num in head:
            if num == val:
                head.remove(num)
        return head

#463 整数排序
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:
                    min1 = A[j]
                    A[j]=A[i]
                    A[i]=min1
        return A

