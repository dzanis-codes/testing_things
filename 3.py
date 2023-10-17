https://docs.docker.com/desktop/install/windows-install/

docker pull scrapinghub/splash


Run the Splash Container:

After pulling the image, you can run a Splash container with the following command:

bash
Copy code
docker run -it -p 8050:8050 scrapinghub/splash
This command will start the Splash container and map port 8050 in the container to port 8050 on your host machine.

Access Splash Web Interface:

You can access the Splash web interface by opening a web browser and navigating to http://localhost:8050. This web interface allows you to test Splash, explore its capabilities, and inspect rendered pages.

Configure Scrapy to Use Splash:

In your Scrapy project, when making requests to websites where JavaScript rendering is required, use the SplashRequest class to specify that you want to use Splash. Here's an example, as shown in the earlier Scrapy spider:
from scrapy_splash import SplashRequest

class MySpider(scrapy.Spider):
    # ...
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 2})
    # ...







pip install scrapy-splash
