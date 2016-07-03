from numpy import *
import copy 
M=[23,45,67,34,21]##中心到末端距离，一个中心，5个末端
N=[[11,21,24,34,54,34],[24,35,67,52,38,34],[19,22,82,34,56,67],[25,22,33,44,55,32],[43,44,42,17,52,21]]##5*6项，末端到客户端距离。5是末端节点个数，6是客户端个数
##M,N均为list，N[2][3]形式调用
F=[1234,2234,2111,2345,2368]##末端中心建设成本，与末端中心个数相符合
Q=[13,45,33,25,48,30]##每个客户端需求量，个数与客户端个数相同

mcount=len(M)
ncount=len(N[0])

#a,b车单位距离的成本及速度，冷藏成本及折旧费
ca=3
cb=2
va=100
vb=80
fa=123
fb=89
ha=34
hb=23

cij=1.3#自提的单位距离人工成本##可能和i,j有关
cpi=0.5#非自提的单位时间等待成本##可能和i,j有关

hmin=33#P[i]的最低与最高范围值。
hmax=90

X0=zeros((mcount,ncount))##填入末端个数和客户端个数##ndarray,X[2,3]形式
W0=mat(zeros((1,ncount)))##填入1和客户端个数##matrix

def P_value(X):##末端节点货运量
    P=[]##生成list
    for i in range(mcount):
        P.append(0)
        for j in range(ncount):
            P[i]+=Q[j]*X[i][j]
        #print(P[i])
    return P

def Z_value(X):##根据X得到Z
    Z=[]
    for i in range(mcount):
        Z.append(0)
        for j in range(ncount):
            if X[i][j]==1:
                Z[i]=1
    for j in range(ncount):
        test=0
        for i in range(mcount):
            if X[i][j]==1:
                test+=1
        if test>1:
            print("please check the X ! something wrong!")
    return Z
    
def zzz(X):##调试函数和Z_value()第一个循环作用一样，但是continue和break都难以实现该目标。
#continue是结束当前i，j的循环，进入下一个j+1；break是打破现在j，进入下一个i+1循环，都很难准确做到0/1计数。
    z=[]
    for i in range(mcount):
        for j in range(ncount):
            if X[i][j]==1:
                z.append(1)
                #print(i,j)
                break
            z.append(0)
    return z

def Z_choice(Z):#返回选中的末端节点
    Z_record=[]
    for i in range(len(Z)):
        if Z[i]==1:
            
            Z_record.append(i)
    return Z_record
        
def cost_dis(X,W,P):#运输费用
    S1=0
    S2=0
    for i in range(mcount):
        S1+=M[i]*P[i]*ca
        #print(S1)
        for j in range(ncount):
            S2+=N[i][j]*Q[j]*X[i][j]*cb*(1-W[j])
        #print(S2)
    return S1+S2

def cost_cold(X,W,P):#冷藏成本
    S1=0
    S2=0
    for i in range(mcount):
        S1+=(fa+ha)*M[i]/va*P[i]
        for j in range(ncount):
            S2+=(fb+hb)/vb*N[i][j]*Q[j]*X[i][j]*(1-W[j])
    return S1+S2
   
def cost_old(Z):#折旧费用
    S=0
    for i in range(mcount):
        S+=F[i]*Z[i]
    return S

def up_cost(X,W):#上层花费
    P=P_value(X)
    Z=Z_value(X)
    all=cost_dis(X,W,P)+cost_cold(X,W,P)+cost_old(Z)+value_extra(X)
    #print(all,'here')
    return all

def cost_peop(X,W):#人工自提成本
    S=0
    #print(W)
    for i in range (mcount):
        for j in range(ncount):
            #print(W[j])
            S+=cij*X[i][j]*Q[j]*N[i][j]*W[j]
    #print(S)
    return S
    
def cost_wait(X,W):#送货等待成本
    S=0
    for i in range(mcount):
        for j in range(ncount):
            S+=cpi*X[i][j]*N[i][j]*(1-W[j])/vb
    #print(S)
    
    return S

def down_cost(X,W):#下层花费
    all=cost_peop(X,W)+cost_wait(X,W)+value_extra(X)
    return all

def set_xij(X,i,j,k):##调整Xij个别值
    if i == k or k >mcount or k <0:
        print('wrong! give a wrong k !')
        return X
    else:
        X[k][j]=X[i][j]
        X[i][j]=0
        return X
    
def X_init(k=0):##随机生成X序列
    X0=zeros((mcount,ncount))##每次需要重新生成X0，否则ndarray随动
    for j in range(ncount):
        if k==0:
            print('lll')
            i = random.randint(mcount)
            X0[i][j]=1
        else:
            i = random.choice(k)
            print(i)
            X0[i][j]=1
    return X0
    
def W_init():##随机生成W序列
    W0=zeros((1,ncount))
    W0=W0[0]#这种方法不好，应该直接生成一个list，而不是把这些0的集合作为其中一列。
    for j in range(ncount):
        W0[j]=random.randint(2)
    
    return W0
    
