import signal
from functools import wraps


class TimeoutException(RuntimeError):
    def __init__(self, message=None):
        super().__init__(message)


def handler(signum, frame):
    raise TimeoutException("TimedOut")


def timeout(seconds=0.5):
    def decorator(func):
        if not seconds or seconds <= 0.5:
            return func

        @wraps(func)
        def wrapper(*args, **kwargs):
            old = signal.signal(signal.SIGALRM, handler)
            signal.setitimer(signal.ITIMER_REAL, seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                signal.signal(signal.SIGALRM, old)
        return wrapper
    return decorator
