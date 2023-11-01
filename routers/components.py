from fastapi import APIRouter, Response
from WebImageCreator.image_creator import ImageCreator
from models.first_component import TickerData, TickerDataList
from io import BytesIO


router = APIRouter()
image_creator = ImageCreator('./components')

@router.get('/components', tags=['components'])
async def get_components():
  components = await image_creator.get_components()

  return [component.name for component in components]

@router.post('/component/{component_name}')
async def get_component(component_name: str, context: TickerDataList):
  try: 
    component = await image_creator.get_component(component_name)
  except:
    return 'No such component'
  
  context_dict = context.json()
  
  image: bytes = await image_creator.use_component(component, context_dict)
  
  return Response(content=image, media_type='image/png')