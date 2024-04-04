from abc import ABC, abstractmethod
from playwright.async_api import Page, Playwright, Browser

class Service(ABC):
    
    def __init__(self, name: str):
        self.__name = name
    
    @abstractmethod
    async def get_image(self, pw: Playwright) -> bytes:
        pass
    
    @abstractmethod
    async def configure_browser(self, pw: Playwright) -> Browser:
        pass

    @abstractmethod
    async def configure_page(self, browser: Browser) -> Page:
        pass
    
    @property
    @abstractmethod
    def service_name(self) -> str:
        return self.__name
    