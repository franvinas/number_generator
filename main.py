from PIL import Image
import argparse


parser = argparse.ArgumentParser(description='Generate an image.')
parser.add_argument('n', metavar='N', type=int, nargs='?', default=None, help='an integer for the accumulator')
parser.add_argument('--range', dest='range', nargs=2, help='sum the integers (default: find the max)')
parser.add_argument('--show', dest='show', action='store_const', const=True, default=False, help='sum the integers (default: find the max)')
parser.add_argument('--position', dest='position', type=float, help='sum the integers (default: find the max)')


space = 0


def generate_img(n: int, numbers_img: dict, background: Image, pos):
    digits = [int(d) for d in str(n)]
    icon = Image.open(f'static/white #.png').convert('RGBA')

    total_num_width = sum(numbers_img[d].width for d in digits) + space * (len(digits) - 1) + icon.width
    # total_num_height = max(numbers_img[d].height for d in digits)

    x_pos = int((background.width - total_num_width) / 2)
    y_pos = int(background.height * pos)
    img = Image.new(mode='RGBA', size=(background.width, background.height))
    img.paste(background, box=(0, 0))

    img.paste(icon, box=(x_pos, y_pos), mask=icon)
    x_pos += icon.width

    for d in digits:
        number_img = numbers_img[d]
        img.paste(number_img, box=(x_pos, y_pos), mask=number_img)
        x_pos += number_img.width + space
    return img


def __main__():
    args = parser.parse_args()
    generated_images_folder = 'generated'
    numbers_img = {i: Image.open(f'static/white {i}.png').convert('RGBA') for i in range(10)}
    background = Image.open('static/background.jpg').convert('RGBA')

    if args.position:
        pos = args.position
    else:
        pos = 0.5

    if args.n:
        img = generate_img(args.n, numbers_img, background, pos)
        if args.show:
            img.show()
        else:
            img.save(f'{generated_images_folder}/{args.n}.png')

    if args.range and not args.show:
        for n in range(int(args.range[0]), int(args.range[1])):
            img = generate_img(n, numbers_img, background, pos)
            img.save(f'{generated_images_folder}/{n}.png')


__main__()
