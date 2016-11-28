
#100 删除排序数组中的重复数字
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        k = len(A)-1
        #print('new')
        for i in range(k):
            #print(i,k,'w',A)
            if A[i]==A[i+1]:
                #k=i
                A.remove(A[i])
                self.removeDuplicates(A)
                break
        
        return len(A)

class Solution:#memory limit不会出现解法
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        k = len(A)-1
        #print('new')
        i = 0
        while i < k:
            if A[i]==A[i+1]:
                A.remove(A[i])
                k-=1
            else:
                i+=1
        return len(A)
        
#101 删除排序数组中的重复数字2 
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        for i in range(len(A)-2):
            if A[i]==A[i+1]==A[i+2]:
                A.remove(A[i+2])
                self.removeDuplicates(A)
                break
        return len(A)

class Solution:#memory limit 不会出现解法
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        k = len(A)-2
        i = 0
        while i< k:
            if A[i]==A[i+1]==A[i+2]:
                A.remove(A[i+2])
                k -= 1
            else:
                i+=1
        return len(A)

#109 数字三角形 怀疑题目出错
class Solution:
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        # write your code here
        ans = []
        s=0
        for i in range(len(triangle)):
            ans.append(min(triangle[i]))
        for num in ans:
            s+=num
        return s
        
#110 最小路径和 没想通

#111 爬楼梯
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        a=int(n/2)
        #b=n%2
        ans = 1
        for i in range(1,a+1):
            num1=1
            k=n-i
            #print('w',i)
            for j in range(i):
                num1=num1*(k-j)/(j+1)
                #print('aa',num1,j)
            #print(i,num1)
            ans+=num1
        return ans                    

#112 删除排序链表中的重复元素
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        a = ()
        if head == None:return None
        elif head!=None:a+=(head,)
        while head.next!=None:
            if head.val == head.next.val:
                head.next =head.next.next
            else:
                head = head.next
        return a[0]

#114 不同的路径 
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        if m==1 or n ==1:return 1
        if m==2:return n
        if n==2:return m
        else: 
            a = self.uniquePaths(m-1,n)
            b = self.uniquePaths(m,n-1)
            return a+b

class Solution:## 不超时版本，这种方法记录下之前的计算过程，避免了重复计算。
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        # write your code here
        s = []
        for i in range(m):
            s.append([])
            for j in range(n):
                if i==0 or j==0: a=1
                #elif i==1:a=j+1
                #elif j==1:a=i+1 这两行可以删去。
                else:
                    a = s[i-1][j]+s[i][j-1]
                s[i].append(a)
        return s[m-1][n-1]

#115 不同的路径2 
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        return self.count_route(obstacleGrid,m,n)
        
    def count_route(self,grid,m,n):
        if m==1:
            if 1 in grid[0][:n]: return 0
            else: return 1

        if n == 1:
            if grid[m-1][0]==1:return 0
            else: 
                return self.count_route(grid,m-1,n)
            
        else:
            if grid[m-1][n-1]==1: 
                return 0
            else:
                return self.count_route(grid,m-1,n)+self.count_route(grid,m,n-1)
 
class Solution:#不超时版本，解决方案同上
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        s = []
        for i in range(m):
            s.append([])
            for j in range(n):
                if i == 0:
                    if j == 0:
                        if obstacleGrid[i][j]==1:a=0
                        else:a=1
                    else:
                        if obstacleGrid[i][j]==1:a=0
                        else:a=s[i][j-1]
                else:
                    if j == 0:
                        if obstacleGrid[i][j]==1:a=0
                        else: a = s[i-1][j]
                    else:
                        if obstacleGrid[i][j]==1:a=0
                        else:a=s[i-1][j]+s[i][j-1]
                s[i].append(a)
        return s[m-1][n-1]          

#128 哈希函数
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        hashcode = 0 
        i = len(key)-1
        for word in key:
            c = ord(word)*pow(33,i)
            i-=1
            hashcode += c
        return hashcode%HASH_SIZE

#133 最长单词 1119 ＃＃＃＃＃＃＃＃
class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code 
        length = []
        for word in dictionary:
            length.append(len(word))
        #print(length)
        m = max(length)
        #print(m)
        for i in range(len(length)):
            #print(length[i],dictionary[i])
            if length[i]==m:
                return dictionary[k]

#138 子数组之和
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        for i in range(len(nums)):
            s=nums[i]
            if s == 0:return [i,i]
            begin=i
            for j in range(i+1, len(nums)):
                s+=nums[j]
                if s == 0:
                    end = j
                    return [begin,end]
                                
