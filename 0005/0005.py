#!/usr/bin/env python
#coding=utf-8

import os
from PIL import Image

iphone5_WIDTH=1136
iphone5_HEIGHT=640

def resize_iphone5_pic(path,new_path,width=iphone5_WIDTH,height=iphone5_HEIGHT):
	im = Image.open(path)
	w,h=im.size

	if w>width:
		h=width*h//w
		w=width
	if h>height:
		w=height*w//h
		h=height


