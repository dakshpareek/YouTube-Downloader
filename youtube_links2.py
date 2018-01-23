#pip install requests,bs4,pytube
import requests
from bs4 import BeautifulSoup
from pytube import YouTube


def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

ch=input("1. Link 2. Playlist :-->  ")
#ch2=input("1. Video 2. Audio :-->> ")
#tipe=False if ch2=="1" else True
tipe=False
if ch==2:
	url1=raw_input("Enter Playlist Link: ")
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
		print "Title :",yt.title
		stream=yt.streams.filter(only_audio=tipe).all()
		print "Downloading.."
		stream[0].download()
		print "--Download Complete--"
	print "*** Task Completed ***"

elif ch==1:
	url1=raw_input("Enter YouTube Link: ")
	yt=YouTube(url1)
	print "Title : ",yt.title
	stream=yt.streams.filter(only_audio=tipe).all()
	#stream[0].download()
	si=stream[0].filesize
	#print stream
	si=sizeof_fmt(si) 
	print "File Size: ",si
	ch=raw_input("Download??  y / n ")
	if ch=='y' or ch=='Y':
		print " Downloading.. "
		stream[0].download()
		print "--- Download Complete ---"
	else:
		print "Exit"






