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
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_4_successfull(self):
        input = r"""Var: x;
Function: fact
    Parameter: n
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * fact(n-1);
        EndIf.
    EndBody.

Function: main
    Body:
        x = 10;
        fact(x);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_5_successfull(self):
        input = r"""Var: x[1][2] = {{1},{1,2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
