from django.http import HttpResponse
from django.conf import settings
import redis
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=0)



def test_redis(request):
    
    views = redis_instance.get('views')
    if not views:
        views = 0
    else:
        views = int(views) + 1
    redis_instance.set('views', views)
    return HttpResponse(' <h1>salam {}</h1>'.format(views))
