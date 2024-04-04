from playwright.async_api import Browser, Page, Playwright
from .service import Service
from jinja2 import Environment, FileSystemLoader
from ..constants import DEFAULT_SERVICES_FOLDER
import os

class JinjaService(Service):

    def __init__(self, name: str, html_template: str, css_styles: str, selector: str, path_to_service: str, context: dict[str, str]) -> None:
        self.__html_template = html_template
        self.__css_styles = css_styles
        self.__selector = selector
        self.__context = context
        self.__env = Environment(loader=FileSystemLoader(os.path.join(DEFAULT_SERVICES_FOLDER, path_to_service)))
        super().__init__(name)

    #Getters and Setters
    @property
    def html_template(self) -> str:
        return self.__html_template

    @property
    def context(self) -> str:
        return self.__context
    
    @property
    def css_styles(self) -> str:
        return self.__css_styles

    @property
    def selector(self) -> str:
        return self.__selector

    @html_template.setter
    def set_html_template(self, html_template) -> str:
        self.__html_template = html_template

    @css_styles.setter
    def set_css_styles(self, css_styles) -> str:
        self.__css_styles = css_styles

    @selector.setter
    def set_selector(self, selector) -> str:
        self.__selector = selector

    @context.setter
    def set_context(self, context) -> str:
        self.__context = context
        
    
    async def configure_browser(self, pw: Playwright) -> Browser:
        browser = await pw.chromium.launch()
        return browser
    
    
    async def configure_page(self, browser: Browser) -> Page:
        page = await browser.new_page()  
        return page      
    
    
    async def get_image(self, pw: Playwright) -> bytes:
        browser = await self.configure_browser(pw)
        page = await self.configure_page(browser)
        
        template = self.__env.from_string(self.html_template)
        rendered_template = template.render(self.context)
        await page.set_content(rendered_template)
        await page.add_style_tag(content= self.css_styles)
        
        selector = await page.query_selector(self.selector)
        image_bytes = await selector.screenshot(type='png')
        
        return image_bytes
        
