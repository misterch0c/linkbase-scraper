# -*- coding: utf-8 -*-

import scrapy
import logging
import cfscrape
from scrapy.spiders import Spider
import json
from scrapy import log,signals, Field
from scrapy.item import Item
from scrapy.http import Request



rez=[]


class LinkbaseSpider(Spider):

	name = "linkbase"
	#allowed_domains = ['127.0.0.1'] #commented = * 
	start_urls = (
		'file://127.0.0.1/home/unkn0wn/web/linkbase/linkb/link.html',
	) 
	# scraper = cfscrape.create_scraper() # returns a requests.Session object
	# body = scraper.get(start_urls[0]).content # => "<!DOCTYPE html><html><head>..."
	def parse(self, response):
		arr = response.xpath('//table[2]//td//text()').extract()
		arr2 = response.xpath('//table[2]//td//@href').extract()


	#dirty but It doesn't work when I check for multiple string at once..?
		for link in arr2:
			if '#' in link:
				arr2.remove(link)
		for link in arr2:
			if 'nachricht.co' in link:
				arr2.remove(link)	
		for link in arr2:
			if 'report_link' in link:
				arr2.remove(link)		
		for link in arr2:
			if 'vanille' in link:
				arr2.remove(link)		
		for link in arr2:
			if 'bit.ly' in link:
				arr2.remove(link)		




		langues =['German','Albanian','Arabic','Azerbaijan','Bosnian','Chinese',
		'Croatia','Czech','English','French','Indonesia','Italian',
		'Malaysian','Netherlands','Persian','Polish','Portuguese','Romanian',
		'Russian','Serbian','Spanish','Thai','Turkish','Ukrainian','Vietnamese']

		nothx = ['Partners','Georgian']
		values={}
		done=[]
		tmpkey=""
		rez2={}
		i=-1


		for el in arr:
			print(el.strip())
			val=el.strip()
			if(val in langues):
				print('val in langues')
				#key=val
				done.append(val)
			# if i>2:
			# 	break
			if(val and val not in nothx and val not in langues):
				print('secondif')
				i=i+1
				url=arr2[i]
				scraper = cfscrape.create_scraper() # returns a requests.Session object
				body = scraper.get(url).content # => "<!DOCTYPE html><html><head>..."
				single_resp=response.replace(body=body)


				


				tmpurl=single_resp.xpath('//iframe/@src').extract()
				rez2['url']=tmpurl
				rez2['lang']=done[len(done)-1]
				rez2['name']=val
				
				
				print('ASSIGNING')
				print(tmpurl)
				print('TOOOO')
				print(val)

				rez2['linkbase_url']=url
				rez.append(rez2)
				rez2={}



				print("UUUUU")



				#yield Request(url,callback=self.parse2)
		#request.meta['item'] = item
				#return request


		with open("result.json", "a") as outfile:
			outfile.write(json.dumps(rez,ensure_ascii=False,indent=4,sort_keys=True).encode('utf-8'))

		print('DONE')
