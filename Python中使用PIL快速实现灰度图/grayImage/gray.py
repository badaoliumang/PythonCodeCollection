from PIL import Image
img=Image.open('1111.jpg')
img=img.convert('L')
img.save('灰度图.jpg')
