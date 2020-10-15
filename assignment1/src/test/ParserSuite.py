import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_function_successful_1(self):
        input = r"""Function: foo
Parameter: x,y[5]
Body:
    Var: x = 5;
    x[5] = {1,2,3,4,x};
Endbody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))
