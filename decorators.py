import functools


def log_action(action_type):
    def decorate(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{action_type}] Executing: {func.__name__}")
            return func(*args, **kwargs)

        return wrapper
    return decorate
