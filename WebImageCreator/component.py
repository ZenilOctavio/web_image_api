from dataclasses import dataclass
from enum import Enum

# DataTypes = Enum('DataTypes', ['Number', 'String'])  

class DataTypes(Enum):
  Number=1
  String=1

@dataclass
class Component:
  name: str
  selector: str
  html_file: str
  css_file: str
  # js_file: str
  #Variable name and DataType
  # context: dict[str, DataTypes]
