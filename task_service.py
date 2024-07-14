import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0)

class TaskService:
    @staticmethod
    def set_status(task_id, status):
        redis_client.set(task_id, status)

    @staticmethod
    def get_status(task_id):
        status = redis_client.get(task_id)
        return status.decode('utf-8') if status else None
