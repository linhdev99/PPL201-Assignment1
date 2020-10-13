import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_1(self):
        input = r"""int a, b, c;"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,201))
    def test_2(self):
        input = r"""
int a, b, c;
int foo(int a; float c, d)
{
    int e;
    e = a + 4;
    return foo(e);
}
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,202))
    def test_3(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e;
    e = a + 4;
    f = 1.2;
    return foo(f);
}
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,203))
    def test_4(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    e = a + 4;
    f = 1.2;
    return foo(e);
}
float goo()
{
    float f;
    f = 1.1e3;
    return f;
}
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,204))
    def test_5(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    e = a + 4;
    f = 1.2;
    return foo(f,e,1.2);
}
float goo()
{
    float f;
    f = 1.1e3;
    return f;
}
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,205))
    def test_6(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    e = a + 4;
    f = 1.2;
    return foo(f,e,1.2);
"""
        expect = r"""Error on line 9 col 0: <EOF>"""
        self.assertTrue(TestParser.checkParser(input,expect,206))
    def test_7(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    e = a + 4;
    f = 1.2;
    return foo(f,e,1.2)
}
"""
        expect = r"""Error on line 9 col 0: }"""
        self.assertTrue(TestParser.checkParser(input,expect,207))
    def test_8(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    e = + 4;
    f = 1.2;
    return foo(f,e,1.2);
}
"""
        expect = r"""Error on line 6 col 8: +"""
        self.assertTrue(TestParser.checkParser(input,expect,208))
    def test_9(self):
        input = r"""
int a, b, c;
float foo(int a; float c, d)
{
    int e, f;
    f = 1.2;
    e = f + 4;
    return foo(f,e,1.2);
}
"""
        expect = r"""successful"""
        self.assertTrue(TestParser.checkParser(input,expect,209))
    def test_10(self):
        input = r"""
int a, b, c;
float foo(int a, float c, d)
{
    int e, f;
    f = 1.2;
    e = f + 4;
    return foo(f,e,1.2);
}
"""
        expect = r"""Error on line 3 col 17: float"""
        self.assertTrue(TestParser.checkParser(input,expect,210))
#     def test_simple_program(self):
#         """Simple program: int main() {} """
#         input = r"""
# Var: y;
# """
#         expect = r"""successful"""
#         self.assertTrue(TestParser.checkParser(input,expect,201))
#
#     def test_1_wrong_var_decl(self):
#         """Miss variable"""
#         input = r"""
# Var: ;
# """
#         expect = r"""Error on line 2 col 5: ;"""
#         self.assertTrue(TestParser.checkParser(input,expect,202))
#
#     def test_2_wrong_var_decl(self):
#         """Miss variable"""
#         input = r"""
# Var: x =
# """
#         expect = r"""Error on line 3 col 0: <EOF>"""
#         self.assertTrue(TestParser.checkParser(input,expect,203))
