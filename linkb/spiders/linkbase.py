# -*- coding: utf-8 -*-

import scrapy
import cfscrape
from scrapy.spiders import Spider

rez={}

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
		langues =['German','Albanian','Chinese']
		nothx = ['Partners']
		values=[]
		


		for el in arr:
			print(el.strip())
			val=el.strip()

			if(val in langues):
				print('val in langues')
				key=val
				
				rez[key]=values

			if(val and val not in nothx and val not in langues):
				print('secondif')
				values.append(val)
				#rez[key]=val;
			

		print("0000000000000000000000000000")

		pass

		print(rez)
	