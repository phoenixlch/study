#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

Bak_dir = [r'D:\python\day1',r'D:\python\day2']
Bak_Tag= r"E:\BAK"
Today = Bak_Tag  +  time.strftime('\%Y%m%d')
if not os.path.exists(Today):
    MK = "mkdir %s" %Today
    if os.system(MK)==0:
        print MK

Copy_command = "copy %s %s " %(Bak_dir[0],Today)
if os.system(Copy_command) == 0:
    print "Successful"
else:
    print "Fail"

