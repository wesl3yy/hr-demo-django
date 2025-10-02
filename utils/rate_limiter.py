import time

from django.http.response import JsonResponse
from functools import wraps


RATE_LIMIT_STORE = {}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def rate_limit(max_requests: int, window_seconds: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) < 2:
                return JsonResponse({"error": "Invalid request"}, status=400)

            request = args[1]
            client_ip = get_client_ip(request)
            now = time.time()
            timestamps = RATE_LIMIT_STORE.get(client_ip, [])

            timestamps = [ts for ts in timestamps if now - ts < window_seconds]

            if len(timestamps) >= max_requests:
                return JsonResponse(
                    {"error": "Rate limit exceeded. Try later."},
                    status=429
                )

            timestamps.append(now)
            RATE_LIMIT_STORE[client_ip] = timestamps
            return func(*args, **kwargs)

        return wrapper
    return decorator
