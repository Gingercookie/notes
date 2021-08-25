def inspect(func):
    def wrapped_func(*args, **kwargs):
        print(f"Running {func.__name__}")
        val = func(*args, **kwargs)
        print(f"Result: {val}")
        return val
    return wrapped_func

@inspect
def combine(a, b):
    return a + b

class User:
    base_url = 'https://example.com/api'

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @classmethod
    def query(cls, query_string):
        return cls.base_url + '?' + query_string

    @staticmethod
    def name():
        return 'Kevin Bacon'

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"
