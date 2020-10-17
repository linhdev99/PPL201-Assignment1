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

            r"Illegal Escape In String:  Hi Hi \m",
            133
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

            r"abc,123,x__123,abc xyz,Illegal Escape In String:  abc\m",
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
"abc \ xyzhg r324f sd12.34532sad.343"
""",

            r"abc - xyz,Illegal Escape In String: abc \ ",
            144
        ))

    def test_45_illegal(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yasdasdasdasdasd d2 \\d ayz"
""",

            r"abc - xyz,Illegal Escape In String: abc \y",
            145
        ))

    def test_46_esc(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"asdasd \\ xasdasdyz"
""",

            r"""asdasd \\ xasdasdyz,<EOF>""",
            146
        ))

    def test_47_esc(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'"\\value\\value\\empty\\??\\haha\n\t\b\f"',
            r"\\value\\value\\empty\\??\\haha\n\t\b\f,<EOF>",
            147
        ))

    def test_48_uncloseStr(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'"string ne, string nua ne\' ',
            r"Unclosed String: string ne, string nua ne\' ",
            148
        ))

    def test_49_exp(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"b[1+2] + int(3) + float_to_int(5.1) - 2 * 3 - 5 + 4 + f[a || b] % 2",
            r"b,[,1,+,2,],+,int,(,3,),+,float_to_int,(,5.1,),-,2,*,3,-,5,+,4,+,f,[,a,||,b,],%,2,<EOF>",
            149
        ))

    def test_50_exp(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"1.2 +. 3.e5 *. 1e5 \. xyz -. foo(3.1) *. int_to_float(213123)",
            r"1.2,+.,3.e5,*.,1e5,\.,xyz,-.,foo,(,3.1,),*.,int_to_float,(,213123,),<EOF>",
            150
        ))

    def test_51_exp(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"x = x+y-z*y\f-t1 && 123123;",
            r"x,=,x,+,y,-,z,*,y,\,f,-,t1,&&,123123,;,<EOF>",
            151
        ))

    def test_52(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Var: x, y, z[3];
Body:
    x = 5;
    y = 1.2e3;
    
    z[3] = {1,2,3};
EndBody.
            """,
            r"Var,:,x,,,y,,,z,[,3,],;,Body,:,x,=,5,;,y,=,1.2e3,;,z,[,3,],=,{,1,,,2,,,3,},;,EndBody,.,<EOF>",
            152
        ))

    def test_53_complex(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Body:
        x = 10;
        ok();
    EndBody.
            """,
            r"""Function,:,foo,Body,:,x,=,10,;,ok,(,),;,EndBody,.,<EOF>""",
            153
        ))

    def test_54_unclose_str(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
value = "string nay la value;
value2 = "string string string";
            """,
            r"""value,=,Unclosed String: string nay la value;""",
            154
        ))

    def test_55_for(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
For (i = 1, i < 5, 2) Do
    writeln(i);
EndFor.
            """,
            r"""For,(,i,=,1,,,i,<,5,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",
            155
        ))

    def test_56_function(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo2
    Parameter: x
    Body:
        If n == 0 Then
            Return 1;
        Else
            Return n * foo(n-1);
        EndIf.
    EndBody.    
            """,
            r"""Function,:,foo2,Parameter,:,x,Body,:,If,n,==,0,Then,Return,1,;,Else,Return,n,*,foo,(,n,-,1,),;,EndIf,.,EndBody,.,<EOF>""",
            156
        ))

    def test_57_function(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
        x = x + 1;
        str = "str;
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,Unclosed String: str;""",
            157
        ))

    def test_58_function_str(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
        x = x + 1;
        str = "str\n";
        str2 = "sdas\a";
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,str2,=,Illegal Escape In String: sdas\a""",
            158
        ))

    def test_59_function_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
    ** chay thu thoi **
        x = x + 1;
        str = "str\n";
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,EndBody,.,<EOF>""",
            159
        ))

    def test_60_function_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
    ** chay thu thoi **
        x = x + 1;
        str = "str\n";
    ** dong nay loi ne!
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,Unterminated Comment""",
            160
        ))

    def test_61_function_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
    ** chay thu thoi **
        x = x + 1;
        str = "str\n";
    ** --> dong nay loi ne! *
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,Unterminated Comment""",
            161
        ))

    def test_62_function_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
    ** chay thu thoi **
        x = x + 1;
        str = "str\n";
    *** --> xxxxxx! **
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,EndBody,.,<EOF>""",
            162
        ))

    def test_63_function_cmt(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Parameter: x
    Body:
    ** chay thu thoi **
        x = x + 1;
        str = "str\n";
    ** This is a single-line comment. **
    ** This is a
     * multi-line
     * comment.\a\a\a\a\ad\s\ad\asd\qw\eq\we\as\d
     **
    EndBody.  
            """,
            r"""Function,:,foo,Parameter,:,x,Body,:,x,=,x,+,1,;,str,=,str\n,;,EndBody,.,<EOF>""",
            163
        ))

    def test_64_function(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Body:
        a = a[x+y*z] - 5;
    EndBody.
            """,
            r"""Function,:,foo,Body,:,a,=,a,[,x,+,y,*,z,],-,5,;,EndBody,.,<EOF>""",
            164
        ))

    def test_65_function(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Function: foo
    Body
        s = "asdasdasd;fdfeasd\n\t\b";
        q = "\n\t\b\\\\\\";
        w = "qweasd
        
        
        ";
    EndBody.
            """,
            r"""Function,:,foo,Body,s,=,asdasdasd;fdfeasd\n\t\b,;,q,=,\n\t\b\\\\\\,;,w,=,Unclosed String: qweasd""",
            165
        ))

    def test_66_err_tok(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
\\ // / \
            """,
            r"""\,\,Error Token /""",
            166
        ))

    def test_67_err_tok(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
@aa2312
            """,
            r"""Error Token @""",
            167
        ))

    def test_68_err_tok(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
+22\t\t\t\t\t\t\t\t\t
            """,
            r"""+,22,\,t,\,t,\,t,\,t,\,t,\,t,\,t,\,t,\,t,<EOF>""",
            168
        ))

    def test_69_tok(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
+\.\.\.\.\.\.\.\.\.\.\.\.\\\\\
            """,
            r"""+,\.,\.,\.,\.,\.,\.,\.,\.,\.,\.,\.,\.,\,\,\,\,\,<EOF>""",
            169
        ))

    def test_70_tok(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
%%%%%%%%%%%%%
            """,
            r"""%,%,%,%,%,%,%,%,%,%,%,%,%,<EOF>""",
            170
        ))

    def test_71_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
// (,True,[ acb40 % For,),with
= boolean .. p104c ] function do z71ae of < begin if break with of procedure b4169 break - of = = function div
(* <= : a41aa,while,m8bcd .. E8869,,,string*)
Else as If fbm While WhileEnd ... ,,, !!! && ||
""",
            r"""Error Token /""",
            171
        ))

    def test_72_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
