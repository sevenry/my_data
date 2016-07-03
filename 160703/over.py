from numpy import *
import copy 
M=[23,45,67,34,21]##中心到末端距离，一个中心，5个末端##如果你是7个就加两个数。！需修改
N=[[11,21,24,34,54,34],[24,35,67,52,38,34],[19,22,82,34,56,67],[25,22,33,44,55,32],[43,44,42,17,52,21]]##5*6项，末端到客户端距离。5是末端节点个数，6是客户端个数，如果你是7*18，就按照同样的格式输入进去就好~ ！需修改

F=[1234,2234,2111,2345,2368]##末端中心建设成本，与末端中心个数相符合。！需修改
Q=[13,45,33,25,48,30]##每个客户端需求量，个数与客户端个数相同。！需修改

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
cpi=0.5#非自提的单位时间等待成本##可能和i,j有关 ！有关则需修改！

hmin=33
hmax=90

def P_value(X):
    P=[]
    for i in range(mcount):
        P.append(0)
        for j in range(ncount):
            P[i]+=Q[j]*X[i][j]
    return P
 
def Z_value(X):
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
            print("please check the X ! something wrong!")##出现这行则说明代码有误。
    return Z
    
def Z_choice(Z):
    Z_record=[]
    for i in range(len(Z)):
        if Z[i]==1:
            
            Z_record.append(i)
    return Z_record
        
def cost_dis(X,W,P):
    S1=0
    S2=0
    for i in range(mcount):
        S1+=M[i]*P[i]*ca
        for j in range(ncount):
            S2+=N[i][j]*Q[j]*X[i][j]*cb*(1-W[j])
    return S1+S2

def cost_cold(X,W,P):
    S1=0
    S2=0
    for i in range(mcount):
        S1+=(fa+ha)*M[i]/va*P[i]
        for j in range(ncount):
            S2+=(fb+hb)/vb*N[i][j]*Q[j]*X[i][j]*(1-W[j])
    return S1+S2
   
def cost_old(Z):
    S=0
    for i in range(mcount):
        S+=F[i]*Z[i]
    return S

def up_cost(X,W):
    P=P_value(X)
    Z=Z_value(X)
    all=cost_cold(X,W,P)+cost_dis(X,W,P)+cost_old(Z)+value_extra(X)
    return all

def cost_peop(X,W):
    S=0
    for i in range (mcount):
        for j in range(ncount):
            S+=cij*X[i][j]*Q[j]*N[i][j]*W[j]
    return S
    
def cost_wait(X,W):
    S=0
    for i in range(mcount):
        for j in range(ncount):
            S+=cpi*X[i][j]
    return S

def down_cost(X,W):
    all=cost_peop(X,W)+cost_wait(X,W)
    return all

def set_xij(X,i,j,k):
    if i == k or k >mcount or k <0:
        print('wrong! give a wrong k !')##出现这行则说明代码有误。
        return X
    else:
        X[k][j]=X[i][j]
        X[i][j]=0
        return X
    
def X_init(k):
    X0=zeros((mcount,ncount))
    for j in range(ncount):
        if k==0:
            i = random.randint(mcount)
            X0[i][j]=1
        else:
            i = random.choice(k)
            X0[i][j]=1
    return X0
    
def W_init():
    W0=zeros((1,ncount))
    W0=W0[0]
    for j in range(ncount):
        W0[j]=random.randint(2)
    
    return W0
    
def random_up(W,k):
    end=99999999999
    for upt in range (60):##初始随机生成个数，！可修改。
        Xinit=X_init(k)
        endtry=up_cost(Xinit,W)##考虑到后续爬山法的无效性。应该选择该行。
        #endtry,Xtry=climb_X(Xinit,W)
        if endtry<end:
            end = endtry
            Xbest=copy.deepcopy(Xinit)
    return end,Xbest
    
def climb_X(X,W):
    best=up_cost(X,W)
    Xbest=copy.deepcopy(X)
    for j in range (ncount):
       for i in range (mcount):
            if X[i][j]==1:
                for addcount in range (5):
                    k=i-2+addcount
                    if k>=0 and  k<mcount and k!=i:
                        X1=set_xij(X,i,j,k)
                        cost1=up_cost(X1,W)
                        if cost1<best:
                            best=cost1
                            Xbest=copy.deepcopy(X1)
                break
    return best,Xbest
   
def random_down(X):
    end=99999999999
    for upt in range(20):##初始随机生成个数！可修改。
        Winit=W_init()
        endtry=down_cost(X,Winit)
        if endtry < end :
            end = endtry
            Wbest = Winit
    return end, Wbest
    
def value_extra(X):
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
    return S1+S2   
            
lines=[]
for i in range (mcount):
    lines.append(0)

def allinall(k=True):
    Wbest=W_init()
    whole=9999999999999
    error=10000
    time=0
    while time<12:###测试总的迭代次数  
        up_end,Xtry=random_up(Wbest,k)
        time+=1
        down_end,Wtry=random_down(Xtry)
        extra=value_extra(Xtry)
        real_up=up_cost(Xtry,Wtry)
        money=real_up+down_end+extra
        if money<whole:
            error=whole-money
            whole=money
            Xbest=copy.deepcopy(Xtry)
            Wbest=copy.deepcopy(Wtry)
            if error < 10:
                time+=1
            else:time=0
        else:
            time+=1
    return whole,Xbest,Wbest

for i in range(2):###得出多组计算结果，记录分别选择的中心，！可修改
    price,XXX,WWW=allinall(k=0)
    Z=Z_value(XXX)
    Z_record=Z_choice(Z)
    for number in Z_record:
        lines[number]+=1
    new_lines=argsort(lines)
    
kk=new_lines[1:]###我这里是5个中心，输出1,2,3,4四个，如果之后是7个中心，输出最高的4个，则改成[3:],即3,4,5,6；如果输出最高的3个，改成[4:]，即4,5,6。！可修改
kk=list(kk)
print(kk)

best_price=99999999999
for i in range(2):##在筛选后的几个中心中再次多组计算，！可修改
    price,XXX,WWW=allinall(kk)
    Z=Z_value(XXX)
    Z_record=Z_choice(Z)
    print(i,Z_record)
    if price<best_price:
        best_price=price
        best_xline=copy.deepcopy(XXX)
        best_wline=copy.deepcopy(WWW)
    print(best_price)##可参看多次输出的价格结果，不想查看则在print前加'#'。！可修改
    
up=up_cost(best_xline,best_wline)
down=down_cost(best_xline,best_wline)
extra=value_extra(best_xline)
money=up+down+extra    
print(money,'down')##验证此处的计算结果与之前的结果一致，说明确实是由对应X和W序列生成。
#print(best_xline)##输出对应最优价格的X序列
print(best_xline[1])
print(best_wline)##W序列
print(P_value(best_xline))#P序列
print(Z_value(best_xline))#Z序列










