import os
from .component import Component
from .exceptions import ComponentPathException, ComponentDirectoryException, ComponentFileException
from enum import Enum

class AcceptedFiles(Enum):
  HTML='.html'
  JINJA='.jinja'
  CSS='.css'
  # JS='.js'
  TXT='.txt'

class ComponentRetriever:

  def __verify_path(self, path: str) -> None:
    if not os.path.exists(path):
      raise ComponentPathException(f'Path doesn\'t exists: {path}')

    if not os.path.isdir(path):
      raise ComponentPathException(f'Given path is a file: {path}')
    
    
  def __init__(self, components_path: str):
    self.__components: str[Component] = []
    self.__verify_path(components_path)
    self.__path = components_path
    
  @property
  def Components_path(self) -> str:
    return self.__path

  @Components_path.setter
  def Components_path(self, new_path):
    
    self.__verify_path(new_path)
    
    self.__path = new_path

  @property
  def Components(self) -> list[Component]:
    return self.__components
    
  def read_components(self) -> list[Component]:
    if not self.__directory_parsed():
      raise ComponentDirectoryException('Component directory is not correcly parsed')

    components: list[Component] = []

    jinja2_path = os.path.join(os.path.abspath(self.__path), 'jinja2')
    
    for directory in os.listdir(jinja2_path):
      if os.path.isfile(os.path.join(jinja2_path, directory)):
        continue

      html_file = open(os.path.join(os.path.abspath(self.__path),'jinja2',directory,'file.jinja'))
      css_file = open(os.path.join(os.path.abspath(self.__path),'jinja2',directory,'file.css'))
      
      components.append(Component(directory.split('.')[0],'section',html_file.read(),css_file.read()))

      html_file.close()
      css_file.close()
    
    self.__components = components
    
    return self.__components

  
  def __directory_parsed(self) -> bool:
    directories = os.listdir(self.__path)

    #check jinja2
    if not 'jinja2' in directories:
      raise ComponentDirectoryException('There isn\'t a jinja2 directory')
    
    jinja2_directories = os.listdir(f'{self.__path}/jinja2')

    root_file: bool = False

    for directory in jinja2_directories:
      if (directory == 'root.html.jinja'):
        root_file = True
        continue
      
      self.__check_file_types_jinja2(f'{self.__path}/jinja2/{directory}')
      # self.__read_component_data(directory)
      
      
        
    if not root_file:
      raise ComponentDirectoryException('No root file in the directory')
    
    return True
  
  def __check_file_types_jinja2(self, directory_path: str) -> bool:
    files = os.listdir(directory_path)
    
    accepted_file_types = [filetype.value for filetype in AcceptedFiles._member_map_.values()]
    
    for file in files:
      file_extension = '.'+file.split('.')[-1]
      if file_extension not in accepted_file_types:
        raise ComponentFileException(f'File extension for {file} not accepted - ({accepted_file_types})')
    
    return True
      
  def __read_component_data(self, component_path: str) -> (str, list[type]):
    #To implement
    pass