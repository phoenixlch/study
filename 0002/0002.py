#!/usr/bin/env python
#coding=utf8

#第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import uuid
import MySQLdb

def create_code(num,length):
	result = []
	while True:
		uuid_id=uuid.uuid1()
		temp=str(uuid_id).replace('-','')[:length]
		if temp not in result:
			result.append(temp)
		if len(result)==num:
			break
	return result



def save_to_mysql(num_list):
	conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
	cur=conn.cursor()

	sql_create_database = 'create database if not exists activecode_db'
	cur.execute(sql_create_database)

	conn.select_db("activecode_db")
	sql_create_table= 'create table if not exists active_codes(active_code char(32))'
	cur.execute(sql_create_table)

	cur.executemany('insert into active_codes value(%s)',num_list)

	conn.commit()
	cur.close()
	conn.close()

code_num = create_code(20,20)

save_to_mysql(code_num)