#141 x的平方根
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        x = int(x)
        
        i = self.decide_length(0,x)
        #print(i)
        begin=pow(10,i)
        end=pow(10,i+1)
        for j in range(begin,end):
            
            if j*j>x:
                return j-1
        
    def decide_length(self,i,x):
        if x<100:return i
        else:
            #print(x,i)
            s = int(x/100)
            if s>=100:
                return self.decide_length(i+1,s)
            else: return i+1

#142 检查2的幂次  
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        while n >2:
            b=n%2
            n=n/2
            if b==1:
                return False
        if n == 2 or n ==1:
            return True
        else:return False
  
class Solution:#利用位运算，时间复杂度降低为O(1)
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n==0:return False
        a=n&(n-1)
        if a ==0:return True
        else:return False

#156 合并区间 不知道为什么不对
class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                intervals[i][1]=intervals[i+1][1]
                intervals.remove(intervals[i+1])
                return self.merge(intervals)
            
        return intervals

#157 判断字符串是否没有重复字符
class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        news = set(list(str))
        if len(news)==len(str):
            return True
        else:
            return False

#165 合并两个排序链表
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        a = ()
        if l1 == None:return l2
        elif l2 == None:return l1
        else:
            while l1!=None:
                new = (l1.val,)
                l1 = l1.next
                a = a + new
            while l2!=None:
                new= (l2.val,)
                a+=new
                l2 = l2.next
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                if a[i]>a[j]:
                    b = a[:i]+(a[j],)+a[i:j]
                    if j<len(a)-1:
                        b+=a[j+1:]
                    a = b
        s = ListNode(a[0])
        for i in range(len(a)-1):
            if i ==0 :y=s
            c = ListNode(a[1+i])
            s.next = c
            s=c
        return y
  
#166 链表倒数第n个节点 time limit
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        a = ()
        if head == None:return None
        while head!=None:
            a += (head.val,)
            head = head.next
        count = len(a) - n
        return ListNode(a[count])          

#167 链表求和 看不懂题目

#173 链表插入排序
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        # write your code here
        a = ()
        if head == None:return None
        while head!=None:
            new = (head.val,)
            a = a + new
            head = head.next
        if len(a)==1:return ListNode(a[0])
        for i in range(1,len(a)):
            for j in range(i):
                k = a[i]
                if k<a[j]:
            
                    b = a[:j]+(a[i],)+a[j:i]
                    if i<len(a)-1:
                        b+=a[i+1:]
                    a=b
        s = ListNode(a[0])
        for i in range(len(a)-1):
            if i ==0 :y=s
            c = ListNode(a[1+i])
            s.next = c
            s=c
        return y

#174 删除链表中倒数第n个节点 time limit
class Solution:
    def removeNthFromEnd(self, head, n):
        # write your code here
        a = ()
        if head == None:return None
        while head!=None:
            a += (head.val,)
            head = head.next
        if len(a)==1:return None
        count = len(a) - n
        if count<len(a)-1:
            a = a[:count]+a[count+1:]
        else:
            a = a[:count]
        s = ListNode(a[0])
        if len(a)==1:return s
        for i in range(len(a)-1):
            if i ==0 :y=s
            c = ListNode(a[1+i])
            s.next = c
            s=c
        return y

#181 将整数A转化为整数B 
class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        newa = bin(a)[2:]
        newb = bin(b)[2:]
        newa,newb = self.modify_num(newa,newb)
        change = 0
        #print(newa,newb)
        for i in range(len(newa)):
            if newa[i]!=newb[i]:
                change+=1
        return change
        
    def modify_num(self, a , b):
        if len(a)==len(b):return a,b
        elif len(a)>len(b):
            b='0'+b
            return self.modify_num(a,b)
        else :
            return self.modify_num(b,a)

class Solution:#解决负数问题
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        # write your code here
        if a>=0:newa = bin(a)[2:]
        else:newa = bin(pow(2,32)+a)[2:]
        if b>=0:newb = bin(b)[2:]
        else:newb = bin(pow(2,32)+b)[2:]
        newa,newb = self.modify_num(newa,newb)
        change = 0
        #print(newa,newb)
        for i in range(len(newa)):
            if newa[i]!=newb[i]:
                change+=1
        return change
        
    def modify_num(self, a , b):
        if len(a)==len(b):return a,b
        elif len(a)>len(b):
            b='0'+b
            return self.modify_num(a,b)
        else :
            return self.modify_num(b,a)

#172 删除元素
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        for num in A:
            if num == elem:
                A.remove(num)
                self.removeElement(A,elem)#这里需要重复调用是因为调用的顺序按照序号来，比如删除了4号后原来的5号成了4号，而
                #函数继续调用5号就是原来的6号，因此会跳过去。
        return len(A),A

#185 矩阵的之字形遍历 没想好

#197 排列序号 没想好
