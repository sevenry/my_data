#204 单例 ＃＃＃＃感觉这一类的也要单独刷

#212 空格替换 感觉题目出错了
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        a = len(string)
        news = ''
        for s in string:
            if s!=' ':news+=s
            if s==' ':news+='%20'
                
        return news

#227 栈 再说吧＃＃＃＃＃＃＃

#365 二进制中有多少个1 
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        if num>=0:newn = bin(num)[2:]
        else:newn = bin(pow(2,32)+num)[2:]
        #newn = bin(num)[2:]
        count = 0
        #print(newn)
        for i in newn:
            #print(i)
            if i=='1':
                count+=1
            #print(count)
        return count

#372 在O(1)时间复杂度删除链表节点 感觉题目出错了otz

#373 奇偶分割数组 需注意：挨个排序的时候，一旦顺序进行变换，并没有必要break再重新调用。
class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]%2<nums[j]%2:
                    rep = nums[j]
                    nums[j]=nums[i]
                    nums[i]=rep
                    #return self.partitionArray(nums)#比如第一个一只排序到第4个发现按照规则，应该4在1位，那么4优先于1，肯定优先于2，3
                    #因此没有必要重新调用函数本身。
                    #break
        return nums
         
#389 判断数独是否合法 
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for line in board:
            if self.count_num(line)==False:
                return False
        
        for i in range(9):
            newl = []
            for line in board:
                newl.append(line[i])
            if self.count_num(newl)==False:return False
            
        for i in [0,3,6]:
            for m in [0,3,6]:
                newl = []
                for j in range(i,i+3):
                    for k in range(m,m+3):
                        newl.append(board[j][k])
                if self.count_num(newl)==False:return False
        return True
            
    def count_num(self, line):
        newl=[]
        for num in line:
            if num!='.':
                num = int(num)
                newl.append(num)
        for i in range(1,10):
            if newl.count(i)>1:return False
        else:return True

#397 最长上升连续子序列
class Solution:
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        # Write your code here
        add_length=self.count_length(A)
        newa = []
        for i in range(len(A)):
            newa.append(A[len(A)-i-1])
        minus_length=self.count_length(newa)
        return max(add_length,minus_length)
        
    def count_length(self,A):
        maxlength=min(1,len(A))
        
        for i in range(len(A)-1):
            flag=True
            length = 1
            for j in range(i,len(A)-1):
                #print(j,'w')
                for k in range(j+1,len(A)):
                    #print(j,k,A[j],A[k])
                    if A[j]>A[k]:   
                        #print(i,j,k,'w')
                        length+=1
                        break
                        
                    else:
                        #print('why',j,k)
                        flag = False
                        break
                if flag == False:
                    #print(flag)
                    #print(j,k,'aa')
                    break
                        
                    
            #print(i,length)
            if length>maxlength:
                maxlength=length
        return maxlength

#407 加1
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        s = 0
        for i in range(len(digits)):
            s+=digits[len(digits)-i-1]*pow(10,i)
        num = s+1
        newd = []
        while num>9:
            a = num%10
            newd.append(a)
            num = int(num/10)
        newd.append(num)
        newn = []
        for i in range(len(newd)):
            newn.append(newd[len(newd)-1-i])
        return newn

#408 二进制求和 注：这里是对二进制本身求和，因此给出的本身都只能转化成正数，除非有溢出的情况。            
class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        newa = int(a,base=2)
        newb = int(b,base=2)
        c = newa+newb
        return bin(c)[2:]

#413 反转整数
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        if n==0:return 0
        if n>0 :
            k=[]
            
            while n >9:
                a = n%10
                n=int(n/10)
                k.append(a)
            k.append(n)
            newd = 0
            for i in range(len(k)):
                newd+=k[i]*pow(10,len(k)-1-i)
            
        if n<0:
            newd = self.reverseInteger(-n)
        
        if len(bin(newd))>34:return 0
        return newd*(abs(n)/n)
        
#415 有效回文串 
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        # Write your code here
        if s =='':return True
        if s == ' ':return True
        s = s.lower()
        news = list(s)
        newst = []
        for st in news:
            if st.isalpha() or st.isnumeric:
                newst.append(st)
        
        n = int(len(newst)/2)
        for i in range(n):
            if newst[i]!=newst[len(newst)-i-1]:
                return False
        return True

#420 报数 不会

#422 最后一个单词的长度
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        if s =='':return 0
        s = s.lower()
        s = s.split(' ')
        while '' in s:
            s.remove('')
            
        return len(s[-1])

