from PIL import Image
import numpy as np

img = Image.open("photo_01.jpg")
width, height = img.size
filter_size = 2
img2 = Image.new('RGB', (width, height))
img_pixels = np.array([[img.getpixel((x, y)) for x in range(width)] for y in range(height)])

#print(img_pixels)
reverse_color_pixels = 255 - img_pixels
print(reverse_color_pixels)
for y in range(height):
    for x in range(width):
        r, g, b = reverse_color_pixels[y][x]
        img2.putpixel((x, y),(r, g, b))


img2.show()
