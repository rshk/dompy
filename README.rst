DOMpy
#####

Document Object Model, in Python.

.. image:: https://img.shields.io/travis/rshk/dompy/master.svg
    :target: https://travis-ci.org/rshk/dompy

.. image:: https://img.shields.io/pypi/v/dompy.svg
    :target: https://pypi.python.org/pypi/dompy

.. image:: https://img.shields.io/pypi/l/dompy.svg
    :target: https://pypi.python.org/pypi/dompy

.. image:: https://img.shields.io/pypi/status/dompy.svg
    :target: https://pypi.python.org/pypi/dompy

.. image:: https://img.shields.io/pypi/pyversions/dompy.svg
    :target: https://pypi.python.org/pypi/dompy


Abstract
========

Most web "template engines" handle HTML generation as text; this has
some drawbacks, especially about flexibility, readability and
performance.

Dompy aims to take a different approach to solving the problem of
generating HTML programmatically, by exposing a DOM-like API that can
be used to build the page structure, and then render to HTML.


Example
=======

.. code-block:: python

    from dompy import tags

    mypage = tags.Html()

    page_head = tags.Head()
    page_head.append(tags.Title().text('Hello, World!'))
    mypage.append(page_head)

    page_body = tags.Body()
    page_body.append(tags.H1().text('Hello, World!'))
    mypage.append(page_body)

    output = str(mypage)

Of course, the idea there is to have different functions generate
parts of the template, and then combine the results together:

.. code-block:: python

    from dompy import tags

    def make_page():
        head = tags.Head().append(*make_head())
        body = tags.Body().append(*make_body())
        return tags.Html().append(head, body)

    def make_head():
        yield tags.Title().text('Hello, World!')
        yield tags.Link({'rel': 'stylesheet', 'href': 'style.css'})

    def make_body():
        yield tags.H1().text('Hello, World!')
        yield tags.P().text('This is a paragraph of text')

    output = str(make_page())

Now, output looks something like this (indentation added for clarity):

.. code-block:: html

    <html>
        <head>
            <title>Hello, World!</title>
            <link href="style.css" rel="stylesheet">
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is a paragraph of text</p>
        </body>
    </html>