#423 有效的括号序列 真是写的肝胆俱裂
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        
        news=list(s)
        
        #print(news,'hh')
        if len(news)%2 > 0: return False
        newt = []
        for i in range(len(news)):
            #print(i,news[i])
            if news[i] in ['(','[','{']:
                newt.append(news[i])
                #print(newt,'w')
            else:
                if len(newt)==0:return False
                #print(newt[-1],news[i],'bij')
                if newt[-1]=='(' and news[i]==')':
                    #print(newt,'(a)')
                    newt.pop(-1)
                elif newt[-1]=='[' and news[i]==']':
                    #print(newt,'[a]')
                    newt.pop(-1)
                elif newt[-1]=='{' and news[i]=='}' :
                    #print(newt,'{a}')
                    newt.pop(-1)
                else: return False
                #print(newt,'www')
        if len(newt)>0:return False
        return True
        
        
    '''    
    def remove_str(self,news,st):
        for i in range(3):
            if news[0]==stleft[i]:
                if news[1]==stright[i]:
                    news.remove(news[1])
                if news[-1]==stright[i]:
                    news.remove(news[-1])
                news.remove(news[0])
         
    def duichen_test(self,news):
        for i in range(len(news)/2):
            if news[i] =='(' and news[len(news)-1-i]!=')':
                return False
            if news[i] == '[' and news[len(news)-1-i] !=']':
                return False
            if news[i] == '{' and news[len(news)-1-i] !='}':
                return False
        return True
        
    def shunxu_test(self,news):
        for i in range(len(news)/2):
            if news[2*i] == '(' and news[2*i+1] !=')':
                return False
            if news[2*i] == '[' and news[2*i+1] !=']':
                return False
            if news[2*i] == '{' and news[2*i+1] !='}':
                return False
        return True
        
    '''

#433 岛屿的个数 啊啊啊无论如何写不出来
class Solution:        
    def numIslands(self, grid):
        # Write your code here
        
        newg = []
        for i in range(len(grid)):##反向计算是为了左下三角形的情况出现。问题是，如果本来存在右下三角形，
            #翻转后再次形成左下三角形影响计数。
            newg.append(grid[len(grid)-1-i])
        #print(newg)
        #count = min(self.island_count(grid),self.island_count(newg))
        count=self.island_count(grid)
        return count
        
    def island_count(self,grid):
        islands = []
        count = 0
        rec = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    rec.append([i,j])
                    islands += self.island_get(i,j)
                    #print(islands,i,j)
                    if [i,j] not in islands:
                        #print('w')
                        count+=1
        for i in range(len(grid)-1):#因此在这里将三角形的情况进行解决，但同时对转折方框的情况考虑出错。
            for j in range(1,len(grid[0])):
                if grid[i][j-1] == 0 and grid[i+1][j-1]==1 and grid[i][j]==1 and grid[i+1][j]==1:
                    
                    print(i,j,'www')
                    count-=1
        #print(islands)
        return count
    
    def island_get(self,hi,sj):
        islands = []
        
        islands.append([hi+1,sj])
        islands.append([hi,sj+1])
        if hi>0 :islands.append([hi-1,sj])
        if sj>0 :islands.append([hi,sj-1])
    
        return islands
    
    def numIslands2(self,grid):
        islands = []
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=self.panduan(grid,i,j)
        return count
                    
    def panduan(self,grid,hi,sj):#这里是想对周边进行判断，但是如果全是1，1个岛屿，得到的结果也是0.
        islands = []
        
        if hi<len(grid)-1:islands.append([hi+1,sj])
        if sj<len(grid[0])-1:islands.append([hi,sj+1])
        if hi>0 :islands.append([hi-1,sj])
        if sj>0 :islands.append([hi,sj-1])
        
        for [i,j] in islands:
            if grid[i][j]==1:
                print(i,j,'w')
                return 0
        return 1
    
    def island_get2(self,hi,sj):#这里是希望通过全周围，计算出所有的岛屿，再加上斜对角的情况。
        for i in range(3):
            for j in range(3):
                if hi-1+i>=0 and sj-1+j>=0:
                    #print(hi-1+i,sj-1+j)
                    islands.append([hi-1+i,sj-1+j])
        #print(hi,sj,islands)
        return islands

#445 余弦相似度
class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    import math
    def cosineSimilarity(self, A, B):
        # write your code here
        if A==[] and B==[]:return 2
        fenzi = 0
        fenmua = 0
        fenmub = 0
        for i in range(len(A)):
            fenzi += A[i]*B[i]
            fenmua += A[i]*A[i]
            fenmub += B[i]*B[i]
        if min(fenmua,fenmub)==0:return 2
        sim = fenzi/math.sqrt(fenmua)/math.sqrt(fenmub)
        return sim
        
