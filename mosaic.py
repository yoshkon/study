from PIL import Image
import numpy as np

img = Image.open("photo_01.jpg")
width, height = img.size
filter_size = 2
img2 = Image.new('RGB', (width, height))
img_pixels = np.array([[img.getpixel((x, y)) for x in range(width)] for y in range(height)])


def draw_partial_img(imgx, start_x, start_y, partial_size_x, partial_size_y, pixel_color):
    for y in range(start_y, start_y + partial_size_y):
        for x in range(start_x, start_x + partial_size_x):
            imgx.putpixel((x, y), pixel_color)


for y in range(0, height, filter_size):
    for x in range(0, width, filter_size):
        partial_img = img_pixels[y:y + filter_size, x:x + filter_size]
        color_array = partial_img.reshape(partial_img.shape[0] * partial_img.shape[1], 3)
        #color_array = partial_img.reshape(400, 3)
        max_index = np.argmax(color_array.sum(axis=1))
        max_r, max_g, max_b = color_array[max_index]
        draw_partial_img(img2, x, y, partial_img.shape[1], partial_img.shape[0], (max_r, max_g, max_b))

img2.show()
