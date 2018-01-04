from pygame import image, PixelArray
import sys

img = sys.argv[1]

arr = PixelArray(image.load(img))
mode = int(str(arr[0][0])[-1])


if mode == 1: #light
  length = int(str(arr[0][1])[-3:])

  print('Length:', length)

  height = len(arr[0])

  word = ''
  x = 0
  y = 2
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

if mode == 2: #heavy
  pass