def random_up(W,k):##上层随机法
    end=99999999999
    for upt in range (60):##初始随机生成个数
        Xinit=X_init(k)
        #print(Xtry)
        endtry=up_cost(Xinit,W)##考虑到后续爬山法的无效性。应该选择该行。
        #endtry,Xtry=climb_X(Xinit,W)
        ##print(endtry,up_cost(Xtry,W),'www')#########不同哎！！！！
        if endtry<end:##因为初始end非常大，所以第一次总会循环到这里，可以生成初始的Xbest，不用提前声明。
            end = endtry
            Xbest=copy.deepcopy(Xinit)
    #print(up_cost(Xbest,W),'rup',end)
    return end,Xbest
    
def climb_X(X,W):##上层爬山
    best=up_cost(X,W)
    #print(best,'init')
    Xbest=copy.deepcopy(X)
    #print(best,up_cost(X,W),'hhh')
    #print(X,'fir')
    for j in range (ncount):
        #print(j,'j')
        for i in range (mcount):
            #print(i,'i')
            #print(X[i][j])
            if X[i][j]==1:
                for addcount in range (5):
                    k=i-2+addcount
                    if k>=0 and  k<mcount and k!=i:
                        #print('k',k)
                        X1=set_xij(X,i,j,k)
                        cost1=up_cost(X1,W)
                        #print(cost1,'cost1')
                        if cost1<best:
                            best=cost1
                            Xbest=copy.deepcopy(X1)##数组的随动性
                            #print(best,up_cost(Xbest,W),'wht')
                            #print('Xbest')
                            #print(Xbest)
                break
    #print(best,'climb')
    #print('xxx')
    #print(Xbest)
        #print(best,up_cost(Xbest,W),'climb')
    return best,Xbest
  
def random_down(X):##下层随机法
    end=99999999999
    for upt in range(30):##初始随机生成个数
        Winit=W_init()
        #print(Winit)
        endtry=down_cost(X,Winit)
        
        #print(endtry,end)
        if endtry < end :
            end = endtry
            Wbest =copy.deepcopy(Winit)
    #print(end,'ran')   
    #print()
    return end, Wbest
    
def value_extra(X):##罚函数
    S2=0
    Z=Z_value(X)
    Z_record=Z_choice(Z)
    P=P_value(X)
    if len(Z_record)!=3:##如果选中的中心不是3个，成本为1000000。！可修改
        S1=1000000
    else:S1=0
    for keys in Z_record:##如果P[i]的值不在区间范围内，惩罚成本为100000。！可修改
        extra=100000*max(0,hmin-P[keys])+100000*max(P[keys]-hmax,0)
        
        S2+=extra
        #print(S2,'S2')
    return S1+S2   
    
lines=[]
for i in range (mcount):
    lines.append(0)
    
def allinall(k):##迭代函数
    Wbest=W_init()
    whole=9999999999999
    error=10000
    time=0
    #print()
    #print('yes!')
    while time<12:###测试总的迭代次数  
        up_end,Xtry=random_up(Wbest,k)###旧的w引用该函数，得到的结果是随机的x和上层，后续是根据得到的x以及新的w生成的下层结果。
        time+=1
        #print(up_end,'up_end',value_extra(Xtry))
        down_end,Wtry=random_down(Xtry)
        extra=value_extra(Xtry)###再加一次，确保无罚函数出现。
        #print('extra',extra)
        real_up=up_cost(Xtry,Wtry)
        money=real_up+down_end+extra
        #print('all',down_end)
        #print(Xtry)
        #print(money,'money')
        if money<whole:
            #print('ok!')
            error=whole-money
            whole=money
            Xbest=copy.deepcopy(Xtry)
            Wbest=copy.deepcopy(Wtry)
            if error < 10:
                time+=1
            else:time=0
        else:
            time+=1
        #print(time,'time')
        #print(whole,'whole')
        ###遗传尝试
        
        #print(Wold)
        #print(Z_record)
    return whole,Xbest,Wbest
 
k=[0,3,4]
#w= W_init()
#random_up(w,k)
x=X_init()
print(x[:,0])


for i in range(20):###初次循环得到被选中频率较高的末端中心
    price,XXX,WWW=allinall(k=0)
    Z=Z_value(XXX)
    Z_record=Z_choice(Z)
    for number in Z_record:
        lines[number]+=1
    #print(lines)
    new_lines=argsort(lines)###按照数字从小到大顺序返回对应的序列号
    #print(new_lines)

kk=new_lines[1:]
kk=list(kk)##转化成list才能在X_init()中完成选择

best_price=99999999999
for i in range(5):###再次循环，在较高频率的末端中心中进行随机选择。
    price,XXX,WWW=allinall(kk)
    if price<best_price:
        #print(price,best_price)
        best_price=price
        #print(best_price,'p')
        best_xline=copy.deepcopy(XXX)
        best_wline=copy.deepcopy(WWW)
    print(best_price,'jjj')##总价
#print(best_wline)
    #print(best_wline)

up=up_cost(best_xline,best_wline)
down=down_cost(best_xline,best_wline)
extra=value_extra(best_xline)
money=up+down+extra    
print(money,'down')##验证总价与对应的X和W序列一致。


