\\ (,True,[ acb40 % For,),with
= boolean .. p104c ] function do z71ae of < begin if break with of procedure b4169 break - of = = function div
(* <= : a41aa,while,m8bcd .. 1E8869,,,string*)
Else as If fbm While asd- asd=sad 23 EndWhile ... ,,, !!! && ||
""",
            r"""\,\,(,,,True,,,[,acb40,%,For,,,),,,with,=,boolean,.,.,p104c,],function,do,z71ae,of,<,begin,if,break,with,of,procedure,b4169,break,-,of,=,=,function,div,(,*,<=,:,a41aa,,,while,,,m8bcd,.,.,1E8869,,,,,,,string,*,),Else,as,If,fbm,While,asd,-,asd,=,sad,23,EndWhile,.,.,.,,,,,,,!,!,!,&&,||,<EOF>""",
            172
        ))

    def test_73_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Else df [] f]d[f]f3] dfdf.af.df..f.d.f...fder243df 1.24 1.e23 \. sdasd2
-13s 34 a_sda as23_34 s.
= True False Else If sdm ><.,..12;;;;;::::sdasd"sad" 23.dfsdf +.*. -.+.s
frwes das34 35446fgd 2 fadfsd65f eEES 1E32 
()()()()()()(((()))){}{}{}[][][][{{()}}{) asd=asd=as=d2 && || ****
            """,
            r"""Else,df,[,],f,],d,[,f,],f3,],dfdf,.,af,.,df,.,.,f,.,d,.,f,.,.,.,fder243df,1.24,1.e23,\.,sdasd2,-,13,s,34,a_sda,as23_34,s,.,=,True,False,Else,If,sdm,>,<.,,,.,.,12,;,;,;,;,;,:,:,:,:,sdasd,sad,23.,dfsdf,+.,*.,-.,+.,s,frwes,das34,35446,fgd,2,fadfsd65f,eEES,1E32,(,),(,),(,),(,),(,),(,),(,(,(,(,),),),),{,},{,},{,},[,],[,],[,],[,{,{,(,),},},{,),asd,=,asd,=,as,=,d2,&&,||,<EOF>""",
            173
        ))

    def test_74_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
