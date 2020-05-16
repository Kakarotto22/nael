from pyrogram import *
from time import sleep
app = Client("short_link")


def edited_message(client, message):
	print(message)

def leech(client, message):
	print(message)
	file_name = message.document.file_name
	msg_id = message.message_id
	if file_name == "sites.txt":
		file = message.download(file_name="links.txt")
		f = open("downloads/links.txt","r")
		f = f.read()
		f = f.split("\n")
		links_number = len(f)
		for line in f:
			link = message.reply_text(line, quote=False)
			msg_id = link.message_id
			message.reply_text("/leech",reply_to_message_id=msg_id)
			sleep(60)



#
leech_handler = MessageHandler(
	leech,
	filters=Filters.document
)
app.add_handler(leech_handler)
#
edited_message_handler = MessageHandler(
	edited_message,
	filters=Filters.edited & Filters.text
)
app.add_handler(edited_message_handler)
#
#
app.run()  # Automatically start() and idle()
