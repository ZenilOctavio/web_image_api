from fastapi import APIRouter

router = APIRouter()

@router.get('/components', tags=['components'])
def get_components():
  return ['component1', 'component2', 'component3']