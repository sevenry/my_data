import pandas as pd 
import matplotlib.pyplot as plt 

datas = pd.read_csv('lagou.csv')
datas = datas.drop('companyLogo',axis = 1)#删除无关项
datas = datas.replace(['1-3','3-5'],['1-3年','3-5年'])##处理时间数据
datas = datas[datas['jobNature']=='实习']#排除兼职和实习影响

'''
city = datas.groupby('city').size()
city.sort(ascending = False)
#city.ix[:10].plot(kind = 'bar')
city.plot(kind='bar')
plt.title('全国实习招聘情况按城市排名')
plt.show()

city_ratio = city/len(datas)
print(city_ratio.ix[0])
city5 = city_ratio.ix[:5].sum()
city10 = city_ratio.ix[:10].sum()
print(city5, city10)

work_year = datas.groupby('workYear').size()##7项
work_year.sort(ascending = False)
work_year.plot(kind='bar')
plt.title('全国招聘情况按工作经验排名')
plt.show()

work_year_ratio = work_year/len(datas)
work_year_ratio.to_csv('work_year_ratio.csv')
print(work_year_ratio)


education = datas.groupby('education').size()
education.sort(ascending = False)
education.plot(kind='bar')##如果是横的柱状图，则排序为True
plt.title('全国招聘情况按学历要求排名')
plt.show()

education_ratio = education/len(datas)
education_ratio.to_csv('education_ratio.csv')
print(education_ratio)


companySize = datas.groupby('companySize').size()
companySize.sort()
companySize.plot(kind = 'barh')
plt.show()

companySize_ratio = companySize/len(datas)
companySize_ratio.to_csv('companySize_ratio.csv')

for choice in ['companySize', 'financeStage','jobNature','positionType']:
	kk = datas.groupby(choice).size()
	kk.sort()
	print(kk)
	kk.plot(kind = 'barh')
	plt.show()
'''
for choice in ['positionType']:
	kk = datas.groupby(choice).size()
	kk.sort(ascending = False)
	#print(kk)
	k1 = kk/len(datas)
	print(k1)
	for i in range(5):
		print(k1.ix[:5*i].sum())
	kk.plot(kind = 'bar')
	plt.title('全国实习招聘情况按职位领域排名')
	plt.show()



