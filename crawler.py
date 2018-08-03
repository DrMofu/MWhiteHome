import requests
import json
import sqlite3


def getMyInfo():
	# 1 关注者信息
	followerURL = 'https://api.bilibili.com/x/relation/stat?vmid=3769932'
	res = requests.get(followerURL) # 获取html文件信息
	res.encoding = 'utf-8'  # 很重要！
	ans = json.loads(res.text)
	follower = ans['data']['follower']

	# 2 视频信息
	videoInfo = []
	videoURL ='https://space.bilibili.com/ajax/member/getSubmitVideos?mid=3769932&page=1&pagesize=25'
	res = requests.get(videoURL) # 获取html文件信息
	res.encoding = 'utf-8'  # 很重要！
	ans = json.loads(res.text)

	for item in ans['data']['vlist']:
		Info = {'title':item['title'],\
				'description':item['description'],\
				'pic':item['pic'],\
				'comment':item['comment'],\
				'favorites':item['favorites'],\
				'length':item['length'],\
				'play':item['play'],\
				'aid':item['aid']
			   }
		videoInfo.append(Info)

	# 数据库导入
	conn = sqlite3.connect('myInfo.db')
	c = conn.cursor()
	cursor = c.execute("SELECT AID from MY_VIDEO")
	print(cursor)
	# resultList = cursor.flatten
	for item in videoInfo:
		if item['aid'] in cursor
			# 更新
			pass
		else
			# 插入
			pass
	return 0