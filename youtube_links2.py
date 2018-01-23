import requests
from bs4 import BeautifulSoup
from pytube import YouTube

ch=input("1. Link 2. Playlist")
if ch==2:
	url1=raw_input("Enter Playlist Link")
	#url1="https://www.youtube.com/playlist?list=PLFACC72B70062EB2D"

	r = requests.get(url1)

	r=r.text.encode("utf-8")

	soup = BeautifulSoup(r,'lxml')

	d1 = soup.findAll("td",{"class": "pl-video-title"})

	all_video_links_in_playlist=[]

	for demo in d1:
		#print demo.find("a").text.encode("utf-8")#,
		link="www.youtube.com"
		link=link+demo.find("a").attrs['href']
		all_video_links_in_playlist.append(link)

	#print all_video_links_in_playlist

	for every_video in all_video_links_in_playlist[20:]:
	#for every_video in all_video_links_in_playlist:
		yt=YouTube(every_video)
		print "Video Title :",yt.title
		stream=yt.streams.filter(file_extension='mp4').all()
		print "Downloading.."
		stream[0].download()
		print "Download Complete"
	print "Task Completed"
	
elif ch==1:
	url1=raw_input("Enter YouTube Link")
	yt=YouTube(url1)
	print "Video Title :",yt.title
	stream=yt.streams.filter(file_extension='mp4').all()
	print "Downloading.."
	stream[0].download()
	print "Download Complete"




