#####容易
#1 a+b no answer

#2 尾部的0
class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        s=0
        while n>=5:
            
            n=int(n/5)
            
            s+=n

        return s

#6 合并排序数组
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        A.extend(B)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:
                    min = A[j]
                    
                    A[j]=A[i]
                    A[i]=min
        return A
            
#8 旋转字符串 不知道为啥结果不对
class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        while offset>0:
            news = s[1]
            for i in range(2,len(s)):
                news+=s[i]
            news+=s[0]
            offset-=1
            s=news
            print(news,offset)
        print(news)
        return news

#9 fizz buzz
class Solution:
    """
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        results = []
        for i in range(1, n+1):
            if i % 15 == 0:
                results.append("fizz buzz")
            elif i % 5 == 0:
                results.append("buzz")
            elif i % 3 == 0:
                results.append("fizz")
            else:
                results.append(str(i))
        return results

#13 字符串查找
class Solution:
    def strStr(self, source, target):
        # write your code here
        if target=="":return 0 
        
        for i in range(len(source)):
            #print(source[i])
            if source[i]==target[0]:
                rec = i
                #print(rec)
                
                for j in range(1,len(target)):
                    #print(target[j],source[rec+j],'w')
                    if target[j] != source[rec+j]:break
                    if j == len(target)-1:
                        return rec
        return -1 

#14 二分查找
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        # write your code here
        if target not in nums:return -1
        for i  in range(len(nums)):
            if nums[i]==target:return i

#22 平面列表
class Solution(object):
    def flatten(self, nestedList):
        # Write your code here
        
        keyrec=True
        if type(nestedList) is int:
            return [nestedList]
        while keyrec==True:
            a=[]
            keyrec=False
            for num in nestedList:
                if type(num) is int:
                    a.append(num)
                elif type(num) is list:
                    a.extend(num)
                    keyrec=True
            nestedList = a
            
        return nestedList

#28 搜索二维矩阵 题目看不懂

#30 插入区间 想不好

#35 翻转链表 
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head):#使用tuple而不是list
        # write your code here
        a = ()
        if head == None:return None
        elif head!=None:a+=(head.val,)
        while head.next!=None:
            
            head = head.next
            new = (head.val,)
            a = a + new
        if len(a)==1:
            return ListNode(a[0])
        newlist = ()
        for i in range(len(a)):
            newl = ListNode(a[i])
            newlist+=(newl,)
        for i in range(len(newlist)-1):
            newlist[len(newlist)-1-i].next=newlist[len(newlist)-2-i]
        return newlist[len(newlist)-1]

    def reverse2(self, head):
        # write your code here
        a = []
        if head == None:return None
        elif head!=None:a.append(head.val)
        while head.next!=None:
            
            head = head.next
            a.append(head.val)
        if len(a)==1:
            return ListNode(a[0])
        newlist = []
        for i in range(len(a)):
            newl = ListNode(a[i])
            newlist.append(newl)
        for i in range(len(newlist)-1):
            newlist[len(newlist)-1-i].next=newlist[len(newlist)-2-i]
        return newlist[len(newlist)-1]

    def reverse(self, head):
        # write your code here
        a = []
        if head == None:return None
        elif head!=None:a.append(head.val)
        while head.next!=None:
            a.append(head.next.val)
            head = head.next
        
        if len(a)==1:
            return ListNode(a[0])
        s = ListNode(a[len(a)-1])
        for i in range(len(a)-1):
            if i ==0 :y=s
            c = ListNode(a[len(a)-2-i])
            s.next = c
            s=c
        return y

#39 恢复旋转排序数组 不知道为啥结果不对。同8一样，结果正确，返回值错误
class Solution:
     
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        
        while nums[0]>nums[-1]:
            results = nums[1:]
            results.append(nums[0])
            nums = results
            print(nums)
        return nums

#41 最大子数组 
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if len(nums)==1:return nums[0]
        
        maxf = []
        for i in range(len(nums)):
            a = nums[i]
            s=[a]
            for j in range(i+1, len(nums)):
                a+=nums[j]
                s.append(a)
            maxf.append(max(s))
        maxr=max(maxf)
            #if max(s)>maxf: maxf=max(s)#另一种方法是每次i计算一圈，将最大值与记录的最大值比较，如果更大则更新。
        return maxr

    def maxSubArray(self, nums):###这种方法则是考虑只要有正数，最大的数组不会是负数开头。
        # write your code here
        if len(nums)==1:return nums[0]
        maxi = max(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                a = nums[i]
                if a>maxi:maxi=a
                for j in range(i+1, len(nums)):
                    a += nums[j] 
                    if a>maxi:maxi=a
        return maxi

class Solution: #不超时的解决方法 
#考虑到如果连续两个正数的情况下，那么最大和肯定是由前一个开始；并且如果两个连续和为负，最大和肯定是从之后开始
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        ###这种方法则是考虑只要有正数，最大的数组不会是负数开头。
        # write your code here
        if len(nums)==1:return nums[0]
        maxi = max(nums)
        rec = []
        rec2 = []
        for i in range(len(nums)):
            if nums[i]>0:
                rec.append(i)
        for num in rec:
            #print(num,'w')
            if num==0:rec2.append(num)
            elif num == len(nums)-1:pass
            
            elif nums[num]+nums[num+1]>0 and nums[num-1]<0:
                #print(num,'a')
                rec2.append(num)
        #print(rec)        
        #print(rec2)
        for num in rec2:
            a = nums[num]
            for j in range(num+1, rec[-1]+1):
                #print(nums[j])
                a += nums[j] 
                #print(a,'w')    
                if a<0:break
                elif a>maxi:maxi=a
        
        return maxi                

#44 最小子数组 所以这里还是超时了是为什么啊
class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        if len(nums)==1:return nums[0]
        mini = min(nums)
        rec = []
        rec2 = []
        for i in range(len(nums)):
            if nums[i]<0:
                rec.append(i)
        #print(rec)
        for num in rec:
            #print(num,'w')
            if num==0:rec2.append(num)
            elif num == len(nums)-1:pass
            elif nums[num]+nums[num+1]<0 and nums[num-1]>=0:
                #print(num,'a')
                rec2.append(num)
        print(rec2)
        for i in range(len(rec2)－1):
            num = rec2[i]
            num1 = rec2[i+1]
            
        
        
        for num in rec2:
            a = nums[num]
            for j in range(num+1, rec[-1]+1):
                #print(nums[j])
                a += nums[j] 
                #print(a,'w')    
                if a>0:break
                elif a<mini:mini=a
        
        return mini

#46 主元素
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        
        # write your code here
        rec = set(nums)
        times=[]
        for num in rec:
            if nums.count(num)>len(nums)*0.5:
                return num

#50 数组剔除元素后的乘积 
class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        b =[]
        t = len(A)
        for i in range(t):
            num = 1
            for j in range(t):
                while j!=i:num*=A[j]
            b.append(num)
        return b

class Solution:#不超时版本 考虑到后续的所有计算结果都有前面重复的部分
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        # write your code here
        b = []
        t = len(A)
        news = 1
        for i in range(t):
            num = 1
            num=news
            for j in range(i+1,t):
                num*=A[j]
                
            news*=A[i]
            b.append(num)
        return b
        
#53 翻转字符串
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        
        rec = s.split()
        if rec == []:return ''
        recstr = rec[-1]
        for i in range(len(rec)-1):
            recstr+=' '+rec[len(rec)-i-2]
        return recstr

#55 比较字符串
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        A=list(A)
        for num in B:
            if num in A:
                A.remove(num)
            else:return False
        return True
        
#60 搜索插入位置
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        # write your code here
        if A==[]:return 0
        if A[0]>=target:return 0 
        for i in range(len(A)):
            if A[i]>=target:
                if A[i-1]==target:return i-1
                if A[i-1]<target:return i
        if A[-1]<target:return len(A)

#64 合并排序数组2 好像没看懂题目意思
class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for num in B:
            A.append(num)
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                ts = A[i+1]
                A[i+1]=A[i]
                A[i]=ts
        return A

##66,67,68 二叉树otz 85 93 97 155 175 177 245 375 453 469 480

#66 二叉树的前序遍历 莫名其妙什么危险引用 可能是应该引用规定的节点吧
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
                
class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        tree = Tree1()
        for num in root:
            tree.add(tree.root,num)
        tree.qianxu(tree.root)
       
class Node(object):
    """节点类"""
    def __init__(self, elem=-1, lchild=None, rchild=None):
        if elem=='#':
            self.elem=None
        else:
            self.elem = elem
            self.lchild = lchild
            self.rchild = rchild
 
class Tree1(object):
    def __init__(self):
        self.root = Node()
    
    def position(self,posi):
        newposi=[]
        for current in posi:
            if current.elem==None:posi.remove(current)
            elif current.lchild==None or current.rchild==None:
                return current
        for current in posi:
            newposi+=[current.lchild,current.rchild]
            return self.position(newposi)
        
    def add(self, current=None, elem=-1):
        node = Node(elem)##最新的节点
        if current.elem == -1:            #假设树是空的。则对根节点赋值
            print('initial right')
            self.root = node
        else:
            posi = self.position([self.root])
            print('posi.elem',posi.elem)
            if posi.lchild==None:
                posi.lchild=node
            else:
                posi.rchild = node
        
    def qianxu(self,current=None):
        if current.elem!=None:
            print(current.elem)

            if current.lchild!=None:
                self.qianxu(current=current.lchild)
            if current.rchild!=None:
                self.qianxu(current=current.rchild)
        else:
            print('')

#80 中位数
class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        newn = sorted(nums)
        if len(newn)%2==0:return newn[len(newn)/2-1]
        else:return newn[(len(newn)-1)/2]

#82 落单的数
class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        if A ==[]:return 0
        new = set(A)
        for num in new:
            if A.count(num)<2:return num

#96 链表划分 感觉链表需要单独来做 
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        a = []
        if head == None:return None
        elif head!=None:a.append(head.val)
        while head.next!=None:
            head = head.next
            a.append(head.val)
            
        if len(a)==1:
            return ListNode(a[0])
        i=0
        k = len(a)
        while i < k:
            if a[i]>=x:
                a.append(a[i])
                a.remove(a[i])
                k-=1
            else:
                i+=1
        newlist = []
        for i in range(len(a)):
            newl = ListNode(a[i])
            newlist.append(newl)
        for i in range(len(newlist)-1):
            newlist[i].next=newlist[i+1]
        return newlist[0]

class Solution:#使用tuple
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        # write your code here
        a = ()
        if head == None:return None
        elif head!=None:a+=(head.val,)
        while head.next!=None:
            head = head.next
            a+=(head.val,)
            
        if len(a)==1:
            return ListNode(a[0])
        i=0
        k = len(a)
        while i < k:
            if a[i]>=x:
                a+=(a[i],)
                a = a[:i]+a[i+1:]
                k-=1
            else:
                i+=1
        newlist = ()
        for i in range(len(a)):
            newl = ListNode(a[i])
            newlist+=(newl,)
        for i in range(len(newlist)-1):
            newlist[i].next=newlist[i+1]
        return newlist[0]
