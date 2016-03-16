#!/usr/bin/env python
#coding=utf-8

"""
第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re

def count_the_words(path):
	with open(path) as f:
		text = f.read()
		word_list = re.findall(r'[a-zA-Z0-9]+',text)
		count = len(word_list)
	return count

if __name__ == '__main__':
	nums = count_the_words('key.txt')
	num2 = count_the_words('AP.xlsx')
	num3 = count_the_words('file.txt')
	print nums
	print num2
	print num3