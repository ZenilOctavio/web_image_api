from fastapi import APIRouter
from WebImageCreator.image_creator import ImageCreator
from models.first_component import TickerData, TickerDataList

router = APIRouter()
image_creator = ImageCreator('./components')

@router.get('/components', tags=['components'])
async def get_components():
  components = await image_creator.get_components()

  return [component.name for component in components]

@router.post('/component/')
async def get_component(context: TickerDataList):
  return context.json()