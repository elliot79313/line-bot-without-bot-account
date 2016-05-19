#-*- coding: UTF-8 -*-
# https://github.com/carpedm20/LINE

from line import LineClient, LineGroup, LineContact

f = open("credentials")
ID = f.readline().strip()
PASSWD = f.readline().strip()
f.close()

client = LineClient(ID, PASSWD, com_name="line_api_demo")
friends = client.contacts


for i, friend in enumerate(friends):
	print i, friend

#for i, group in enumerate(groups):
#	print i, group

friend = client.contacts[429]
friend.sendMessage("hello world! 本訊息由機器人寄送 XD")
