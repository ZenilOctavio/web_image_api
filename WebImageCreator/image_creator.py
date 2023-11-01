from .component_retriever import ComponentRetriever
from .component import Component
from .exceptions import ComponentFindException
import os
from typing import Union
from playwright.async_api import async_playwright
from jinja2 import Environment, FileSystemLoader
from .constants import DEFAULT_COMPONENTS_FOLDER, DEFAULT_JINJA2_FOLDER
from io import BytesIO
import asyncio

class ImageCreator:

  # async def __initialize_playwright(self):
  #   self.__playwright = await async_playwright().start()
  #   self.__browser = await self.__playwright.chromium.launch()
  
  def __init__(self, path_to_components: str = os.path.join('.', DEFAULT_COMPONENTS_FOLDER)):
    self.__retriever = ComponentRetriever(path_to_components)
    self.__retriever.read_components()
    self.__env = Environment(loader=FileSystemLoader(os.path.join(path_to_components, DEFAULT_JINJA2_FOLDER)))
    # asyncio.run(self.__initialize_playwright())

  async def get_components(self) -> list[Component]:
    return self.__retriever.Components
  
  async def refresh_components(self) -> None:
    self.__retriever.read_components()
  
  async def get_component(self, component_name: str):
    """This method returns the first occurence of the component saved with the given name."""
    component: Component
    for component in self.__retriever.Components:
      if component.name == component_name:
        return component
  
    raise ComponentFindException(f'No such component with name {component_name}')
  
  async def use_component(self, component: Union[str, Component], context: dict) -> bytes:
    
    async with async_playwright() as pw:
      browser = await pw.chromium.launch()
      
      if isinstance(component, str):
        component = await self.get_component(component)
    
      page = await browser.new_page()
      print(page)
    # try:
    #   print(browser)
    #   page = await browser.new_page()
    # except:
    #   print('Couldn\'t create a new page instance')
    #   return None
    
      template = self.__env.from_string(component.html_file)
      rendered_template = template.render(context)

      # print(rendered_template)
      # print(context)

      await page.set_content(rendered_template)
      # print(await page.content())
      await page.add_style_tag(content=component.css_file)

      image_bytes = await (await page.query_selector(component.selector)).screenshot(type='png')
    # await browser.close()
      return image_bytes
