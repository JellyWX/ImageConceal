from pygame import image, PixelArray
import sys

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

img = sys.argv[1]

string = input('Please enter the string to be concealed > ')

char_list = [str(ord(c)) for c in string]
print(str(len(char_list)))
char_list.insert(0, str(len(char_list)))

for char in range(len(char_list)): # convert all chars into 3-piece strings to be injected
  if len(char_list[char]) > 3:
    print('Please use only ASCII characters')
    sys.exit()

  while len(char_list[char]) != 3:
    char_list[char] = '0' + char_list[char]

arr = PixelArray(image.load(img)) # load the specified image as an integer array

width = len(arr)
height = len(arr[0])

if width*height < len(char_list):
  print('The image is not large enough')
  sys.exit()

x = 0
y = 0
for char in char_list:
  str_pix = str(arr[x][y])
  str_pix = str_pix[:-3] + char
  arr[x][y] = hex_to_rgb('#' + hex(int(str_pix))[2:])

  if y < height - 1:
    y += 1
  else:
    x += 1
    y = 0

s = arr.make_surface()

image.save(s, 'new.png')