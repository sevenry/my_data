#根据给定的文件夹，依次读取每个文件，提取其中一部分，存到另一个文件夹中，以同名存储。

import os
import json


dirs = os.listdir('./maildata2/')
file_names = []
for name in dirs:
    file_names.append(name)
	
for name in file_names:
    fp = open('./maildata2/'+name, "r",encoding='UTF-8')
    www = json.load(fp)
    abc = www['data']
    txt1 = abc[0]['pure']
    ff = open('./maildata_pre/'+name[:31]+'txt','a+',encoding='UTF-8')
    ff.write(txt1)
    ff.close()