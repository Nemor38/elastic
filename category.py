from fastapi import APIRouter, HTTPException
from ..models.category import CategoryIndex

router = APIRouter()

@router.get('/search')
def search(query: str):
    results = CategoryIndex.search(query)
    return results['hits']['hits']
