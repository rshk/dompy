from __future__ import absolute_import, unicode_literals

import six
import io


class Tag(object):
    name = None
    has_content = False
    raw_text = False

    def __init__(self, attrs=None):
        self._attrs = {}
        if attrs is not None:
            self._attrs.update(attrs)
        self.children = []

    # ---------- Attribute manipulation

    def __getitem__(self, name):
        return self._attrs[name]

    def __setitem__(self, name, value):
        self._attrs[name] = value

    def __delitem__(self, name):
        del self._attrs[name]

    # ---------- Children manipulation

    def append(self, *children):
        self.children.extend(children)
        return self  # allow chaining

    # ---------- Serialization

    def __str__(self):
        out = io.StringIO()
        out.write('<{}'.format(self.name))

        for key, val in sorted(six.iteritems(self._attrs)):
            out.write(' {}="{}"'.format(key, html_escape(val)))

        out.write('>')

        if self.has_content:
            for child in self.children:
                out.write(self._format_child(child))
            out.write('</{}>'.format(self.name))

        return out.getvalue()

    def _format_attribute(self, name, value):
        return '{}="{}"'.format(name, html_escape(value))

    def _format_child(self, child):
        text_form = six.text_type(child)

        if isinstance(child, (Tag, Safe)) or self.raw_text:
            # TODO if raw_text, valdate that it doesn't contain </script>
            return text_form

        return html_escape(text_form)


# See: http://dev.w3.org/html5/html-author/#index-of-elements
_EMPTY_TAGS = [
    'area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input',
    'link', 'meta', 'param', 'source']
_KNOWN_TAGS = [
    'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b',
    'base', 'bb', 'bdo', 'blockquote', 'body', 'br', 'button',
    'canvas', 'caption', 'cite', 'code', 'col', 'colgroup', 'command',
    'datagrid', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog',
    'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figure', 'footer',
    'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header',
    'hr', 'html', 'i', 'iframe', 'img', 'input', 'ins', 'kbd',
    'label', 'legend', 'li', 'link', 'map', 'mark', 'menu', 'meta',
    'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 'option',
    'output', 'p', 'param', 'pre', 'progress', 'q', 'rp', 'rt',
    'ruby', 'samp', 'script', 'section', 'select', 'small', 'source',
    'span', 'strong', 'style', 'sub', 'sup', 'table', 'tbody', 'td',
    'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'ul',
    'var', 'video']
_RAW_TEXT_TAGS = ['script']  # others?


class TagFactory(object):

    def __init__(self):
        self._cached_tags = {}

    def __getattr__(self, name):
        name = name.lower()

        if name not in _KNOWN_TAGS:
            raise AttributeError('{} is not a known HTML5 tag'.format(name))

        if name not in self._cached_tags:
            self._cached_tags[name] = self._create_tag(name)

        return self._cached_tags[name]

    def _create_tag(self, name):
        return type(name.title(), (Tag,), {
            'name': name,
            'has_content': name not in _EMPTY_TAGS,
            'raw_text': name in _RAW_TEXT_TAGS,
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
