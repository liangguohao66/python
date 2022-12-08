class Mymeta(type):
    def __init__(self, name, bases, dic):
        super().__init__(name, bases, dic)
        print('===>Mymeta.__init__')
        print(self.__name__)
        print(dic)
        print("yaml_tag:", self.yaml_tag)
        #if 'yaml_tag' in kwargs and kwargs['yaml_tag'] is not None:
        #    cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)

    def __new__(cls, *args, **kwargs):
        print('===>Mymeta.__new__')
        print(cls.__name__)
        return type.__new__(cls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('===>Mymeta.__call__')
        obj = cls.__new__(cls)
        cls.__init__(cls, *args, **kwargs)
        print('===>Mymeta.__call_end')
        return obj
    
class Foo(metaclass=Mymeta):
    yaml_tag = '!Foo'

    def __init__(self, name):
        print('Foo.__init__')
        self.name = name

    def __new__(cls, *args, **kwargs):
        print('Foo.__new__')
        return object.__new__(cls)

foo = Foo('foo')
