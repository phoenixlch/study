#!/usr/bin/env python
# coding=utf-8

# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？

import uuid


# def create_code(num, length):  # 生成num个激活码，含有“length”位
#     result = []
#     while True:
#     	uuid_id = uuid.uuid1()
#     	temp = str(uuid_id).replace('-','')[:length]
#     	if not temp in result:        #源代码错误处
#     		result.append(temp)
# 		if len(result) == num:
# 			break
# 	return result

# print create_code(20,20)


import uuid
import MySQLdb

def create_code(num, length):
#生成”num“个激活码，每个激活码含有”length“位
    result = []
    while True:
        uuid_id = uuid.uuid1()
        temp = str(uuid_id).replace('-', '')[:length]
        if temp not in result:
            result.append(temp)
        if len(result) == num:
            break
    return result

print create_code(20,20)
