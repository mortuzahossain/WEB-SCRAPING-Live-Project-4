# _*_ coding: utf-8 _*_

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS('phantomjs.exe')

def DownloadPageHtml(url):
	print 'Downloading : ' + url
	driver.get(url)
	html = driver.page_source
	return html


base_url = 'http://banglaoldsongs.fusionbd.com/downloads/mp3_index.php?dir=Bangla_Songs/'
big_latter = map(chr,range(ord('A'),ord('Z') + 1))

i = 0

for later in big_latter:

	html = DownloadPageHtml(base_url + later)
	soup = BeautifulSoup(html,'lxml')
	all_link = soup.find_all('div',class_ = 'odd')

	add_link = 'http://banglaoldsongs.fusionbd.com/downloads/'

	for link in all_link:
		html = DownloadPageHtml(add_link + link.find('a')['href'])
		soup = BeautifulSoup(html,'lxml')

		all_link = soup.find_all('div',class_ = 'odd')

		download_link = "http://banglaoldsongs.fusionbd.com/downloads/download.php?"

		i = i + 1
		filename = 'Output/' + str(i) + '.sql'


		f = open(filename,'w')

		for link in all_link:
			detailslink = link.find('a')['href']

			if len(link.text.rsplit('.mp3',1)) == 2:
				name = link.text.rsplit('.mp3',1)[0].replace("'","\'")
				size = link.text.rsplit('.mp3',1)[1].replace('Download - [','').replace(']','').replace("'","\'")
				url = download_link + 'file=' + detailslink.rsplit('file=',1)[-1].replace('&sort=0','').replace("'","\'")
				sql = "INSERT INTO songs (title,size,url) VALUES ('{}','{}','{}');\n".format(name,size,url)
				print sql
				f.write(sql)

		f.close()
