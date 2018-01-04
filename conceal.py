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

if len(str(len(char_list))) > 9:
  print('String too long. The max size is 999999999')
  sys.exit()

largest_char = max([len(char) for char in char_list])

for char in range(len(char_list)): # convert all chars into 3-piece strings to be injected
  while len(char_list[char]) != largest_char:
    char_list[char] = '0' + char_list[char]

char_list.insert(0, str(len(char_list)))
char_list.insert(0, str(len(str(len(char_list))))) # adds the number of digits, so the revealer can know how much we're looking at
char_list.insert(0, str(largest_char))

print('Digits:', len(str(len(char_list))))

char_list = [c for char in char_list for c in char]

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
  str_pix = str_pix[:-1] + char

  if int(str_pix) > 16777215:
    new = list(str_pix)
    new[-2] = '0'
    str_pix = ''.join(new)

  arr[x][y] = hex_to_rgb('#' + hex(int(str_pix))[2:]) # this messy conversion is used because pygame doesnt work well with integers or hex numbers

  if y < height - 1:
    y += 1
  else:
    x += 1
    y = 0


s = arr.make_surface()

image.save(s, 'new.png')
