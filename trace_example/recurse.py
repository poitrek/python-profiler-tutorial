
def recurse(lvl):
    print('calling recurse({})'.format(lvl))
    if lvl > 0:
        recurse(lvl-1)


def forgotten_func():
    print('This function is forgotten and never called.')
