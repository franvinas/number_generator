from PIL import Image
import argparse


parser = argparse.ArgumentParser(description='Generate an image.')
parser.add_argument('n', metavar='N', type=int, nargs='?', default=None, help='an integer for the accumulator')
parser.add_argument('--range', dest='range', nargs=2, help='sum the integers (default: find the max)')
parser.add_argument('--show', dest='show', action='store_const', const=True, default=False, help='sum the integers (default: find the max)')


def generate_img(n: int, numbers_img: dict, background: Image):
    digits = [int(d) for d in str(n)]
    width = sum(numbers_img[d].width for d in digits)
    height = max(numbers_img[d].height for d in digits)

    img = Image.new(mode='RGBA', size=(width, height))
    img.paste(background, box=(0, 0))
    pos = 0
    for d in digits:
        number_img = numbers_img[d]
        img.paste(number_img, box=(pos, 0), mask=number_img)
        pos += number_img.width
    return img


def __main__():
    args = parser.parse_args()
    generated_images_folder = 'generated'
    numbers_img = {i: Image.open(f'static/{i}.png').convert('RGBA') for i in range(10)}
    background = Image.open('static/background.jpg').convert('RGBA')

    if args.n:
        img = generate_img(args.n, numbers_img, background)
        if args.show:
            img.show()
        else:
            img.save(f'{generated_images_folder}/{args.n}.png')

    if args.range and not args.show:
        for n in range(int(args.range[0]), int(args.range[1])):
            img = generate_img(n, numbers_img, background)
            img.save(f'{generated_images_folder}/{n}.png')


__main__()
