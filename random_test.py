#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import random

#设定只有5个人可以中
n_tickets = 5
#设定参与抽奖的人，可以一直扩充
pname = ("小洁","宁宁","拉拉","小派","1 ","2 ","3","4","5","6","7","8","9","10","11","13","12")

#随机抽奖，想了解可以看看 http://apps.hi.baidu.com/share/detail/24178346
slice = random.sample(pname, n_tickets)

type = sys.getfilesystemencoding()


#后面就是打印出来而已
print "恭喜以下同学获得奖品：".decode('UTF-8').encode(type)
print
for x in range(n_tickets-1):
    print slice[x],
    if not (x+1) % 5:
        print        
print
print

os.system("pause")

