"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:
    :return:
    """
    # 新建與原圖長寬相同之空白圖
    new_img = SimpleImage.blank(img.width, img.height)
    # 依序填入相對應的像素至空白圖中
    for x in range(img.width):
        for y in range(img.height):
            # 設定使用變數: n為計算平均像素的總數、r g b 分別為紅綠藍三色的像素總和
            n = 0
            r = 0
            g = 0
            b = 0
            # 尋找鄰近的像素
            for x1 in range(x-1, x+2):
                for y1 in range(y-1, y+2):
                    # 判定是否為邊界
                    if x1 >= 0 and y1 >= 0:
                        if x1 <= img.width-1 and y1 <= img.height-1:
                            r = r + img.get_pixel(x1, y1).red
                            g = g + img.get_pixel(x1, y1).green
                            b = b + img.get_pixel(x1, y1).blue
                            n = n + 1
            # 計算填入空白圖的像素
            new_img.get_pixel(x, y).red = r / n
            new_img.get_pixel(x, y).green = g / n
            new_img.get_pixel(x, y).blue = b / n
    return new_img


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(10):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
