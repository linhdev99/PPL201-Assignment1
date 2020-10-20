import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_function_successful_1(self):
        input = r"""Function: foo
Parameter: x,y[5]
Body:
    Var: x = 5;
    x[5] = {1,2,3,4,x};
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

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
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_5_successfull(self):
        input = r"""Var: x[1][2] = {{1},{1,2}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_6_successfull(self):
        input = r"""Var: x;
Var: y = 1;
Var: z[5];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_7_successfull(self):
        input = r"""Var: x, a;
Var: y = 1, b;
Var: z[5], c = z[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_8_successfull(self):
        input = r"""Var: x, a;
Var: y = 1, b[3] = {1,2,3};
Var: z[5], c = z[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_9_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1, b[3] = {1,2,3};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_10_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1 + 2, b[3] = {1,2,3};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh", sName = "Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_11_successfull(self):
        input = r"""Var: x, a, id = 1710165;
Var: y = 1 + 2, b[3] = {1,2,3};
Var: s[3] = {1+2,x+y\b[1],123*x};
Var: z[5], c = z[1];
Var: sName = "Huynh Pham Phuoc Linh", sName = "Linh";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_12_successfull(self):
        input = r"""Var: x[2][3] = {{1,2},{2,3,4}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_13_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_14_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_15_successfull(self):
        input = r"""Var: x[2] = {1+2*3,4.5\.1.1e3+.1.-.2.3*.y};
Var: x[1][1] = {{1.2+.2e3},{12e-4*.12.9e-3}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

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
        self.assertTrue(TestParser.checkParser(input, expect, 216))

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
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_18_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4];
    Body:
        x = !(y && z[1]);
        f[1][1] = !(x || y) && z[1];
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_19_successfull(self):
        input = r"""Var: x, y, z[3], f[3][4], a, b;
    Body:
        a = True;
        b = False;
        x = !(y && z[1]);
        f[1][1] = !x || !(y && z[a&&b]);
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

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
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_21_successfull(self):
        input = r"""Function: foo
Parameter: x
Body:
    Var: a,b,c[10];
        Body:
            a = 3 + doSomething();
            b = 0x44AF99 + a * 0xA23CD - 0o2123 + e[3] - !(True && a);
            c[3] = {1.2, 10e9, 10.10e-10 *. 132. + 11.1e+5 \. 2e10};
            Var: v, r = 10., h = 5.e1, fls = False;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
    If (x%2==0) Then
        Return x * foo(x-1);
    Else
        Return int_to_float(a*(b-x)) +. c[3];
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_22_successfull(self):
        input = r"""Function: foo
Parameter: x
Body:
    Var: a,b,c[10];
        Body:
            a = 3 + doSomething();
            b = 0x44AF99 + a * 0xA23CD - 0o2123 + e[3] - !(True && a);
            c[3] = {1.2, 10e9, 10.10e-10 *. 132. + 11.1e+5 \. 2e10};
            Var: v, r = 10., h = 5.e1, fls = False;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody.
    If (x%2==0) Then
        Return x * foo(x-1);
    Else
        Return int_to_float(a*(b-x)) +. c[3];
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_23_successfull(self):
        input = r"""Function: foo
Parameter: x
Body:
    Var: a,b[2][3],c;
        Body:
            a = 0;
            b[2][3] = {{1,2,3},{4,5}};
            c = "";
        EndBody.
    If x < 1 Then
        Return x + b[0][0];
    Else
        For (i = a, i < 10, 2) Do
            c = c + int_to_string(x) + ": Value " + int_to_string(i) + "\n";
        EndFor.
        print(c);
        Return foo(x-1);
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_24_successfull(self):
        input = r"""Function: foo
Parameter: x
Body:
    Var: a,b[2][3],c;
        Body:
            a = 0;
            b[2][3] = {{1,2,3},{4,5}};
            c = "";
        EndBody.
    If x < 1 Then
        Return x + b[0][0];
    ElseIf (x > 1) && (x < 5) Then
        For (i = a, i < 20, 1) Do
            If i % 2 == 0 Then
                c = "Test If, For statement";
                **Test thoi, lam gi cang :v**
                print(c);
            EndIf.
            Return foo(x-1);
        EndFor.
    Else
        For (i = a, i < 10, 2) Do
            c = c + int_to_string(x) + ": Value " + int_to_string(i) + "\n";
        EndFor.
        print(c);
        Return foo(x-1);
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_25_successfull(self):
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
        For (i = 0, i < 20, 1) Do
            If i % 2 == 0 Then
                print(fact(i));
            Else
                print("i % 2 != 0\n");
            EndIf.
            Var: i = 0;
            While i < 10 Do
                For (i = 0, i < 20, 1) Do
                    If i > 10 Then
                        val = fact(i * 2);
                        print(int_to_string(val) + "\n");
                    ElseIf (i > 5) && (i <= 10) Then
                        val = fact(i);
                        print(int_to_string(val) + "\n");
                    Else
                        print("Next --> \n");
                    EndIf.
                EndFor.
            EndWhile.
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_26_successfull(self):
        input = r"""Var: x;
Function: main
    Body:
        For (i = 0, i < 20, 1) Do
            If i % 2 == 0 Then
                print(fact(i));
            Else
                print("i % 2 != 0\n");
            EndIf.
            Var: i = 0;
            While i < 10 Do
                For (i = 0, i < 20, 1) Do
                    If i > 10 Then
                        val = fact(i * 2);
                        print(int_to_string(val) + "\n");
                    ElseIf (i > 5) && (i <= 10) Then
                        sName = "Phuoc Linh";
                        Continue;
                        sID = 1710165;
                    Else
                        val = fact(i);
                        print(int_to_string(val) + "\n");
                    EndIf.
                EndFor.
            EndWhile.
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_27_successfull(self):
        input = r"""Var: a,b,c,x,y,z,sID,sName;
Function: main
    Body:
        x = 1000000.;
        a = 0;
        Do
            a = a + 1;
            x = x \. int_to_float(a);
            c = float_to_int(x) % 5;
            Var: xx, yy = 0;
            If (c > 3) || (c <= 1) Then
                xx = x + y \ z;
            Else
                xx = x - y \ z;
            EndIf.
        While x < 1 EndDo.
        Var: yy = True;
        If yy Then
            While yy Do
                Do
                    For (i = 0, i < 10, 1) Do
                        While yy Do
                            If yy Then
                                If yy Then
                                    If !yy Then
                                        print("Dong nay khong bao gio duoc in!");
                                        Break;
                                    Else
                                        sID = 1710165.4;
                                        sName = "Phuoc Linh";
                                        yy = False;
                                        Continue;
                                    EndIf.
                                EndIf.
                            EndIf.
                        EndWhile.
                    EndFor.
                While yy EndDo.
            EndWhile.
        Else
            x = x \. y;
            Continue;
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_28_successfull(self):
        input = r"""Var: a,b,c,x,y,z,sID,sName;
Function: main
    Body:
        If bool_of_string ("True") Then
            a = int_of_string (read ());
            b = float_of_int (a) +. 2.0;
        Else
            a = x * y;
            b = x + y;
            z = pow(a,b);
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_29_successfull(self):
        input = r"""Var: a[10],b,c,x,y,z,sID,sName;
Function: main
    Body:
        a[3 + foo(2)] = a[b[2][3]] + 4;
        If bool_of_string ("True") Then
            a = int_of_string (read ());
            b = float_of_int (a) +. 2.0;
            While a > b Do
                For (i = 0, i < z+y, 1) Do
                    a[5] = {1,2,3,4,5};
                    str = "Hello, I'"m Linh";
                    f = 0x0ABCFF; f1 = 0o01234567;
                    Do
                        something();
                    While bool_of_string("HIHI") EndDo.
                EndFor.
            EndWhile.
        Else
            a = x * y;
            b = x + y;
            z = pow(a,b);
        EndIf.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_30_successfull(self):
        input = r"""Var: a[10],b[5][5],c,x,y,z,sID,sName;
Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
Function: main
    Body:
        c = True;
        d = False;
        e = c && d;
        f = !e;
        For (i = 100, i < b[1][1], -1) Do
            While c Do
                Do
                    Do
                        While !d Do
                            While !d Do
                                Do
                                    If !e Then
                                        d = True;
                                        c = False;
                                    ElseIf x < 1 Then
                                        d = !d;
                                        c = c && True;
                                        c = False;
                                    Else
                                        c = False;
                                    EndIf.
                                While !d EndDo.
                            EndWhile.
                        EndWhile.
                    While !d EndDo.
                While !d EndDo.
            EndWhile.
        EndFor.
    EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_31_successfull(self):
        input = r"""Function: increase
Parameter: x
Body:
    Return x+1;
EndBody.
Function: square
Parameter: x
Body:
    Return x*x;
EndBody.
Function: pow
Parameter: x, y
Body:
    Var: result = 1;
    For (i = 0, i < y, 1) Do
        result = result * x;
    EndFor.
    Return result;
EndBody.
Function: main
Body:
    Var: x;
    x = increase(5);
    x = square(x);
    x = pow(x, 5);
    print("Result = ");
    print(x);
    Return;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_32_successfull(self):
        input = r"""Var: x1, x2, x3, y[3];
Body:
    x1 = 2131;
    x2 = 0X123ABF;
    x3 = 0O12323;
    y[3] = {0.2,0.1e4,-23.43};
EndBody.
Function: increase
Parameter: x
Body:
    Return x+1;
EndBody.
Function: square
Parameter: x
Body:
    Return x*x;
EndBody.
Function: pow
Parameter: x, y
Body:
    Var: result = 1;
    For (i = 0, i < y, 1) Do
        result = result * x;
    EndFor.
    Return result;
EndBody.
Function: main
Body:
    Var: x;
    x = increase(5);
    x = square(x);
    x = pow(x, 5);
    print("Result = ");
    print(x);
    If x < y Then
        x = 5.4;
    Else
        y = 5.e-5;
    EndIf.
    Return;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_33_successfull(self):
        input = r"""Var: x1, x2, x3, y[3];
Body:
    x1 = 2131;
    x2 = 0X123ABF;
    x3 = 0O12323;
    y[3] = {0.2,0.1e4,-23.43};
EndBody.
** Test comment o giua **
** Test comment o giua **
** Test comment o giua **
Function: increase
Parameter: x
Body:
    Return x+1;
EndBody.
**
* Test comment o giua *
* Test comment o giua *
* Test comment o giua *
**
Function: square
Parameter: x
Body:
    Return x*x;
EndBody.
Function: pow
Parameter: x, y
Body:
    Var: result = 1;
    For (i = 0, i < y, 1) Do ** Test o day **
        result = result * x;
        ** khong co gi **
    EndFor.
    **
        * Test comment o giua *
        * Test comment o giua *
        * Test comment o giua *
    **
    Return result;
EndBody.
Function: main
Body:
    Var: x;
    x = increase(5);
    x = square(x);
    **
        * Test comment o giua *
        * Test comment o giua *
        * Test comment o giua *
    **
    x = pow(x, 5);
    print("Result = ");
    print(x);
    If x < y Then
        x = 5.4;
    Else
        y = 5.e-5;
    EndIf.
    Return;
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_34_successfull(self):
        input = r"""Function: main
Body:
    str = **cai nay khong phai string** "Value \n";
    num = **cai nay khongo phai num** 10E-5;
    value = foo(str, num, string_to_float(str) + num **Test Parser thoi**, **Test cho nay** str + float_to_string(num));
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_35_successfull(self):
        input = r"""Function: main
Body:
    str = **cai nay khong phai string** "Value \n";
    num = **cai nay khongo phai num** 10E-5;
    value = foo(str, num, string_to_float(str) + num **Test Parser thoi**, **Test cho nay** str + float_to_string(num));
    If num > 100. Then 
        **True: num > 100 ???**
    ElseIf num > 35 Then
        **???$$#!@$)#(!)@(*#(!)@*)%#*$@#$489878934234-*4234(*&(*&#%*%!@^#^!@#^@#**
    Else
        val = "\n\b\t\f\\" **adasd???**;
        **
        * line 1 *
        * line 2 *
        **
    EndIf.
EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_99_successfull(self):
        input = r""""""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_100_successfull(self):
        input = r""""""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 300))
