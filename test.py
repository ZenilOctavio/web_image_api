from WebImageCreator.services.table_service import TableService
from WebImageCreator.image_deliverer import ImageDeliverer
from playwright.async_api import async_playwright
import asyncio


async def main():
    img_deliverer = ImageDeliverer([TableService])   
    
    bytes = await img_deliverer.use_service('table_service', {
        "logs": [
            {
                "name": "PESO-DOLAR",
                "open": "16.5",
                "close": "17",
                "change": 15
            },
            {
                "name": "hola",
                "open": "a",
                "close": "todo",
                "change": 1234
            },
            {
                "name": "hola",
                "open": "a",
                "close": "todo",
                "change": 1234
            },
        ]
    })
    
    with open('image.png','wb') as fil:
        fil.write(bytes)

asyncio.run(main())