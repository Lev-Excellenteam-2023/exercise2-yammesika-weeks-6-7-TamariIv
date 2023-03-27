# DOESN'T WORK
# Function rgb_im.getpixel() on line 15 always returns (255, 255, 255) and doesn't recognize the black pixels

from PIL import Image


def get_message(path):
    image = Image.open(path)
    rgb_im = image.convert('RGB')

    width, height = image.size
    msg = ''
    for x in range(width):
        for y in range(height):
            r, g, b = rgb_im.getpixel((x, y))
            if r == 0 and g == 0 and b == 0:
                msg += chr(y)
    return msg


if __name__ == '__main__':
    print(get_message(f'C:/Users/tamar/excellenteam/python_ex2/code.png'))


