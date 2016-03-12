from dompy import tags

__all__ = []


def form(*children, **attrs):
    horizontal = attrs.pop('horizontal', False)
    inline = attrs.pop('inline', False)

    classes = []
    if horizontal:
        classes.append('form-horizontal')
    if inline:
        classes.append('form-inline')
    if len(classes):
        attrs['class_'] = ' '.join(classes)
    return tags.Form(*children, **attrs)


def form_group(*children):
    return tags.Div({'class': 'form-group'}, *children)


def form_input(type_='text', name=None, id=None, label=None, placeholder=None):
    label_kwargs = {}
    input_kwargs = {'type_': type_}

    if id is None and name:
        id = 'input-{}'.format(name)
    if label is None and name:
        label = name.replace('-', ' ').title()

    if name:
        input_kwargs['name'] = name

    if id:
        label_kwargs['for_'] = id
        input_kwargs['id'] = id

    if placeholder:
        input_kwargs['placeholder'] = placeholder


def form_buttons_group():
    pass
