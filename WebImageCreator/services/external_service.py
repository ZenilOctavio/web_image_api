from .service import Service
from playwright.async_api import Playwright

class ExternalService(Service):
    def __init__(self, name: str, url: str, selector: str):
        self.__name = name
        self.__url = url
        self.__selector = selector
        
        super().__init__(name)
        
    @property
    def url(self) -> str:
        return self.__url

    @property
    def selector(self) -> str:
        return self.__selector

    @url.setter
    def set_url(self, url):
        self.__url = url

    @selector.setter
    def set_selector(self, selector):
        self.__selector = selector
        
        
    async def get_image(self, pw: Playwright) -> bytes:
    
        browser = await self.configure_browser(pw)
        page = await self.configure_page(browser)
                
        indices_selector = await page.query_selector(self.selector)
        image_bytes = await indices_selector.screenshot(type='png')
    
        return image_bytes
        