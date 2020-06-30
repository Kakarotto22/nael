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
		message.reply_text("ارسل الان رقم الحلقة التي سابدا منها")
		get_data("e_n1")
	elif text and data == "e_n1" and user_id in sudoers:
		get_en(text)
		message.reply_text("ارسل الان رقم الحلقة التي ساتوقف عندها")
		get_data("e_n2")
	elif text and data == "e_n2" and user_id in sudoers:
		get_data("None")
		link = get_url()
		e_n = text
		i  = int(get_en())
		qualty = get_qualty()
		while i < int(e_n)+1:
			main_delay = get_main_delay()
			url = get_link(f"{link}{i}",qualty)
			if url != None:
				msg = app.send_message(chat_id,f"{url}")
				msg.reply_text("/leech")
			i += 1
			if i+3 < int(e_n)+1:
				sub_delay = get_sub_delay()
				sleep(int(sub_delay))
				url = get_link(f"{link}{i}",qualty)
				if url != None:
					msg = app.send_message(chat_id,f"{url}")
					msg.reply_text("/leech")
				i += 1
				sleep(int(sub_delay))
				url = get_link(f"{link}{i}",qualty)
				if url != None:
					msg = app.send_message(chat_id,f"{url}")
					msg.reply_text("/leech")
				i += 1
				sleep(int(sub_delay))
				url = get_link(f"{link}{i}",qualty)
				if url != None:
					msg = app.send_message(chat_id,f"{url}")
					msg.reply_text("/leech")
				i += 1
			sleep(int(main_delay))
		app.send_message(chat_id,"Download Finished")
	elif text == "ارسال" and user_id in sudoers:
		videos = video_list()
		videos = sorted(videos)
		msg = message.reply("جارٍ الإرسال...")
		for video in videos:
			vid = get_vid(video)
			desc = get_desc(video)
			file_ref = get_fref(video)
			subdesc = get_subdesc()
			app.send_video(chat_id=int(get_channel_id()),video=vid,file_ref=file_ref,caption=desc+"\n"+subdesc)
			sleep(3)
		msg.edit_text("All videos was send")
		reset_data()
	elif text.lower() == "review":
		videos = video_list()
		print(videos)
		videos = sorted(videos)
		msg = f"You have {len(videos)} videos to send:"
		i = 1
		for video in videos:
			desc = get_desc(video)
			msg += f"\n{i} {desc}"
			i += 1
		if len(msg) < 4096:
			message.reply(msg)
		else:
			res_first, res_second = msg[:len(msg)//2],msg[len(msg)//2:]
			msg.reply(res_first)
			msg.reply(res_second)
	elif text == "/subdesc":
		desc = get_subdesc()
		message.reply(f"Sub Descrption is : `{desc}`\nYou can Change it just send /setsubdesc")
	elif text == "/qualty":
		qualty = get_qualty()
		message.reply(f"Qualty is : `{qualty}`\nYou can Change it just send /setqualty")
	elif text == "/channel":
		channel_id = get_channel_id()
		message.reply(f"Channel id is : `{channel_id}`\nYou can Change it just send /setchannel")
	elif text == "/maindelay":
		main_delay = get_main_delay()
		message.reply(f"Main delay is : `{main_delay}`\nYou can Change it just send /setmaindelay")
	elif text == "/subdelay":
		sub_delay = get_sub_delay()
		message.reply(f"Sub delay is : `{sub_delay}`\nYou can Change it just send /setsubdelay")
	elif text == "/setsubdesc":
		message.reply("Please Send New Sub Descreption")
		get_data("change_subdesc")
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
	elif text and data == "change_subdesc" and user_id in sudoers:
		get_data("None")
		get_subdesc(text)
		message.reply("Sub Descreption Was changed")
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
