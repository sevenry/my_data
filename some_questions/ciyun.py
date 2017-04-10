import jieba
import wordcloud
import PIL

from wordcloud import WordCloud

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

china_text=open("yhx.txt").read()
ttt=jieba.cut(china_text)
a=" ".join(ttt)

stopwords = {"的","了","之"}
alice_coloring = np.array(Image.open( "alice.png"))
##注意这里需要下载字体
wc = WordCloud(font_path='zitiaaa.ttf',background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40)
# generate word cloud
wc.generate(a)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
#plt.axis("off")
plt.figure(figsize=(3000,1000))
plt.show()

