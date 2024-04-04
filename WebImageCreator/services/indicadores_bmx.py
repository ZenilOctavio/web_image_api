from playwright.async_api import Browser, Page, Playwright
from .external_service import ExternalService

class IndicadoresBancoDeMexico(ExternalService):
    service_name: str = 'indicadores_bancomx'
    
    def __init__(self, *args, **kwargs):
        self.__name = IndicadoresBancoDeMexico.service_name
        self.__url = 'https://www.banxico.org.mx/'
        self.__selector = 'div#content > div.container > div.row > div.col-xs-12.col-sm-12.col-md-12.col-lg-4 > div.panel-default'
        
        super().__init__(self.__name, self.__url, self.__selector)
    
    
    async def configure_page(self, browser: Browser) -> Page:
        page = await browser.new_page(viewport={
            "width": 840,
            "height": 980
        })
        
        await page.goto(self.url)
        
        return page
    
    async def configure_browser(self, pw: Playwright) -> Browser:
        return await pw.chromium.launch()
    

        