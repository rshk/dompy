from itertools import product
import six


def make_column_classes(**kwargs):
    prefixes = ('xs', 'sm', 'md', 'lg')
    extras = ('offset', 'push', 'pull')

    classes = []

    names = []
    names.extend(prefixes)
    names.extend(
        '{}-{}'.format(p, e)
        for p, e in product(prefixes, extras))

    for name in names:
        value = kwargs.pop(name.replace('-', '_'), None)
        if value is not None:
            classes.append('col-{}-{}'.format(name, value))

    if len(kwargs):
        raise TypeError(
            "make_column_classes() got unexpected keyword arguments: {}"
            .format(', '.join(repr(k) for k in six.iterkeys(kwargs))))

    return classes
