import os
from os import path
from wordcloud import WordCloud
from matplotlib import pyplot as plt
# 获取当前文件路径
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
# 获取文本text
text = open(path.join(d,'aobama.txt')).read()
# 生成词云
#scale=2缩放2倍
#max_font_size = 100 最多显示词汇量100
#background_color='red' 背景颜色 红色
#colormap='Blues' 色图，可更改名称进而更改整体风格
wc = WordCloud(scale=2,max_font_size = 100,background_color='red',colormap='Blues')
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
