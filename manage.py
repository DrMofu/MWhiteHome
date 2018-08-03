# -*- coding: UTF-8 -*-
# 执行各类数据库创建、数据操作等任务

from flask_script import Manager
from index import app
import sqlite3

manager = Manager(app)

@manager.command
def initDB():
	conn = sqlite3.connect('myInfo.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE MY_VIDEO
	       (AID INT PRIMARY KEY     NOT NULL,
	       TITLE          TEXT     NOT NULL,
	       DESCRIPTION    TEXT     NOT NULL,
	       PIC			  TEXT     NOT NULL,
	       COMMENT		  INT      NOT NULL,
	       FAVORITES 	  INT  	   NOT NULL,
	       LENGTH 		  CHAR(10) NOT NULL,
	       PLAY 		  INT      NOT NULL);''')
	c.execute('''CREATE TABLE INFO
	       (NAME    TEXT    PRIMARY KEY    NOT NULL,
	       VALUE    TEXT);''')
	conn.commit()
	conn.close()
	print("Finished!")


if __name__ == '__main__':
	manager.run()