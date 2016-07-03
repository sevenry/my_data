###二叉树算法。参看统计学习方法第五章所给思路所写。

class decisionnode:
  def __init__(self,results=None,tb=None,fb=None):
    self.results=results
    self.tb = tb
    self.fb = fb

def devideset(data,loc):
    n=len(data)
    left=[]
    right=[]
    for j in range(n):
        if j<=loc:
            left.append(data[j])
        else:
            right.append(data[j])
    return left,right

def build_tree(data,demand):
    if len(data)==1:return decisionnode()

    loc,ending=make_loc(data)
    print(ending,data[loc],'jj')
    if ending<demand:
        return decisionnode(results=ending)
    else:
        set1,set2=devideset(data,loc)
        nleft=build_tree(set1,demand/2)
        nright=build_tree(set2,demand/2)
        return decisionnode(tb=nleft,fb=nright)


def make_loc(data):
    ending=999999999
    ly=ry=0
    N=len(data)
    left=right=[]
    for i in range(N-1):
        left,right=devideset(data,i)
        
        lmin=get_min(left)
        rmin=get_min(right)
            
        whole=lmin+rmin
        #print(i,whole)
        if whole<ending:
            ending=whole
            loc=i
            #print(i,whole,'hh')
            
    return loc,ending
 
'''
def get_min(data):

    y=0
    for num in data:
        y=y+(num-x)*2
    x=4
    return y'''
 
def get_min(data):###由于是二次函数，所以平方和最低值点在平均值处取得。
    y=0
    s=0
    for num in data:
        s += data
    ave=s/len(data)
    for num in data:
        y=y+(num-ave)*2
    return y












