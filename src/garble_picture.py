import click
import os

import numpy
from PIL import Image
import random


@click.command()
@click.argument('--input_path', default='.', help='输入的文件夹文件地址')
@click.argument('--filters', defualt='jpg.png', help('过滤器类型,若有多个,采用,隔开'))
@click.option('--output_path', default='.', help='输出的文件夹地址')
def manage(input_path, filters, output_path):
    """"""
    _filters = filters.split(',')

    for root, file, file_path in iter_file_path(input_path, _filters):
        new_output_path = output_path + root.split(input_path)[-1]

        if not os.path.exists(new_output_path):
            os.mkdir(new_output_path)

        img = garble_picture(file_path)

        img.save(os.path.join(new_output_path, file))


def iter_file_path(path, filters):
    """迭代生成相匹配的文件路径"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split('.')[-1] in filters:
                yield root, file, os.path.join(root, file)


def garble_picture(file_path):
    """混淆图片文件"""
    img = numpy.array(Image.open(file_path))
    img_length = len(img)
    img_high = len(img[0])
    for i in range(20):
        length = random.randint(0, img_length-1)
        high = random.randint(0, img_high-1)
        img[length][high] += 1

    return Image.fromarray(img.astype(numpy.uint8))


if __name__ == '__main__':
    manage()
