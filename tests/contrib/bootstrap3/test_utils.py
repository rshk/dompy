import pytest

from dompy.contrib.bootstrap3.utils import make_column_classes


class Test_make_column_classes(object):

    def test_col_xs_10(self):
        assert make_column_classes(xs=10) == ['col-xs-10']

    def test_col_xs_10_sm_5(self):
        assert make_column_classes(xs=10, sm=5) == ['col-xs-10', 'col-sm-5']

    def test_col_md_4_md_offset_2(self):
        classes = make_column_classes(md=4, md_offset=2)
        assert classes == ['col-md-4', 'col-md-offset-2']

    def test_col_md_4_md_offset_0(self):
        classes = make_column_classes(md=4, md_offset=0)
        assert classes == ['col-md-4', 'col-md-offset-0']

    def test_none_value_is_skipped(self):
        assert make_column_classes(xs=None, sm=None) == []

    def test_invalid_kwarg_raises_typeerror(self):
        with pytest.raises(TypeError):
            make_column_classes(INVALID_KWARG='SOMETHING')
