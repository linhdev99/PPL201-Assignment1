import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

    def test_illegal_escape_2(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\t def"  ""","""abc\\t def,<EOF>""",108))

    def test_comment_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** comment * """, "Unterminated Comment",109))

    def test_comment_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** comment 2 """, "Unterminated Comment",110))

    def test_comment_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** comment ** """, "<EOF>",111))

    def test_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("""id1 id2 iD3 iDi4""", "id1,id2,iD3,iDi4,<EOF>", 112))

    def test_id_2(self):
        self.assertTrue(TestLexer.checkLexeme("""ID1""","Error Token I",113))

    def test_id_3(self):
        self.assertTrue(TestLexer.checkLexeme("_ID1","Error Token _",114))

    def test_id_4(self):
        self.assertTrue(TestLexer.checkLexeme("s_UID","s_UID,<EOF>",115))

    def test_id_5(self):
        self.assertTrue(TestLexer.checkLexeme("s_Uid_1T","s_Uid_1T,<EOF>",116))

    def test_keyword_1(self):
        self.assertTrue(TestLexer.checkLexeme(r"""If ElseIf Else Then EndIf
        Function Parameter Body EndBody For EndFor Do EndDo While EndWhile
        Return Break Continue True False Var""","If,ElseIf,Else,Then,EndIf,Function,Parameter,Body,EndBody,For,EndFor,Do,EndDo,While,EndWhile,Return,Break,Continue,True,False,Var,<EOF>",117))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme(r"""IF ELSEIF ELSE THEN ENDIF
        FUNCTION PARAMETER BODY ENDBODY FOR ENDFOR DO ENDDO WHILE ENDWHILE
        RETURN BREAK CONTINUE TRUE FALSE VAR""","Error Token I",118))

    def test_specific_char_1(self):
        self.assertTrue(TestLexer.checkLexeme(r"""+ +. - -.
* *. \ \.
% ! && ||
== != < >
<= >= =/= <.
>. <=. >=.""","+,+.,-,-.,*,*.,\,\.,%,!,&&,||,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>",119))

    def test_specific_char_2(self):
        self.assertTrue(TestLexer.checkLexeme("() [] : . , ; {}","(,),[,],:,.,,,;,{,},<EOF>",120))

    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""12.0e3
12e3
12e5
0.e12
12.8E+3
1200.
12000e-1
123.3
0e1
1.3232
123213.132123
0.0123123
11E-312312
3123.
1200e0
9871.e-4
213123.
23123.
123.01""",
            "12.0e3,12e3,12e5,0.e12,12.8E+3,1200.,12000e-1,123.3,0e1,1.3232,123213.132123,0.0123123,11E-312312,3123.,1200e0,9871.e-4,213123.,23123.,123.01,<EOF>",
            121))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Hello, I'"m from Dong Thap!\n I'"m a student >.<! ^^"
""",
            r"""Hello, I'"m from Dong Thap!\n I'"m a student >.<! ^^,<EOF>""",
            122))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Hello, I'"m from Dong Thap!\n I'"m a student >.<! ^^"
""",
            r"""Hello, I'"m from Dong Thap!\n I'"m a student >.<! ^^,<EOF>""",
            122))

    def test_id_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
as23123 a_123 a23_322 a_____ 23a_sds 1.03sade23
""",
            r"""as23123,a_123,a23_322,a_____,23,a_sds,1.03,sade23,<EOF>""",
            123))

    def test_arr_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a[323] a[foo()] a[b[1]] a[i] a[1][1][c1]
""",
            r"""a,[,323,],a,[,foo,(,),],a,[,b,[,1,],],a,[,i,],a,[,1,],[,1,],[,c1,],<EOF>""",
            124))

    def test_arr_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a[3] = {1,2,3};
a[2][2] = {{1,2},{3,4}};
Var: a[5];
""",
            r"""a,[,3,],=,{,1,,,2,,,3,},;,a,[,2,],[,2,],=,{,{,1,,,2,},,,{,3,,,4,},},;,Var,:,a,[,5,],;,<EOF>""",
            125))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r""" "New line
             """,
            """Unclosed String: New line""",
            126))

    def test_escape_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" hello world \t "     asdf 
""",

            r' hello world \t ,asdf,<EOF>',
            127
        ))

    def test_escape_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"bbbb  \b"
""",

            r'bbbb  \b,<EOF>',
            128
        ))

    def test_escape_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"aaa   \f"
""",

            r'aaa   \f,<EOF>',
            129
        ))

    def test_escape_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            130
        ))

    def test_escape_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            131
        ))

    def test_escape_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            132
        ))

    def test_illegal_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            133
        ))

    def test_illegal_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
illegal: "\a"
""",

            r'''illegal,:,Illegal Escape In String: \a''',
            134
        ))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc ' xyz "
""",

            "Unclosed String:  abc ",
            134
        ))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \' xyz "
""",

            r" abc \' xyz ,<EOF>",
            135
        ))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc '" xyz " ghi
""",

            r""" abc '" xyz ,ghi,<EOF>""",
            136
        ))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc" 123 x__123 "abc xyz"
" abc\m "
""",

            "abc,123,x__123,abc xyz,Illegal Escape In String:  abc\m",
            137
        ))

    def test_err_tok_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            !== != & ^ % $ # ... \
            """,
            "!=,=,!=,Error Token &",
            138
        ))

    def test_err_tok_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"If a & b Then",
            "If,a,Error Token &",
            139
        ))

    def test_err_tok_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"If a && b Then a = x ^ 2;",
            "If,a,&&,b,Then,a,=,x,Error Token ^",
            140
        ))

    def test_err_tok_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"#value 10",
            "Error Token #",
            141
        ))

    def test_num_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"1234 0000001234 00000431230",
            "1234,0,0,0,0,0,0,1234,0,0,0,0,0,431230,<EOF>",
            142
        ))

    def test_num_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "0,0,0,0,1.1111000000,0e-4,0,0,0,0,0,0,0,0,1e-40000,<EOF>",
            143
        ))

    def test_44_illegal(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            144
        ))

    def test_45_illegal(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            145
        ))

    def test_exp_1(self):
        self.assertTrue(TestLexer.checkLexeme("x = x+y-z*y\\f-t1 && 123123;","x,=,x,+,y,-,z,*,y,\,f,-,t1,&&,123123,;,<EOF>",131))
