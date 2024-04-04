from .services.service import Service
from playwright.async_api import async_playwright
from typing import Type, Any

class ImageDeliverer:

    def __init__(self, services: list[Type[Service]]) -> None:
        self.__services = services
        self.__playwright = async_playwright()
    
    @property
    def services(self):
        return self.__services
    
    @services.setter
    def set_services(self, services: list[Type[Service]]):
        self.__services = services 
    
    def find_service(self, service_name: str) -> Type[Service]:
        for service in self.services:
            if service.service_name == service_name:
                return service
            
    async def use_service(self, service: Type[Service], context: dict[str, Any]) -> bytes:
        service_instance = service(context)
        
        pw = await self.__playwright.start()
        image_bytes = await service_instance.get_image(pw)
        await pw.stop()
        
        return image_bytes