# from pathlib import Path

import scrapy
from ..items import DbScrapingItem
import os
import csv 

class DbscrapingSpider(scrapy.Spider):
    name = "db_scraping"

    def start_requests(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        yield scrapy.Request(url='https://www.transfermarkt.fr/spieler-statistik/wertvollstemannschaften/marktwertetop/',headers=headers ,  callback=self.parse)
          

    def parse(self, response):
        # paginate resulsts
        club_lists = response.css('tr.odd a::attr(href), tr.even a::attr(href)').extract()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        for club_list in club_lists:   
            next_page = response.urljoin(club_list)
            if next_page:
                yield scrapy.Request(url=next_page, headers=headers ,  callback=self.parse_next_page)
            else:
                return
    
    def parse_next_page(self, response):
        players = response.css('tr.odd a::attr(href), tr.even a::attr(href)').extract()
        for player in players:
            next_page = response.urljoin(player)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            if next_page:
                yield scrapy.Request(url=next_page, headers=headers ,  callback=self.get_data)
            else:
                return
    
    def get_data(self , response):
        data_elements  = response.css('.info-table__content--bold')
        index = 0
        item = DbScrapingItem()
        name = ''
        for element in data_elements:
            content = element.xpath('text()').get().strip()
            print('=====>', content)
            if index == 0:
                item['player_name'] = content
                name = content
            if index == 3 : 
                item['player_weight'] = content

            if index == 5 : 
                item['player_position'] = content
            
            if index == 6 : 
                item['player_strong_foot'] = content
            
            index = index + 1
        yield item 