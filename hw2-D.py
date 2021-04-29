from functools import wraps


def counter(f):
    def reset():
        wrapped.rdepth = 0
        wrapped.ncalls = 0

    @wraps(f)
    def wrapped(*args, **kwargs):
        if wrapped.depth == 0:
            reset()

        wrapped.depth += 1
        wrapped.ncalls += 1
        wrapped.rdepth = max(wrapped.rdepth, wrapped.depth)

        try:
            return f(*args, **kwargs)
        finally:
            wrapped.depth -= 1

    wrapped.depth = 0
    reset()
    return wrapped
