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
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_6_successfull(self):
        input = r"""Var: x;
Var: y = 1;
Var: z[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_7_successfull(self):
        input = r"""Var: x, a;
Var: y = 1, b;
Var: z[5], c = z[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_8_successfull(self):
        input = r"""Var: x, a;
Var: y = 1, b[3] = {1,2,3};
Var: z[5], c = z[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_9_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1, b[3] = {1,2,3};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_10_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1 + 2, b[3] = {1,2,3};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh", sName = "Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_11_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1 + 2, b[3] = {1,2,3};
Var: s[3] = {1+2,x+y\b[1],123*x};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh", sName = "Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_12_successfull(self):
        input = r"""Var: x[2][3] = {{1,2},{2,3,4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_13_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_14_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_15_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3+.1.-.2.3*.y};
Var: x[1][1] = {{1.2+.2e3},{12e-4*.12.9e-3}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_16_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4];
    Body:
        x = 10;
        Var: a = x + 1;
        y = x \. a +. 1.2e3 - 15. *. 10.10e10 *. -9.9e-1;
        f[3][4] = {{1,2,3},{3+y,x+a,x+y}};
        x = f[1-foo2(2*f[2][2])][1+foo()] + 1;
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_17_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4];
    Body:
        x = 10;
        Var: a = x + 1;
        y = x \. a +. 1.2e3 - 15. *. 10.10e10 *. -9.9e-1;
        f[3][4] = {{1,2,3},{3+y,x+a,x+y}};
        x = f[1-foo2(2*f[2][2])][1+foo()] + 1;
        Var: test[10][10][10][10][10];
        test[x][y][z[1][1][(x+y)*a]][f[1][2]][a] = {{x*f},{f[1][4]-(f[1][1]+a)},{x},{y},{f[2][3]}};
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_18_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4];
    Body:
        x = !(y && z[1]);
        f[1][1] = !(x || y) && z[1];
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_19_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4], a, b;
    Body:
        a = True;
        b = False;
        x = !(y && z[1]);
        f[1][1] = !x || !(y && z[a&&b]);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_20_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4], a, b;
    Body:
        Var: c = False;
        a = True;
        b = a && (c || False);
        x = !(y && z[1]);
        f[1][1] = !x || !(y && z[a&&b]);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
