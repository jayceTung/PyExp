# coding:utf-8
s = u"中文"
import MySQLdb
con = MySQLdb.connect(host='localhost', user='root', passwd='123456', db='test', charset='utf8')
cursor = con.cursor()


cursor.close()
con.close()
