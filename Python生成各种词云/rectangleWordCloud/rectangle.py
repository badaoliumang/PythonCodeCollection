import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt
# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text
text = open(path.join(d,'aobama.txt')).read()
# 生成词云
wc = WordCloud(scale=2,max_font_size = 100)
wc.generate_from_text(text)
# 显示图像
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.tight_layout()
#存储图像
wc.to_file('aobama.png')
# or
# plt.savefig('1900_basic.png',dpi=200)
plt.show()
