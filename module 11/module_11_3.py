"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV

Интроспекция
"""





class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'Hi, my name is {self.name}, i`m {self.age} years old')

def introspection_info(obj):
    _type = type(obj)
    _attr = vars(obj) if hasattr(obj, '__dict__') else None
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    module = obj.__class__.__module__

    return {
        'type':_type,
        'attributes':_attr,
        'methods' : methods,
        'module': module
    }


me = MyClass('Vova', 22)
num = 42
print(introspection_info(me))
print(introspection_info(num))
