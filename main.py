#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
from base.mysqlpy import MySQLHelper


def main():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8')
    cur = conn.cursor()
    helper = MySQLHelper('test', conn, cur)
    # helper.create_table('game', '(id int auto_increment primary key, name varchar(20), sex int, age int, info varchar(50))')
    helper.insert('game', (1, '张三', 1, 19, '大幅度负能量看电视剧的拉克丝减肥开始两三分'))


if __name__ == '__main__':
    main()
