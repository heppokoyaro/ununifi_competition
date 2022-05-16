from PIL import Image, ImageMath

src = Image.open('src/blue-black.png')
h, s, v = src.convert('HSV').split()

for i in range(256):
  _h = ImageMath.eval('(h + i) % 256', h=h, i=i).convert('L')
  dst = Image.merge('HSV', (_h, s, v)).convert('RGB')
  dst.save('dst/' + str(i) + '.png')