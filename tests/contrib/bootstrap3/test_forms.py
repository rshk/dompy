from dompy.contrib.bootstrap3.forms import form


class Test_form(object):

    def test_form_simple(self):
        assert str(form()) == '<form></form>'

    def test_form_simple_with_content(self):
        assert str(form('FOO')) == '<form>FOO</form>'

    def test_form_inline(self):
        html = str(form(inline=True))
        assert html == '<form class="form-inline"></form>'

    def test_form_horizontal(self):
        html = str(form(horizontal=True))
        assert html == '<form class="form-horizontal"></form>'
