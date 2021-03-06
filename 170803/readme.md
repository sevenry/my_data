##问题：
###屋子里有一百人，每人一百块钱。依次轮流随机挑取一个人，给对方一块钱，所有人给出一块钱的过程称为一轮。多轮后，大家手中的钱财状况是怎么样的？
###代码很简单，我这里设立了附加规则，每一轮结束后，检查大家手中的钱数，如果为0，则玩家退出。
###这里有三种方案判定玩家退出：一，某玩家给出后手中无钱即退出，二，一轮结束后，手中无钱退出；三，轮到某玩家该给钱时，无钱则退出。
###方案一和方案三的实现难度较方案二更大，因为属于一轮循环中途退出，此次循环的总人数发生改变，给钱的策略需要调整，因此选择方案二，同样我个人也觉得方案二较方案一更为合理，较方案三对其它玩家更为公平些。
###这里提供了python和java编写的两个版本。python更为简洁，java的运行更快。

##下面给出利用java运行的结果，这里是不考虑玩家退出的，即玩家可以负债。
####100回合后最大值平均值：  126
####100回合后最低值平均值：  76
####300回合后最大值平均值：  144
####300回合后最低值平均值：  58
####800回合后最大值平均值：  173
####800回合后最低值平均值：  26
####1000回合后最大值平均值：  173
####1000回合后最低值平均值：  22
####3000回合后最大值平均值：  244
####3000回合后最低值平均值：  -34
####8000回合后最大值平均值：  325
####8000回合后最低值平均值：  -113
####12000回合后最大值平均值：  389
####12000回合后最低值平均值：  -170
####20000回合后最大值平均值：  471
####20000回合后最低值平均值：  -265
####50000回合后最大值平均值：  721
####50000回合后最低值平均值：  -506
###100000回合后最大值平均值：  958
####100000回合后最低值平均值：  -645
####200000回合后最大值平均值：  1144
####200000回合后最低值平均值：  -979
####500000回合后最大值平均值：  1759
####500000回合后最低值平均值：  -1637
###从这里可以看出，随着回合次数的增加，最大值平均值与100的差值，最小值平均值与100的差值的增加几乎是一定的。说明这个游戏不会随着次数的增加而趋向我们认知的浮动在100左右。
###我的理解是这样的：对于每个个体来说，每一回合中自己给出一块钱，同时期望也是1块钱，意味着在每一回合结束时，自己最有可能的结果是保持100不变。但是对整个系统来说，所有人保持100不变反而成了个小概率事件，某些人钱数增加某些人钱数降低的可能性反而更高。那么在每一回合结束之后，钱财分布其实对下一回合是没有影响的。也就是说，多次回合下来，部分玩家输的次数较多，部分玩家赢的较多，很可能是个更高概率的事件。
###此外，对于我们所认为的，次数越多应该越平均的直觉来看，也是可以理解的。这里的“越平均”基于的是频率而不是频数。如同掷硬币问题，抛硬币次数越多，正反面出现的概率越接近0.5，而正反面出现的次数可能差的更多。因此在这里，最高值、最低值平均值与初始值100的差值虽然随着回合数的增加在不断增加，但是实际上与回合次数的比值是在不断降低的。
###这里容易让人产生错觉的原因是，我们概念里的平均是频率而不是频数，而问题里比较的是频数，因此随着回合数增加，有人钱越来越少甚至负债等，是很可以理解的。
####20000回合后最大值平均值：  435
####20000回合后最低值平均值：  32
####20000回合后平均还有51玩家
####200000回合后最大值平均值：  1097
####200000回合后最低值平均值：  76
####200000回合后平均还有18玩家
####500000回合后最大值平均值：  1653
####500000回合后最低值平均值：  100
####500000回合后平均还有11玩家
###当经过500000回合后还剩11玩家，我们可以认为，随着回合的增加，游戏人数会不断降低，现在我们来讨论一下极限值，是否会少到只剩一个玩家？因此我设定初始人数为10人，每人手中500元。
####50000回合后最大值平均值：  775
####50000回合后最低值平均值：  93
####50000回合后平均还有10玩家
####500000回合后最大值平均值：  1464
####500000回合后最低值平均值：  100
####500000回合后平均还有5玩家

####5000000回合后最大值平均值：  3141
####5000000回合后最低值平均值：  100
####5000000回合后平均还有2玩家

###我测试了几组来看，很难一家独大，最后几乎都是两个玩家。
###总结：各个玩家手中的钱财数从数额来说，不会随着回合的增加趋于平均，但是与初始值的差值，确实随着回合的增加，与回合数的比值降低，即从频率上来说，确实是在趋于平均。如果设置退出机制，那么游戏玩家会不断减少，但是似乎很难降低到一个人。