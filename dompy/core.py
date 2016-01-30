from __future__ import absolute_import, unicode_literals

import six


class Tag(object):
    name = None
    has_content = False

    def __init__(self, *children, **attrs):
        if not self.has_content and len(children):
            raise ValueError('This tag does not support children')

        self.children = list(children)
        self.attrs = self._normalize_attrs(attrs)

    def _normalize_attrs(self, attrs):
        new_attrs = {}

        for key, val in six.iteritems(attrs):
            key = self._normalize_attribute_name(key)
            new_attrs[key] = val

        return new_attrs

    def _normalize_attribute_name(self, name):
        return name.lower().strip('_-').replace('_', '-')

    def __str__(self):
        attrs = ' '.join(
            self._format_attribute(key, val)
            for key, val in sorted(self.attrs.items()))

        if attrs:
            attrs = ' ' + attrs

        if self.has_content:
            content = ''.join(self._format_child(x) for x in self.children)
            return '<{name}{attrs}>{content}</{name}>'.format(
                name=self.name, attrs=attrs, content=content)

        return '<{name}{attrs}>'.format(name=self.name, attrs=attrs)

    def _format_attribute(self, name, value):
        return '{}="{}"'.format(name, html_escape(value))

    def _format_child(self, child):
        text_form = six.text_type(child)

        if isinstance(child, (Tag, Safe)):
            return text_form

        return html_escape(text_form)


class TagFactory(object):

    _UNCLOSED_TAGS = ['img', 'hr', 'br', 'link', 'meta']  # todo: others?

    def __init__(self):
        self._cached_tags = {}

    def __getattr__(self, name):
        name = name.lower()
        if name not in self._cached_tags:
            self._cached_tags[name] = self._create_tag(name)
        return self._cached_tags[name]

    def _create_tag(self, name):
        has_content = name not in self._UNCLOSED_TAGS
        return type(name.title(), (Tag,), {
            'name': name,
            'has_content': has_content,
        })


class Safe(object):  # Safe value
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# ----------------------------------------------------------------------
# Utils

try:
    from html import escape as html_escape

except ImportError:
    def html_escape(s, quote=True):  # Backport from 3.5
        """
        Replace special characters "&", "<" and ">" to HTML-safe sequences.
        If the optional flag quote is true (the default), the quotation mark
        characters, both double quote (") and single quote (')
        characters are also translated.
        """
        s = s.replace("&", "&amp;")  # Must be done first!
        s = s.replace("<", "&lt;")
        s = s.replace(">", "&gt;")
        if quote:
            s = s.replace('"', "&quot;")
            s = s.replace('\'', "&#x27;")
        return s
