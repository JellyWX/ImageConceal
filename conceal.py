from pygame import image, PixelArray
import sys

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

img = sys.argv[1]

string = input('Please enter the string to be concealed > ')
mode = ''

while mode not in ['heavy', 'light']:
  mode = input('Please select a mode [light (easier to detect, takes less pixels)/heavy (harder to detect, takes 3x the pixels)] > ').lower()


char_list = [str(ord(c)) for c in string]

print(len(char_list))
char_list.insert(0, str(len(char_list)))

for char in range(len(char_list)): # convert all chars into 3-piece strings to be injected
  if len(char_list[char]) > 3:
    print('Please use only ASCII characters with values less than 215 and make sure your message is between 1 and 999 characters long')
    print(char_list[char])
    sys.exit()

  while len(char_list[char]) != 3:
    char_list[char] = '0' + char_list[char]


if mode == 'heavy':
  char_list = [c for char in char_list for c in char]
  char_list.insert(0,'2')

elif mode == 'light':
  char_list.insert(0,'1')


arr = PixelArray(image.load(img)) # load the specified image as an integer array

width = len(arr)
height = len(arr[0])

if width*height < len(char_list):
  print('The image is not large enough')
  sys.exit()

x = 0
y = 0
for char in char_list:
  letter_space = len(char)
  str_pix = str(arr[x][y])
  str_pix = str_pix[:-letter_space] + char

  if int(str_pix) > 16777215:
    new = list(str_pix)
    new[-letter_space-1] = '0'
    str_pix = ''.join(new)

  arr[x][y] = hex_to_rgb('#' + hex(int(str_pix))[2:])

  if y < height - 1:
    y += 1
  else:
    x += 1
    y = 0


s = arr.make_surface()

image.save(s, 'new.png')
