#coding:utf-8
import PIL.Image as im
import numpy
import os,os.path

def convert_to500(filename):
    img=im.open(filename)
    out=img.resize((500,500))
    out.save(filename)



dir="/Users/zhangxu/Downloads/scene训练集"
for (dirpath, dirnames, filenames) in os.walk(dir):
    print dirpath
    for i in filenames:
        if i==".DS_Store":
            pass
        else:
            i=dirpath+'/'+i
            convert_to500(i)




