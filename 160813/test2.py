import pandas as pd 
import matplotlib.pyplot as plt 

datas = pd.read_csv('lagou.csv')
datas = datas.drop(['companyLogo','createTime'],axis = 1)#删除无关项
datas = datas.replace(['1-3','3-5'],['1-3年','3-5年'])##处理时间数据

datas = datas[datas['jobNature']=='全职']#排除兼职和实习影响

'''
###城市 第二部分
cities = datas[datas['city'].isin(['北京','上海','广州','深圳','杭州','成都','武汉','南京','郑州','长沙'])]

### 不同城市薪酬
city1 = cities.pivot_table(['salaryMin','salaryMax'],index='city')
city1 = city1.sort_values(by='salaryMin')
city1.plot(kind='bar')
plt.title('工作需求最多的十大城市平均薪资')
plt.show()

##下面这段用不到
city2 = cities.pivot_table('salaryMax',columns='city')
city2 = city2.sort_values()
cities['salaryavg'] = (cities['salaryMin']+cities['salaryMax'])/2
city3 = cities.pivot_table('salaryavg',index='city')
#city2.plot(kind='barh')
#city3.plot(kind='bar')
plt.show()

###北京部分
bj = datas[datas['city'] == '北京']
title={'companySize':'北京招聘情况按照公司规模分类','education':'北京招聘情况按照学历分类','workYear':'北京招聘情况按照工作经验分类','district':'北京招聘情况按行政区分类','positionType':'北京招聘情况按职位领域分类'}

for choice in ['companySize','education','workYear','district','positionType']:
	kk = bj.groupby(choice).size()
	kk.sort(ascending = False)
	#print(kk)
	kk.plot(kind = 'bar')
	plt.title(title[choice])
	plt.show()

#北京／上海针对不同学历及经验薪酬
bj = bj[bj['education'].isin(['本科','大专','学历不限','硕士'])]
bj = bj[bj['workYear'].isin(['1-3年','3-5年','5-10年','不限','应届毕业生'])]
bj1 = bj.pivot_table('salaryMin',index='education',columns='workYear')
#bj1 = bj1.sort_values(by='salaryMin')
bj1.plot(kind = 'barh')
plt.title('上海市薪资水平——学历／工作经验分布')
plt.show()

###城市对学历人数及薪酬
xl = cities[cities['education'].isin(['本科','大专','学历不限','硕士'])]
xl1 = xl.pivot_table('salaryMax',index='education',columns='city',aggfunc=len)
xl2 = xl.pivot_table('salaryMax',index='education',columns='city')
xl1.T.plot(kind='bar',stacked = True)
plt.title('不同城市对不同学历要求招聘人数')
xl2.T. plot(kind='bar')
plt.title('不同城市招聘针对不同学历平均薪酬')
plt.show()

###城市对工作经验人数及薪酬
jy = cities[cities['workYear'].isin(['1-3年','3-5年','5-10年','不限','应届毕业生'])]
jy1 = jy.pivot_table('salaryMin',index='workYear',columns='city',aggfunc=len)
jy2 = jy.pivot_table('salaryMin',index='workYear',columns='city')
jy1.T.plot(kind='bar',stacked= True)
plt.title('不同城市针对不同工作经验招聘人数')
jy2.T.plot(kind='bar')
plt.title('不同城市招聘针对不同工作经验平均薪酬')
plt.show()
'''

##前十职位薪酬，这里主要是按照薪酬来计算，调用的是全国数据，而非前十城市数据
###或者可以再加一段不同城市不同职位的薪酬
rec = datas.groupby('positionType').size()#只考虑全职
rec.sort(ascending=False)
#rec.sort_values(inplace=True)
rec=list(rec.index[:10])
print(rec)


pt = datas[datas['positionType'].isin(rec)]
pt1 = pt.pivot_table(['salaryMin','salaryMax'],index='positionType')
pt1 = pt1.sort_values(by='salaryMin')
#pt1.plot(kind='bar')
#plt.title('热门职位领域薪资水平')
#plt.show()

###
pt_city = pt[pt['city'].isin(['北京','深圳','广州','上海','杭州'])]
pc1 = pt_city.pivot_table('salaryMin',index='positionType', columns='city')
pc1.plot(kind='bar')
plt.title('热门领域在五大城市薪酬水平')
plt.show()
'''
##实习
datas = datas[datas['jobNature']=='实习']#实习

sx1 = datas.groupby('positionType').size()##education
sx1.sort()
sx1.plot(kind='barh')
plt.show()
'''


