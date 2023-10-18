import scrapy

class SinglePageSpider(scrapy.Spider):
    name = 'single_page_spider'
    start_urls = ['https://www.barbora.lv/piena-produkti-un-olas?page=2']  # Replace with the URL of the webpage you want to scrape

    def parse(self, response):
        # Extract the entire HTML content of the page
        page_content = response.body_as_unicode()

        # Save the HTML content to a text file
        with open('page_content.html', 'w', encoding='utf-8') as file:
            file.write(page_content)

        self.log(f'Page content saved to page_content.html')
