from __future__ import absolute_import, unicode_literals

from dompy import tags, Safe


def test_serialize_empty_div():
    html = str(tags.Div())
    assert html == '<div></div>'


def test_serialize_empty_div_with_attribute():
    html = str(tags.Div({'class': 'foobar'}))
    assert html == '<div class="foobar"></div>'


def test_serialize_empty_div_with_two_attributes():
    html = str(tags.Div({'class': 'foobar', 'role': 'foo'}))
    assert html == '<div class="foobar" role="foo"></div>'


def test_serialize_empty_div_with_data_attribute():
    html = str(tags.Div({'data-foo': 'bar'}))
    assert html == '<div data-foo="bar"></div>'


def test_serialize_div_with_text():
    html = str(tags.Div('Hello, world!'))
    assert html == '<div>Hello, world!</div>'


def test_serialize_nested_divs():
    html = str(tags.Div(tags.Div()))
    assert html == '<div><div></div></div>'


def test_serialize_empty_img():
    html = str(tags.Img())
    assert html == '<img>'


def test_serialize_img_with_attribute():
    html = str(tags.Img({'src': 'http://example.com/foo.png'}))
    assert html == '<img src="http://example.com/foo.png">'


def test_serialize_simple_html_page():
    dom = tags.Html(
        tags.Head(
            tags.Title('Page title'),
            tags.Link({'rel': 'stylesheet', 'type': 'text/css',
                       'href': 'style.css'}),
            ),
        tags.Body(
            tags.Nav({'id': 'main-nav', 'class': 'navigation'}),
            tags.H1('Page title!'),
            tags.P('Text paragraph'),
        ),
    )

    html = str(dom)

    assert html == (
        '<html><head><title>Page title</title>'
        '<link href="style.css" rel="stylesheet" type="text/css">'
        '</head><body><nav class="navigation" id="main-nav"></nav>'
        '<h1>Page title!</h1><p>Text paragraph</p></body></html>')


def test_text_is_escaped():
    html = str(tags.P('Text <br> text'))
    assert html == '<p>Text &lt;br&gt; text</p>'


def test_safe_text_is_not_escaped():
    html = str(tags.P(Safe('Text <br> text')))
    assert html == '<p>Text <br> text</p>'
