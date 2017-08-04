import random
def diliver(i,people):#在一共people人中，第i号玩家将自己的钱随机给其它人
    a = random.randint(0,people-2)
    if a < i:
        return a
    else :
        return a+1

def one_loop(s,people):#在people人中，所有人轮流给一次钱。
    for i in range(people):
        
        s[i]-=1
        a = diliver(i,people)
        s[a]+=1
    return s

def count_loop(loop):
    max_count=0
    min_count=0
    for i in range(10):
        s =[]
        people=100
        for i in range(people):
            s.append(100)
        for i in range(loop):
            s=one_loop(s,people)
        max_count+=max(s)
        min_count+=min(s)
    print("%d次回合后最大值平均值为%d"%(loop,max_count/10))
    print("%d次回合后最小值平均值为%d"%(loop,min_count/10))

def count_loop_init(loop):
    max_count=[]
    min_count=[]
    much_count=[]
    little_count=[]
    people_count=[]
    for i in range(10):
        s =[]
        people=100
        for i in range(people):
            s.append(100)
        for i in range(loop):
            s=one_loop(s,people)
            for k in s:
                if k==0:
                    s.remove(0)
                    people-=1
                    #print(people,len(s),i)
        much_count.append([k>150 for k in s].count(True))
        little_count.append([k<50 for k in s].count(True))
        max_count.append(max(s))
        min_count.append(min(s))
        people_count.append(people)
    print("%d次回合后最大值平均值为%d"%(loop,sum(max_count)/10))
    print("%d次回合后最小值平均值为%d"%(loop,sum(min_count)/10))
    print("%d次回合后还有%d名玩家"%(loop,sum(people_count)/10))

loopa = 100;
loopb = 200;
loopc = 300;
loopd = 600;
loope = 1000;
loopf = 20000;
count_loop(loopa);
count_loop(loopb);
count_loop(loopc);
count_loop(loopd);
count_loop(loope);
count_loop(loopf);

count_loop_init(loope)
