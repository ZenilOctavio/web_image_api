from fastapi.routing import APIRouter, Response
from WebImageCreator import ImageDeliverer, TableService, IndicadoresBancoDeMexico
from typing import Any
from pydantic import BaseModel

router = APIRouter(prefix='/services')
image_deliverer = ImageDeliverer([TableService, IndicadoresBancoDeMexico])


class ContextModel(BaseModel):
    context: None | dict[str, Any] 


@router.get('/', tags=['services'])
async def get_services():
    services_names: list[str] = []
    for service in image_deliverer.services:
        services_names.append(service.service_name)
    
    return services_names

@router.put('/get_image/{service_name}', tags=['services'])
async def get_image_from_service(service_name: str, context_model: ContextModel):
    service = image_deliverer.find_service(service_name)
    image_bytes = await image_deliverer.use_service(service, context_model.context)

    
    return Response(content=image_bytes, status_code=200, media_type='image/png')


