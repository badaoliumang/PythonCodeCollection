from wordcloud import WordCloud
import numpy as np
from PIL import Image
import jieba
mask=np.array(Image.open("ChinaMap.png"))
wcd=WordCloud(background_color=None,repeat=True,max_words=500,height=480,width=854,
             max_font_size=100,font_path="fonts/msyh.ttc",colormap="Reds",mask=mask,
             mode="RGBA")

text="核心价值观是一个国家的重要稳定器。一个民族、一个国家的核心价值观必须同自身的历史文化相契合，\
    同自身正在进行的奋斗相结合，同自身需要解决的时代问题相适应。可以说，社会主义核心价值观培育和践行的过程，\
    也是转型社会重建现代价值秩序的过程。在社会从传统向现代的转型过程中，人们的价值观念也发生了深刻的变化，\
    呈现出多元、多样、多变的特点。经济全球化、社会信息化的迅速发展更是强化了多元文化与价值观在同一时空中的激荡与碰撞。\
    面对多样化和多变性的价值观念，迫切需要培育和践行社会主义核心价值观，确立反映全国各族人民共同认同的价值观“最大公约数”，\
    为人们判断是非得失、做出价值选择提供价值准则，这是社会系统得以正常运转、社会秩序得以有效维护的重要途径。"

ss=" ".join(jieba.lcut(text))
wcd.generate(ss)
wcd.to_image()
wcd.to_file("China_wordcloud.png")