\\ :,..,<= fef8b \ div,=,continue
return ) then lb1e7 true mod , Ve4b7 , := true do begin or >= >= v8b5e := for <> >= or ) [
(* continue ) p0698,*,Oc0d5 .. c9970,,,downto*)
""",
            r"\,\,:,,,.,.,,,<=,fef8b,\,div,,,=,,,continue,return,),then,lb1e7,true,mod,,,Error Token V",
            174
        ))

    def test_75_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
\. <=,var,> b2bb9 else real,boolean,return 361 <> mf34e,else,osdasd
fe,df dsf ,354, d,f ,45,as d3 4.5432 423.4 32423 12.123e3214 12312.e-321
&& False Then edaa6 integer , break aP278e if <> [ * \. Function While div d74f0 > not <> , ] begin *.
(* ; Continue eeecf,False,a_Hc361 <> mf34e,else,or*)
""",

            r"\.,<=,,,var,,,>,b2bb9,else,real,,,boolean,,,return,361,<,>,mf34e,,,else,,,osdasd,fe,,,df,dsf,,,354,,,d,,,f,,,45,,,as,d3,4.5432,423.4,32423,12.123e3214,12312.e-321,&&,False,Then,edaa6,integer,,,break,aP278e,if,<,>,[,*,\.,Function,While,div,d74f0,>,not,<,>,,,],begin,*.,(,*,;,Continue,eeecf,,,False,,,a_Hc361,<,>,mf34e,,,else,,,or,*,),<EOF>",
            175
        ))

    def test_76_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
