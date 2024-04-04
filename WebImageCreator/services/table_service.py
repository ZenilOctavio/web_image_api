from .jinja_service import JinjaService
import os
from ..constants import DEFAULT_SERVICES_FOLDER

class TableService(JinjaService):
    service_name = 'table_service'
    
    def __init__(self, context: dict[str, str]):
        self.__name = TableService.service_name
        abs_path = os.path.abspath('.')
        self.__files_path = os.path.join(abs_path, DEFAULT_SERVICES_FOLDER, self.__name)
        
        html_template = self.load_html_file()
        css_styles = self.load_css_file()
                
        super().__init__(self.__name, html_template, css_styles, 'section', self.__files_path, context)
    
        
    def load_html_file(self) -> str:
        content: str
        with open(os.path.join(self.__files_path, 'index.html'), 'r', encoding='utf-8') as html_file:
            content = html_file.read()
        
        return content

    def load_css_file(self) -> str:

        content: str
        with open(os.path.join(self.__files_path, 'index.css'), 'r', encoding='utf-8') as html_file:
            content = html_file.read()
        
        return content

