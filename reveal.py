from pygame import image, PixelArray
import sys

img = sys.argv[1]

arr = PixelArray(image.load(img))
max_size = int(str(arr[0][0])[-1])
digits = int(str(arr[0][1])[-1])

print(digits)

length = ''
for i in range(2,digits+2):
  length += str(arr[0][i])[-1:]

length = int(length)
print('Length:', length)

height = len(arr[0])

word = ''
x = 0
y = digits+2
char_buffer = ''
for i in range(length*max_size+1):
  if len(char_buffer) == max_size:
    print('Decoding character:', char_buffer)
    word += chr(
      int(
        char_buffer
      ))
    char_buffer = ''

  char_buffer += str(arr[x][y])[-1:]

  if y < height - 1:
    y += 1
  else:
    x += 1
    y = 0

print(word)
