import dataset
import requests
from time import sleep

db = dataset.connect("sqlite:///data.db")
table = db['data']
download_table = db["download_data"]

data = download_table.find_one(id=1)
if data == None:
	table.insert(dict(id=1,url=None,channel_id=-1001413874309,main_delay=300,sub_delay=5,data=None,qualty=360))

def info(e_n):
	data = table.find_one(e_n=e_n)
	return data

def get_desc(e_n):
	data = table.find_one(e_n=e_n)
	return data["desc"]

def get_vid(e_n):
	data = table.find_one(e_n=e_n)
	return data["vid"]

def get_fref(e_n,text=""):
	data = table.find_one(e_n=e_n)
	return data["file_ref"]

def add_video(e_n,desc,vid,file_ref):
	table.insert(dict(e_n=e_n,desc=desc,vid=vid,file_ref=file_ref))

def video_list():
	data = table.all()
	videos = []
	for row in data:
		videos.append(row["e_n"])
	return videos


def gde(text):
	text = text.replace("[Blkom.com] ","")
	text = text.split(".mp4")[0]
	text = text.replace(".1","")
	desc = text.replace("Ep","0")
	e_n = text.replace(" [480p]","")
	e_n = e_n.replace(" [360p]","")
	e_n = e_n.replace(" [720p]","")
	e_n = e_n.split(Ep")
	e_n = e_n[1]
	return desc,e_n

def reset_data():
	table.delete()	
	
def get_data(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["data"]
	else:
		download_table.update(dict(id=1, data=text), ["id"])

def get_channel_id(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["channel_id"]
	else:
		download_table.update(dict(id=1, channel_id=text), ["id"])

def get_subdesc(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["sub_desc"]
	else:
		download_table.update(dict(id=1, sub_desc=text), ["id"])

def get_main_delay(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["main_delay"]
	else:
		download_table.update(dict(id=1, main_delay=text), ["id"])

def get_sub_delay(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["sub_delay"]
	else:
		download_table.update(dict(id=1, sub_delay=text), ["id"])

def get_url(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["url"]
	else:
		download_table.update(dict(id=1, url=text), ["id"])

def get_qualty(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["qualty"]
	else:
		download_table.update(dict(id=1, qualty=text), ["id"])

def get_en(text=""):
	if text == "":
		data = download_table.find_one(id=1)
		return data["e_n"]
	else:
		download_table.update(dict(id=1, e_n=text), ["id"])

def get_link(link,qualty):
	try:
		r = requests.get(link).text
		page = r.split("\n")
		line = r.split("\n")
		for element in line:
			if qualty == 360:
				if "360p <small>" in element or "360 <small>" in element:
					line = line.index(element)
			elif qualty == 480:
				if "480p <small>" in element or "480 <small>" in element:
					line = line.index(element)
			elif qualty == 720:
				if "720p <small>" in element or "720 <small>" in element:
					line = line.index(element)
		line = int(line)-1
		link = page[line]
		link = link.replace('<a href="','')
		link = link.replace('" class="btn btn-default" title="Fansub">','')
		return link
	except:
		pass
