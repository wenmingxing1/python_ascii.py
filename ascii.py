# -*- coding:utf-8 -*-

from PIL import Image       #调入pillow模块中的Image类
import argparse     #argparse为命令行解析工具

#命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file') #输入文件
parser.add_argument('-o-','--output')   #输出文件
parser.add_argument('--width',type = int,default = 70)  #输出字符画宽度
parser.add_argument('--height',type = int,default = 40) #输出字符画高度

#获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("*#@B%8&WM#$oahkbdpqwm.O0QLCJUYXzcvunxrjft/\|(o1{}[]?-_+~<>i!lI;:,\"^`'. ")    #可以不是70个字符

#将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ''
    #length = len(ascii_char)
    gray = int(0.2126*r + 0.7152*g + 0.0722*b)      #彩色rgb转化为灰度

    unit = (256.0 + 1)/len(ascii_char)   
    return ascii_char[int(gray/unit)]   #将相应的灰度值映射为ascii_char中的字符

if __name__ == '__main__':

    im = Image.open(IMG)    #im.open()读取图片
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)    #im.resize()将图像做尺寸变换;Image.NEAREST为图像缩放的参数，这里是最低质量

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))    #getpixel获取每个坐标像素点的rgb，参数格式为（x,y）
        txt += '\n'

    print(txt)

    #字符画输出到文件
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
