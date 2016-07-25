
import random

def runastep1():
    a=random.random()
    if a>0.5:
        return 1
    else:
        return -1
        
def catch1(step=100):##设定的最大步数
    k=1
    i=0
    while i < step:
        i+=1
        k += runastep()
        if k==0:return 1
    if k==0:print(k)
    if k>0:
        return 0

def countmay1(time=10000,s=1000):##测试的数据总量和最大步数
    count=0
    for i in range(time):
        count+=catch(step=s)
    return count/time
        

###2d

def runastep2(num):
    a=random.random()
    b=random.random()
    
    if a>0.5:
        if b>0.5:
            num[0]+=1
        else:
            num[0]-=1
    else:
        if b>0.5:
            num[1]+=1 
        else:
            num[1]-=1
    return num 
        
def catch2(step=1000):##设定的最大步数
    k=[1,1]
    i=0
    while i < step:
        i+=1
        k = runastep(k)
        if k[0]==0:return 1
    return 0

def countmay2(time=10000,s=10000):##测试的数据总量和最大步数
    count=0
    for i in range(time):
        count+=catch(step=s)
    return count/time
 
##3d 
def runastep(num):
    a=random.random()
    b=random.random()
    if a>0.5:
        if b>1/3:
            num[0]+=1
            
        else:
            if b < 2/3:
                num[1]+=1
            else:
                num[2]+=1
    else:
        if b>1/3:
            num[0]-=1
        else:
            if b < 2/3:
                num[1]-=1
            else:
                num[2]-=1
    return num 
        
def catch(step=1000):##设定的最大步数
    k=[1,1,1]
    i=0
    while i < step:
        i+=1
        k = runastep(k)
        if k[0]==0:return 1
    return 0

def countmay(time=10000,s=1000):##测试的数据总量和最大步数
    count=0
    for i in range(time):
        count+=catch(step=s)
    return count/time
    
ans=countmay()
print(ans)
















