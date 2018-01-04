from pygame import image, PixelArray
import sys

img = sys.argv[1]

arr = PixelArray(image.load(img))

length = int(str(arr[0][0])[-3:])

print('Length:', length)

height = len(arr[0])

word = ''
x = 0
y = 1
for i in range(length):
  print('Decoding character:', str(arr[x][y])[-3:])
  word += chr(
    int(
      str(arr[x][y])[-3:]
    ))

  if y < height - 1:
    y += 1
  else:
    x += 1
    y = 0

print(word)
