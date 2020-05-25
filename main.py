from pyrogram import *
from time import sleep
from db import *

app = Client("forward")

sudoers = [183924118,1060779034]

def forward(client,message):
	caption = message.caption
	vid = message.video.file_id
	file_ref = message.video.file_ref
	desc , e_n = gde(caption)
	add_video(e_n,desc,vid,file_ref)


def main(client,message):
	try:
		text = message.text
	except:
		pass
	chat_id = message.chat.id
	user_id = message.from_user.id
	data = get_data()
	if text and text =="تحميل" and user_id in sudoers:
		message.reply_text("ارسل الان الرابط")
		get_data("URL")
	elif text and data == "URL" and user_id in sudoers:
		get_url(text)
		message.reply_text("ارسل الان عدد الحلقات")
		get_data("e_n")
	elif text and data == "e_n" and user_id in sudoers:
		get_data("None")
		link = get_url()
		e_n = text
		i  = 1
		qualty = get_qualty()
		while i < int(e_n)+1:
			main_delay = get_main_delay()
			url = get_link("{}{}".format(link,i),qualty)
			msg = app.send_message(chat_id,"{}".format(url))
			msg.reply_text("/leech")
			i += 1
			if i+3 < int(e_n)+1:
				sub_delay = get_sub_delay()
				sleep(int(sub_delay))
				url = get_link("{}{}".format(link,i),qualty)
				msg = app.send_message(chat_id,"{}".format(url))
				msg.reply_text("/leech")
				i += 1
				sleep(int(sub_delay))
				url = get_link("{}{}".format(link,i),qualty)
				msg = app.send_message(chat_id,"{}".format(url))
				msg.reply_text("/leech")
				i += 1
				sleep(int(sub_delay))
				url = get_link("{}{}".format(link,i),qualty)
				msg = app.send_message(chat_id,"{}".format(url))
				msg.reply_text("/leech")
				i += 1
			sleep(int(main_delay))
		app.send_message(chat_id,"Download Finished")
	elif text == "ارسال" and user_id in sudoers:
		videos = video_list()
		videos = sorted(videos)
		for video in videos:
			vid = get_vid(video)
			desc = get_desc(video)
			file_ref = get_fref(video)
			app.send_video(chat_id=int(get_channel_id()),video=vid,file_ref=file_ref,caption=desc+"\nمُشاهدة بجودة متوسّطة 👆👆")
			sleep(3)
		message.reply("All videos was send")
		reset_data()
	elif text == "review":
		videos = video_list()
		print(videos)
		videos = sorted(videos)
		msg = "You have {} videos to send:".format(len(videos))
		for video in videos:
			desc = get_desc(video)
			msg += "\n{} {}".format(video,desc)
		message.reply(msg)
	elif text == "/qualty":
		qualty = get_qualty()
		message.reply("qualty is : {}\nYou can Change it just send /setqualty".format(qualty))
	elif text == "/channel":
		channel_id = get_channel_id()
		message.reply("Main delay is : {}\nYou can Change it just send /setchannel".format(channel_id))
	elif text == "/maindelay":
		main_delay = get_main_delay()
		message.reply("Main delay is : {}\nYou can Change it just send /setmaindelay".format(main_delay))
	elif text == "/subdelay":
		sub_delay = get_sub_delay()
		message.reply("Sub delay is : {}\nYou can Change it just send /setsubdelay".format(sub_delay))
	elif text == "/setqualty":
		message.reply("Please Send New qualty\nLike This : \n360")
		get_data("change_qualty")
	elif text == "/setchannel":
		message.reply("Please Send New Channel id\nLike This : \n-10082838028")
		get_data("change_channel")
	elif text == "/setmaindelay":
		message.reply("Please Send New Main Delay\nLike This : \n5 Delay for 5 Second")
		get_data("change_main_delay")
	elif text == "/setsubdelay":
		message.reply("Please Send New Sub Delay\nLike This : \n5 Delay for 5 Second")
		get_data("change_sub_delay")
	elif text and data == "change_qualty" and user_id in sudoers:
		get_data("None")
		get_qualty(text)
		message.reply("Qualty Was changed")
	elif text and data == "change_channel" and user_id in sudoers:
		get_data("None")
		get_channel_id(text)
		message.reply("Channel Was changed")
	elif text and data == "change_main_delay" and user_id in sudoers:
		get_data("None")
		get_main_delay(text)
		message.reply("Main delay Was changed")
	elif text and data == "change_sub_delay" and user_id in sudoers:
		get_data("None")
		get_sub_delay(text)
		message.reply("Sub delay Was changed")


#
main_handler = MessageHandler(
	main,
	filters=Filters.document | Filters.text
)
app.add_handler(main_handler)
#
forward_handler = MessageHandler(
	forward,
	filters=Filters.video
)
app.add_handler(forward_handler)
#





app.run()  # Automatically start() and idle()