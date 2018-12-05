from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
# 获取目录，path.dirname(__file__)：获取当前文件的path
# os.getcwd()方法用于返回当前工作目录。
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# 读取文件aobama.txt
text = open(path.join(d, 'aobama.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
#读取照片
alice_mask = np.array(Image.open(path.join(d, "bg.jpg")))
#设置需要屏蔽的词，如果为空，则使用内置的STOPWORDS
stopwords = set(STOPWORDS)
stopwords.add("said")
#生成词云，里面是具体参数
#max_words=2000 要显示的词的最大个数
#background_color="white" 背景颜色
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

# generate word cloud
#生成词云
wc.generate(text)

# store to file
# 存为照片文件
wc.to_file(path.join(d, "alice.png"))

# show
#显示照片文件
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
