from PIL import Image, ImageDraw
import numpy as np
from numpy.random import randint


def k_mean(original_img, k):
    #STEP1
    w, h = original_img.size

    #2jigen
    img_pixels = np.array([[img.getpixel((x, y)) for x in range(w)] for y in range(h)])
    #genshoku
    reduce_img_pixels = np.array([[(0, 0, 0) for x in range(w)] for y in range(h)])

    #daihyo
    class_values = []
    for i in range(k):
        class_values.append(np.array([randint(256), randint(256), randint(256)]))

    #STEP2
    #20
    for i in range(20):
        #STEP2-1
        print("running at iteration No." + str(i))
        sums = []
        for c in range(k):
            sums.append(np.array([0, 0, 0]))
        sums_count = [0] * k

        #STEP2-2
        #class
        for x in range(w):
            for y in range(h):
                min_d = (256 ** 2) * 3
                class_index = 0
                #near class
                for j in range(k):
                    d = sum([x * x for x in img_pixels[y][x] - class_values[j]])
                    if min_d > d:
                        min_d = d
                        class_index = j
                sums[class_index] += img_pixels[y][x]
                sums_count[class_index] += 1
                #reduce_img_pixels[y][x] = tuple(list(map(int, class_values[class_index])))
                reduce_img_pixels[y][x] = class_values[class_index]

        #STEP2-3
        #daihyo
        for m in range(k):
            class_values[m] = sums[m] / sums_count[m]

    #STEP3
    #henkan
    reduce_img = Image.new("RGB", (w, h))
    for x in range(w):
        for y in range(h):
            reduce_img.putpixel((x, y), tuple(reduce_img_pixels[y][x]))
    return reduce_img


filename = "photo_01.jpg"
img = Image.open("./" + filename).convert("RGB")
reduce_img = k_mean(img, 5)
reduce_img.save("./reduce_" + filename)
