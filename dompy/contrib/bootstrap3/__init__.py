from functools import partial

from dompy import tags

from .forms import *  # noqa
from .utils import make_column_classes


def column(**kwargs):
    classes = make_column_classes(**kwargs)
    return partial(tags.Div, class_=' '.join(classes))


def row():
    return partial(tags.Div, class_='row')


def container(fluid=False):
    class_ = 'container-fluid' if fluid else 'container'
    return partial(tags.Div, class_=class_)


def table(striped=False, bordered=False, hover=False, condensed=False):
    classes = ['table']
    if striped:
        classes.append('table-striped')
    if bordered:
        classes.append('table-bordered')
    if hover:
        classes.append('table-hover')
    if condensed:
        classes.append('table-condensed')
    return partial(tags.Table, class_=' '.join(classes))
