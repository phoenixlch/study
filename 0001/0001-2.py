#!/usr/bin/env python
# coding=utf-8

import uuid

def create_code(num, length):         # 生成num个激活码，含有“length”位
    result = []
    while True:
    	uuid_id = uuid.uuid1()
    	temp = str(uuid_id).replace('-','')[:length]
    	if not temp in result:        #源代码错误处
    		result.append(temp)
		if len(result) == num:
			break
	print result
print '--------------------------------------------------------------------------------------'
print create_code(5,20)