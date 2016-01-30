from __future__ import absolute_import, unicode_literals

from dompy import tags


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
