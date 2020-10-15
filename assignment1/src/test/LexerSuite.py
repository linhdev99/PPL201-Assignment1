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
        self.assertTrue(TestLexer.checkLexeme("If ElseIf Else Then EndIf","If,ElseIf,Else,Then,EndIf,<EOF>",117))

    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme(r"""12.0e3
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
123.01""","12.0e3,12e3,12e5,0.e12,12.8E+3,1200.,12000e-1,123.3,0e1,1.3232,123213.132123,0.0123123,11E-312312,3123.,1200e0,9871.e-4,213123.,23123.,123.01,<EOF>",121))