#451 两两交换链表中的节点
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        a = 0
        while head!=None and head.next==None:return head
        while head!=None and head.next!=None:
            #print(head.val,'w')
            rep = head
            rep2 = head.next
            
            if head.next.next!=None and head.next.next.next!=None:
                zan = head.next.next.next
                next_head = head.next.next
            elif head.next.next!=None:
                zan = head.next.next
                next_head = None
            else:
                zan = None
                next_head=None
            head = rep2
            head.next = rep
            head.next.next = zan
            #print(head.val,head.next.val,'www')
            if a==0:
                s = head
                a = 1
            
            head = next_head
        return s 

#464 整数排序2 
class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        for i in range(len(A)-1):
            for j in range(i+1,len(A)):
                if A[i]>A[j]:
                    rep = A[i]
                    A[i] = A[j]
                    A[j] = rep
        return A

class Solution:#这个应该是堆排序法，结果是对的，返回值出错
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers2(self, A):
        # Write your code here
        
        if len(A)>1:
            a = int((max(A)+min(A))/2)
            left = []
            right = []
            for num in A:
                if num<=a:left.append(num)
                else:right.append(num)
            left = self.sortIntegers2(left)
            right = self.sortIntegers2(right)
        else:return A
        a = left+right
        print(a)
        return a

#488 快乐数
class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self,n):
        # Write your code here
        return self.count_happy([],n)
        
    def count_happy(self,list1,n):
        list1.append(n)
        newn=[]
        while n>9:
            a = int(n/10)
            b = n%10
            n = a
            newn.append(b)
        newn.append(n)
        if newn==[1]:return True
        else:
            s=0
            for num in newn:
                s+=num*num
                
        #print(s)
        if s in list1:
            return False
        return self.count_happy(list1,s)

#496 玩具工厂 
class Toy:
    def talk(self):
        raise NotImplementedError('This method should have implemented.')

class Dog(Toy):
    # Write your code here
    def talk(self):
        print('Wow')

class Cat(Toy):
    # Write your code here
    def talk(self):
        print("Meow")

class ToyFactory:
    # @param {string} shapeType a string
    # @return {Toy} Get object of the type
    def getToy(self, typea):
        # Write your code here
        if typea=='Cat':
            a = Cat()
            return a
        if typea=='Dog':
            a=Dog()
            return a

#497 形状工厂 
class Shape:
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Triangle(Shape):
    # Write your code here
    def draw(self):
        print("  /\  ")
        print(" /  \ ")
        print("/____\ ")
        
class Rectangle(Shape):
    # Write your code here
    def draw(self):
        print(" ---- ")
        print("|    |")
        print(" ---- ")

class Square(Shape):
    # Write your code here
    def draw(self):
        print(" ---- ")
        print("|    |")
        print("|    |")
        print(" ---- ")

class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == "Triangle":
            a = Triangle()
        elif shapeType == "Square":
            a = Square()
        elif shapeType == "Rectangle":
            a = Rectangle()
        return a
            
#499 单词计数 啊 map不会

#514 栅栏染色 感觉题目出错了
class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        # Write your code here
        #print(n,k,'w')
        if n ==1 :return k
        if n ==2 :return k*k
        else:
            a = self.numWays(n-1,k)
            if n==3:b=1
            else:
                b = self.numWays(n-3,k-1)
            s = k*(a-b)
            #print(k,a,s,'aa')
        return s    
    
#517 丑数
class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        # Write your code here
        if num ==0:return False
        while num%2==0 or num%3==0 or num%5==0:
            if num%2==0:
                num=num/2
            elif num%3==0:
                num=num/3
            else:
                num=num/5
            
        if num == 1: return True
        else :return False

#524 左填充
class StringUtils:
    # @param {string} originalStr the string we want to append to
    # @param {int} size the target length of the string
    # @param {string} padChar the character to pad to the left side of the string
    # @return {string} a string
    @classmethod
    def leftPad(self, originalStr, size, padChar=' '):
        # Write your code here
        a = size - len(originalStr)
        if a==0:return originalStr
        for i in range(a):
            originalStr = padChar + originalStr
        return originalStr

#539 移动0 不懂为什么不对…… 感觉网站有问题
class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        new=[]
        counts = nums.count(0)
        for i in nums:
            if i !=0:new.append(i)
        for i in range(counts):
            new.append(0)
        print(new)
        return new

#547 两数组的交
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    def intersection(self, nums1, nums2):
        # Write your code here
        new1 = set(nums1)
        new2 = set(nums2)
        new = list(new1.intersection(new2))
        return new

#548 两数组的交2 time limit
class Solution:
    # @param {int[]} nums1 an integer array
    # @param {int[]} nums2 an integer array
    # @return {int[]} an integer array
    
    def intersection(self, nums1, nums2):
        new=[]
        rec = set(nums1)
        for num1 in rec:
            if num1 in nums2:
                for i in range(min(nums1.count(num1),nums2.count(num1))):
                    new.append(num1)
        return new
        ##time limit otz

