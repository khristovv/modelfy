class ModelMeta(type):
    def __call__(cls, *ars, **kwargs):
        print('in __call__')

    def __new__(cls, *args, **kwargs):
        print('in __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('in __init__')


class Model(metaclass=ModelMeta):
    def __call__(cls, *ars, **kwargs):
        print('in __call__')

    def __new__(cls, *args, **kwargs):
        print('in __new__')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        print('in __init__')


if __name__ == "__main__":
    m = Model()
    print(m)