\. ],],* ae0bc not mod,Return,,
function < + a_Qefbe and ; of o366c false array else < > and downto for sJ4981 : <> return = for then ..
(* of break h80bb,or,bfa18 ) f_W6bd3,real,<*)
foo() fo(232) f(23.43 + 43 - 2);
            """,
            r"""\.,],,,],,,*,ae0bc,not,mod,,,Return,,,,,function,<,+,a_Qefbe,and,;,of,o366c,false,array,else,<,>,and,downto,for,sJ4981,:,<,>,return,=,for,then,.,.,(,*,of,break,h80bb,,,or,,,bfa18,),f_W6bd3,,,real,,,<,*,),foo,(,),fo,(,232,),f,(,23.43,+,43,-,2,),;,<EOF>""",
            176
        ))

    def test_77_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""Return Break begin,),] lc648 ; not,(,\
, + Var sdCd03e 434 2156 sd. d544;d=- =3-= 04-=0-=fg <>wAD {wDwFPw wEw+wAS;}{>d[ else to do xd695 ( string of ; EndBody : ] .. f5179 >= + + [ = ; <=
(* || : = d3d6a,begin Body ,sIss6a5a not sfCf2e7,\,<=*)""",
            r"""Return,Break,begin,,,),,,],lc648,;,not,,,(,,,\,,,+,Var,sdCd03e,434,2156,sd,.,d544,;,d,=,-,=,3,-,=,0,4,-,=,0,-,=,fg,<,>,wAD,{,wDwFPw,wEw,+,wAS,;,},{,>,d,[,else,to,do,xd695,(,string,of,;,EndBody,:,],.,.,f5179,>=,+,+,[,=,;,<=,(,*,||,:,=,d3d6a,,,begin,Body,,,sIss6a5a,not,sfCf2e7,,,\,,,<=,*,),<EOF>""",
            177
        ))

    def test_78_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""Return Break begin,),] lc648 ; not,(,\
, + Var sdCd03e 434 2156 sd. d544lse to do xd695 ( string of ; EndBody : ] .. f5179 >= + + [ = ; <=
(* || : = d3d6a,begin Body ,sIss6a5a not sfCf2e7,\,<=*)
;d=- =3-= 04-=0-=fn Body ,sIss6a5a not sfCf2g <>wAD {wDwFPw wEw+wAS;}{>d[ e
            """,
            r"""Return,Break,begin,,,),,,],lc648,;,not,,,(,,,\,,,+,Var,sdCd03e,434,2156,sd,.,d544lse,to,do,xd695,(,string,of,;,EndBody,:,],.,.,f5179,>=,+,+,[,=,;,<=,(,*,||,:,=,d3d6a,,,begin,Body,,,sIss6a5a,not,sfCf2e7,,,\,,,<=,*,),;,d,=,-,=,3,-,=,0,4,-,=,0,-,=,fn,Body,,,sIss6a5a,not,sfCf2g,<,>,wAD,{,wDwFPw,wEw,+,wAS,;,},{,>,d,[,e,<EOF>""",
            178
        ))

    def test_79_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
(,While,: sH050f EndIf Return,+,[
848d While sdownto - + , ] ) >= sHdcb8 False \ fo
, \ "\n"  da8d While sdownto - + , ] ) >= sHdcb8 False \ for > not &&&&&& (
s **dasd ** "\t" or || || |||||| a_M3ff3 While \ For y84
(* ( [ bc9ca,],b1ebd ; w28cd,procedure Parameter ,If*)            
            """,
            r"""(,,,While,,,:,sH050f,EndIf,Return,,,+,,,[,848,d,While,sdownto,-,+,,,],),>=,sHdcb8,False,\,fo,,,\,\n,da8d,While,sdownto,-,+,,,],),>=,sHdcb8,False,\,for,>,not,&&,&&,&&,(,s,\t,or,||,||,||,||,||,a_M3ff3,While,\,For,y84,(,*,(,[,bc9ca,,,],,,b1ebd,;,w28cd,,,procedure,Parameter,,,If,*,),<EOF>""",
            179
        ))

    def test_80_auto_gen(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
** // sad ad var,+,erter, Mter tertaf4 , with,=,- **
to >= ( f3451caert : ] to s_Ie94f for ,rt inertert54teger ; , for re4ern If fdBbfd7 + r5e534al <> if do downto :
(* * ) e4686,end,rf588 > dfdR8121,ert Return Var: ** .sd34';, .\ fsdf sdf'3
;df 'dk'4l'; d;f'lad 'fd' dfdsf';l';dfsd,f3 df
dlf;gdkf;lh 
f/41/2/3??? 4/2 3@@34#)$()_($_ 
** sa
fdtt45 <<>>,..>>(;;:)-=+.-.
            """,
            r"""to,>=,(,f3451caert,:,],to,s_Ie94f,for,,,rt,inertert54teger,;,,,for,re4ern,If,fdBbfd7,+,r5e534al,<,>,if,do,downto,:,(,*,*,),e4686,,,end,,,rf588,>,dfdR8121,,,ert,Return,Var,:,sa,fdtt45,<,<,>,>,,,.,.,>,>,(,;,;,:,),-,=,+.,-.,<EOF>""",
            180
        ))

    def test_81_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
sdfp[3dpf vb..,. df,.d,><> d,f4;, ;,df./ asfd 3 ????
            """,
            r"""sdfp,[,3,dpf,vb,.,.,,,.,df,,,.,d,,,>,<,>,d,,,f4,;,,,;,,,df,.,Error Token /""",
            181
        ))

    def test_82_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Var Return ss.34  3p4 <><sdd >>sdw4 <0df- 34- ! sd "\nfdoemc l;wq sda  \t"
            """,
            r"""Var,Return,ss,.,34,3,p4,<,>,<,sdd,>,>,sdw4,<,0,df,-,34,-,!,sd,\nfdoemc l;wq sda  \t,<EOF>""",
            182
        ))

    def test_83_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            "abc "  xyz"
            """,
            r"""abc ,xyz,Unclosed String: """,
            183
        ))

    def test_84_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
            " abc \sd 34<> 42 xyz "
            """,
            r"Illegal Escape In String:  abc \s",
            184
        ))

    def test_85_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"das d2 \n 
            """,
            r"""Unclosed String: das d2 \n """,
            185
        ))

    def test_86_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""" abc \ xyz " 
            """,
            r"Illegal Escape In String:  abc \ ",
            186
        ))

    def test_87_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""  " abc \r  xyz  """,
            r"Unclosed String:  abc \r  xyz  ",
            187
        ))

    def test_88_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
    " abc s w4 \n\r\t\b  xyz
            """,
            r"""Unclosed String:  abc s w4 \n\r\t\b  xyz""",
            188
        ))

    def test_89_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Var: sd;
** =========== Comment here ==============
 * Line 1
 * Line 2
 * Line 3
======================================= **
            """,
            r"""Var,:,sd,;,<EOF>""",
            189
        ))

    def test_90_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
    " abc \t  xyz "
""",

            "Unclosed String:  abc ",
            190
        ))

    def test_91_err(self):
        self.assertTrue(TestLexer.checkLexeme(
            """
    " asdbc \b  234xyz "
""",

            "Unclosed String:  asdbc ",
            191
        ))

    def test_92_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(
            "BodyElseEndForIfVarEndDoDoWhile",
            "Body,Else,EndFor,If,Var,EndDo,Do,While,<EOF>",
            192
        ))

    def test_93_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: x = True;",
            "Var,:,x,=,True,;,<EOF>",
            193
        ))

    def test_94_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: x = TRUE;",
            "Var,:,x,=,Error Token T",
            194
        ))

    def test_95_keywords(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""Var: x = False; y = y +. 1.; "String?" **Comment** """,
            "Var,:,x,=,False,;,y,=,y,+.,1.,;,String?,<EOF>",
            195
        ))
