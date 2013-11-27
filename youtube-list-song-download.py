import os
import urllib
import json as m_json

def filehandeling(list2=[]):
	fob=open('/list.txt','r')
	listOfSong = fob.readlines()
	for song in listOfSong:
		song = song[:-1]+' full song \n'
		list2.append(song)
	fob.close()
	return list2

keywords = filehandeling()

for query in keywords:
	query = urllib.urlencode ( { 'q' : query } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
	json = m_json.loads ( response )
	results1 = json ['responseData'] ['results']
	wanted= results1[0]['url']
	letssee=urllib.unquote(wanted).decode('utf8')
	
	if os.name=='posix':
		os.system("youtube-dl "+letssee+" --extract-audio --audio-format mp3")
