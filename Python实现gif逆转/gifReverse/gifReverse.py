from PIL import Image,ImageSequence
#将gif放在程序同目录下
im = Image.open(r'1.gif')
sequence = []

for f in ImageSequence.Iterator(im):
    sequence.append(f.copy())

sequence.reverse()
#1r是要生成的倒放的gif
sequence[0].save(r'1r.gif',save_all=True,append_images=sequence[1:])
