from .component_retriever import ComponentRetriever
from .component import Component
from .exceptions import ComponentFindException
import os
from typing import Union
from playwright.sync_api import sync_playwright
from jinja2 import Template
from .constants import DEFAULT_COMPONENTS_FOLDER, DEFAULT_JINJA2_FOLDER
from io import BufferedRandom

class ImageCreator:
  
  def __init__(self, path_to_components: str = os.path.join('.', DEFAULT_COMPONENTS_FOLDER)):
    self.__retriever = ComponentRetriever(path_to_components)
    self.__retriever.read_components()
    self.__playwright = sync_playwright().start()
    self.__browser = self.__playwright.chromium.launch()
    
  
  def get_components(self) -> list[Component]:
    return self.__retriever.Components
  
  def refresh_components(self) -> None:
    self.__retriever.read_components()
  
  def get_component(self, component_name: str):
    """This method returns the first occurence of the component saved with the given name."""
    component: Component
    for component in self.__retriever.Components:
      if component.name == component_name:
        return component
  
    raise ComponentFindException(f'No such component with name {component_name}')
  
  def use_component(self, component: Union[str, Component], context: dict) -> BufferedRandom:
    
    if isinstance(component, str):
      component = self.get_component(component)
    
    page = self.__browser.new_page()
    
    template = Template(component.html_file)
    rendered_template = template.render(context)

    page.set_content(rendered_template)
    page.add_script_tag(component.css_file)
    photo_bytes = page.query_selector(component.selector).screenshot(type='png')

    # page = self.__browser.new_page()
    
    buffer = BufferedRandom(photo_bytes)
    
    return buffer
    