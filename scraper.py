import scrapy

#Scraper tutorial
# class BrickSetSpider(scrapy.Spider):
#     name = "brickset_spider"
#     start_urls = ['http://brickset.com/sets/year-2020']
#     user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

#     def parse(self, response):
#         SET_SELECTOR = '.set'
#         for brickset in response.css(SET_SELECTOR):

#             NAME_SELECTOR = 'h1 ::text'
#             PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
#             MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
#             IMAGE_SELECTOR = 'img ::attr(src)'
#             yield {
#                 'name': brickset.css(NAME_SELECTOR).extract_first(),
#                 'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
#                 'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
#                 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#             }
            
#         NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
#         next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )

#The Guardian
class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.theguardian.com/world/china']
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        SET_SELECTOR = '.u-faux-block-link__overlay'
        for brickset in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'a ::text'
            HREF_SELECTOR = 'a ::attr(href)'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
                'href': brickset.css(HREF_SELECTOR).extract_first(),
            }
        NEXT_PAGE_SELECTOR = './/div[@class="pagination--full"]/div[@class="pagination__list"]/a/@href'
        next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )


#J-list
# class BrickSetSpider(scrapy.Spider):
#     name = "brickset_spider"
#     start_urls = ['https://www.jlist.com/category/books-magazines/how-to-draw']
#     user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

#     def parse(self, response):
#         SET_SELECTOR = '.item'
#         for brickset in response.css(SET_SELECTOR):

#             NAME_SELECTOR = './/h2/a/text()'
#             IMAGE_SELECTOR = 'img ::attr(src)'
#             PRICE_SELECTOR = './/div[@class="price-box"]/span[@class="regular-price"]/span/text()'
#             URL_SELECTOR = './/h2/a/@href'
#             yield {
#                 'name': brickset.xpath(NAME_SELECTOR).extract_first(),
#                 'image': brickset.css(IMAGE_SELECTOR).extract_first(),
#                 'price': brickset.xpath(PRICE_SELECTOR).extract_first(),
#                 'url': brickset.xpath(URL_SELECTOR).extract_first()
#             }
            
#         NEXT_PAGE_SELECTOR = './/div[@class="pager"]/div[@class="pages"]/ol/li/a/@href'
#         next_page = response.xpath(NEXT_PAGE_SELECTOR).extract_first()
#         if next_page:
#             yield scrapy.Request(
#                 response.urljoin(next_page),
#                 callback=self.parse
#             )