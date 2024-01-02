# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DbScrapingItem(scrapy.Item):
    player_name  = scrapy.Field()
    player_first_name  = scrapy.Field()
    player_age  = scrapy.Field()
    player_position   = scrapy.Field()
    player_birth_date  = scrapy.Field()
    player_staf = scrapy.Field() 
    player_club_name = scrapy.Field() 
    player_strong_foot = scrapy.Field() 
    player_nationality = scrapy.Field() 
    player_starting_at = scrapy.Field()
    player_ending_at = scrapy.Field()
    player_weight = scrapy.Field()
    player_full_name = scrapy.Field()
    pass
