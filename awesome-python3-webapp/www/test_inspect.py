# coding: utf-8

import inspect

def fn(a='', b=''):
    pass

def get_args(func):
    args = []
    params = inspect.signature(func).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.defautl == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)

if __name__ == '__main__':
    fn('1', '2.0')
    args = get_args(fn)
    print (args)
