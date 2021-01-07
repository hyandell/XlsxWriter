###############################################################################
#
# Tests for XlsxWriter.
#
# Copyright (c), 2013-2021, John McNamara, jmcnamara@cpan.org
#

from ..excel_comparison_test import ExcelComparisonTest
from ...workbook import Workbook


class MyStr(str):
    pass


class TestCompareXLSXFiles(ExcelComparisonTest):
    """
    Test file created by XlsxWriter against a file created by Excel.

    """

    def setUp(self):

        self.set_filename('types09.xlsx')

    def test_write_string_subclass(self):
        """Test writing subclasses strings."""

        workbook = Workbook(self.got_filename)
        worksheet = workbook.add_worksheet()

        worksheet.write(0, 0, MyStr('Hello'))

        workbook.close()

        self.assertExcelEqual()
