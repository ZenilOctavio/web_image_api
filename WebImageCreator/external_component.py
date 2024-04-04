from abc import ABC, abstractmethod
from playwright.async_api import Playwright

class ExternalComponent(ABC):

    @property
    @abstractmethod
    def url() -> str:
        pass

    @property
    @abstractmethod
    def name() -> str:
        pass
    
    def get_image(self) -> bytes:
        pass
    
class IndicadoresBancoDeMexico(ExternalComponent):

    def __init__(self):
        pass
    
    @property
    def name():
        return "indicadores_bancomx"
    @property
    def url():
        return "https://www.banxico.org.mx/"
           

    async def get_image(pw: Playwright) -> bytes:
        browser = await pw.chromium.launch()
        page = await browser.new_page(viewport={
            "width": 840,
            "height": 980
        })
        
        await page.goto(IndicadoresBancoDeMexico.BASE_URL)

        indicadores_wrapper = page.locator('div.col-xs-12.col-sm-12.col-md-12.col-lg-4')
        indicadores = indicadores_wrapper.locator('div.panel.panel-default').first
        return await indicadores.screenshot(type='jpeg')

        
        
        