from pyrogram import *
from time import sleep
import dataset
app = Client("short_link")

sudoers = (183924118,1060779034)

db = dataset.connect('sqlite:///data.db')
table = db['data']

check = table.find_one(id=1)
if check == None:
	table.insert(dict(id=1,data=None,cl=0))


def leech(client, message):
	f = open("downloads/links.txt","r")
	f = f.read()
	f = f.split("\n")
	for line in f:
		link = message.reply_text(line, quote=False)
		msg_id = link.message_id
		message.reply_text("/leech",reply_to_message_id=msg_id)
		sleep(60)

def forward(client, message):
	caption = open("downloads/caption.txt","r")
	caption = caption.read()
	caption = caption.split("\n")
	caption_line = table.find_one(id=1)["cl"]
	print(caption_line)
	app.send_video(-1001413874309,message.video.file_id,caption=caption[caption_line]+"\nمُشاهدة بجودة متوسّطة 👆👆")
	table.update(dict(id=1, cl=caption_line+1), ["id"])


def main(client,message):
	try:
		text = message.text
	except:
		pass
	data = table.find_one(id=1)["data"]
	if text and text == "download" and message.from_user.id in sudoers:
		message.reply_text("Now Send URL files")
		table.update(dict(id=1, data="URL_file"), ["id"])
	elif message.document and data == "URL_file" and message.from_user.id in sudoers:
		message.download(file_name="links.txt")
		message.reply_text("Now Send Caption file")
		table.update(dict(id=1, data="caption_file"), ["id"])
	elif message.document and data == "caption_file" and message.from_user.id in sudoers:
		message.download(file_name="caption.txt")
		message.reply_text("Ok start Downloading")
		table.update(dict(id=1, data="None"), ["id"])
		leech(client,message)
	if message.text == "/reset" and message.from_user.id in sudoers:
		message.reply_text("Caption Line Was reset")
		table.update(dict(id=1, cl=0), ["id"])

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
print("Bot Is Running")
app.run()  # Automatically start() and idle()
