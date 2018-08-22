from PIL import Image
import numpy as np

img = Image.open("photo_01.jpg")
width, height = img.size
filter_size = 5
img2 = Image.new("RGB", (width-filter_size, height-filter_size))

img_pixels = np.array([[img.getpixel((x,y)) for x in range(width)] for y in range(height)])


for y in range(height - filter_size):
    for x in range(width - filter_size):
        partial_img = img_pixels[y:y + filter_size, x:x + filter_size]
        #color_array = partial_img.reshape(400, 3)
        color_array = partial_img.reshape(25, 3)
        if y == 1 and x == 1:
            print(partial_img)
            print("test")
            print(color_array)
        mean_r, mean_g, mean_b = color_array.mean(axis = 0)
        img2.putpixel((x,y),(int(mean_r),int(mean_g),int(mean_b)))
img2.show()
#img2.save("bokashi.jpg")
