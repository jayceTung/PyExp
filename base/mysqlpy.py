#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

DATABASE_NAME = "test"


class MySQLHelper:

    def __init__(self, name=None, conn=None, cur=None):
        self.name = name
        self.conn = conn
        self.cur = cur

    # create a table
    def create_table(self, name, sql):
        try:
            ex = self.cur.execute
            ex('DROP TABLE IF EXISTS game')
            if ex('show tables') == 0:
                ex('create table ' + name + sql)
                self.conn.commit()
        except MySQLdb.Error, e:
            print "Mysql Error %d %s" % (e.args[0], e.args[1])

    # insert single record
    def insert(self, name, value):
        try:
            self.cur.execute('insert into ' + name + ' values(%s, %s, %s, %s, %s)', value)
        except MySQLdb.Error, e:
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    def __del__(self):
        if self.cur:
            self.cur.close()
        if self.conn:
            self.conn.close()


