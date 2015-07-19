# -*- coding: utf-8 -*-
import scrapy
import cfscrape
from scrapy.spiders import Spider
import json

rez=[]

class LinkbaseSpider(Spider):

	name = "linkbase"
	allowed_domains = ["127.0.0.1"]
	start_urls = (
		'file://127.0.0.1/home/unkn0wn/web/linkbase/linkb/link.html',
	) 
	# scraper = cfscrape.create_scraper() # returns a requests.Session object
	# body = scraper.get(start_urls[0]).content # => "<!DOCTYPE html><html><head>..."

	def parse(self, response):
		arr = response.xpath('//table[2]//td//text()').extract()

		langues =['German','Albanian','Arabic','Azerbaijan','Bosnian','Chinese',
		'Croatia','Czech','English','French','Georgian','Indonesia','Italian',
		'Malaysian','Netherlands','Persian','Polish','Portugese','Romanian',
		'Russian','Serbian','Spanish','Thai','Turkish','Ukrainian','Vietnamese']


		nothx = ['Partners']
		values={}
		done=[]
		tmpkey=""
		rez2={}


		for el in arr:
			print(el.strip())
			val=el.strip()

			if(val in langues):
				print('val in langues')
				#key=val
				done.append(val)

			if(val and val not in nothx and val not in langues):
				print('secondif')
				rez2['lang']=done[len(done)-1]
				rez2['name']=val
				rez2['url']="no"
				rez.append(rez2)
				rez2={}
			

		pass

		with open("result.json", "a") as outfile:
			outfile.write(json.dumps(rez,ensure_ascii=False,indent=4,sort_keys=True).encode('utf-8'))

		print('DONE')