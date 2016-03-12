from __future__ import absolute_import, unicode_literals

from dompy import tags
from dompy.core import Tag


class TestTagsBehaveAsNormalClasses(object):

    def test_same_tag_has_same_type(self):
        type1 = type(tags.Div())
        type2 = type(tags.Div())
        assert type1 is type2

    def test_different_tags_have_different_types(self):
        type1 = type(tags.Div())
        type2 = type(tags.Span())
        assert type1 is not type2

    def test_class_has_correct_name(self):
        assert tags.Div.__name__ == 'Div'
        assert tags.Div.name == 'div'
        assert tags.Div.has_content is True

    def test_img_has_no_content(self):
        assert tags.Img.__name__ == 'Img'
        assert tags.Img.name == 'img'
        assert tags.Img.has_content is False

    def test_tag_isinstance_tag(self):
        div = tags.Div()
        assert isinstance(div, Tag)


class TestTagAttributes(object):

    def test_attribute_can_be_set(self):
        div = tags.Div()
        div['class'] = 'myclass'
        assert str(div) == '<div class="myclass"></div>'

    def test_attribute_can_be_changed(self):
        div = tags.Div({'class': 'original'})
        div['class'] = 'myclass'
        assert str(div) == '<div class="myclass"></div>'

    def test_attribute_can_be_deleted(self):
        div = tags.Div({'class': 'original'})
        del div['class']
        assert str(div) == '<div></div>'

    def test_attribute_can_be_read(self):
        div = tags.Div({'class': 'original'})
        assert div['class'] == 'original'


class TestChildrenAppend(object):

    def test_create_tag_with_children(self):
        div = tags.Div({'class': 'foobar'}).append(
            'Hello, ', tags.Strong().append('World!'))
        assert str(div) == \
            '<div class="foobar">Hello, <strong>World!</strong></div>'
