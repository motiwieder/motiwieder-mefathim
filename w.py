from urllib.request import urlopen
from bs4 import BeautifulSoup
from random import choice

def get_imgs_links(link):
	with urlopen(link) as resp:
		soupobj = BeautifulSoup(resp.read())
	img_tags = [f"https:{tag['src']}" for tag in soupobj.find_all('img')]
	img_srcs = [f"https://en.wikipedia.org{tag.get('href')}"
	for tag in soupobj.find_all('a')
		if (tag.get('href')!=None) and (tag.get('href')[:5]=="/wiki")]
							
	return img_tags, img_srcs 

def img_download(src):
#	print(i)		
	with urlopen(src) as rwiki:
		raw_data = rwiki.read()					
	with open(src.split('/')[-1],'wb') as h_file:
#	:	print(f'moti {i}')		
		h_file.write(raw_data)

#a,b = get_imgs_links('https://en.wikipedia.org/wiki/usa') 
#print(a,b)
#img_download(b[:5])

def crawl(link):
	im, link = get_imgs_links(link)
	for img in im:
		print('download:{im}')
		try:
			img_download(img)
		except Exception as e:
			print('error')	
	next_link = choice(link)
	print('moving to link: {next_link}')
	crawl(next_link)
crawl('https://en.wikipedia.org/wiki/usa')

