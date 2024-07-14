from elasticsearch.helpers import bulk
from ..models.category import CategoryIndex
import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

class CategoryService:
    @staticmethod
    def update_category_index(categories, task_id):
        redis_client.set(task_id, 'in_progress')
        try:
            bulk(CategoryIndex.es, [{
                '_op_type': 'index',
                '_index': CategoryIndex.INDEX_NAME,
                '_id': cat['id'],
                '_source': cat
            } for cat in categories])
            redis_client.set(task_id, 'completed')
        except Exception as e:
            redis_client.set(task_id, f'failed: {str(e)}')
