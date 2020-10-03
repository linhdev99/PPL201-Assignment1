# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\4\3\4\5\4\24\n\4\3\5\3\5\3\5\3\5\3\5\6\5")
        buf.write("\33\n\5\r\5\16\5\34\5\5\37\n\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\2\2\7\2\4")
        buf.write("\6\b\n\2\3\3\2?@\2/\2\f\3\2\2\2\4\17\3\2\2\2\6\23\3\2")
        buf.write("\2\2\b\25\3\2\2\2\n\"\3\2\2\2\f\r\5\4\3\2\r\16\7\2\2\3")
        buf.write("\16\3\3\2\2\2\17\20\5\6\4\2\20\5\3\2\2\2\21\24\5\b\5\2")
        buf.write("\22\24\5\n\6\2\23\21\3\2\2\2\23\22\3\2\2\2\23\24\3\2\2")
        buf.write("\2\24\7\3\2\2\2\25\26\7\33\2\2\26\27\7\b\2\2\27\36\7>")
        buf.write("\2\2\30\32\7\61\2\2\31\33\t\2\2\2\32\31\3\2\2\2\33\34")
        buf.write("\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36")
        buf.write("\30\3\2\2\2\36\37\3\2\2\2\37 \3\2\2\2 !\7\7\2\2!\t\3\2")
        buf.write("\2\2\"#\7\33\2\2#$\7\b\2\2$%\7>\2\2%&\7\3\2\2&\'\7?\2")
        buf.write("\2\'(\7\4\2\2()\3\2\2\2)*\7\61\2\2*+\7\5\2\2+,\7?\2\2")
        buf.write(",-\7\6\2\2-.\3\2\2\2./\7\7\2\2/\13\3\2\2\2\5\23\34\36")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'{'", "'}'", "';'", "':'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'!'", "'&&'", "'||'", "<INVALID>", "'+'", 
                     "'-'", "'*'", "'\\'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "<INVALID>", "<INVALID>", "'<'", "<INVALID>", 
                     "'>'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SEMI", "COLON", "WS", "BCMT", "BODY", 
                      "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", "ENDBODY", 
                      "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                      "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", 
                      "TRUE", "FALSE", "ENDDO", "OPERATOR", "BOOL_OPERATOR", 
                      "NOT", "AND", "OR", "ARITHMETIC_OPERATOR", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", 
                      "DIVDOT", "RELATIONAL_OPERATOR", "RELATIONAL_OPERATOR_INT", 
                      "EQ", "EQINT", "NEQINT", "LTINT", "LTEINT", "GTINT", 
                      "GTEINT", "RELATIONAL_OPERATOR_FLOAT", "NEQF", "LTF", 
                      "LTEF", "GTF", "GTEF", "ID", "INT", "FLOAT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_main = 1
    RULE_var_declare = 2
    RULE_var_normal = 3
    RULE_var_array = 4

    ruleNames =  [ "program", "main", "var_declare", "var_normal", "var_array" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    SEMI=5
    COLON=6
    WS=7
    BCMT=8
    BODY=9
    BREAK=10
    CONTINUE=11
    DO=12
    ELSE=13
    ELSEIF=14
    ENDBODY=15
    ENDIF=16
    ENDFOR=17
    ENDWHILE=18
    FOR=19
    FUNCTION=20
    IF=21
    PARAMETER=22
    RETURN=23
    THEN=24
    VAR=25
    WHILE=26
    TRUE=27
    FALSE=28
    ENDDO=29
    OPERATOR=30
    BOOL_OPERATOR=31
    NOT=32
    AND=33
    OR=34
    ARITHMETIC_OPERATOR=35
    ADD=36
    SUB=37
    MUL=38
    DIV=39
    MOD=40
    ADDDOT=41
    SUBDOT=42
    MULDOT=43
    DIVDOT=44
    RELATIONAL_OPERATOR=45
    RELATIONAL_OPERATOR_INT=46
    EQ=47
    EQINT=48
    NEQINT=49
    LTINT=50
    LTEINT=51
    GTINT=52
    GTEINT=53
    RELATIONAL_OPERATOR_FLOAT=54
    NEQF=55
    LTF=56
    LTEF=57
    GTF=58
    GTEF=59
    ID=60
    INT=61
    FLOAT=62
    ERROR_CHAR=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    UNTERMINATED_COMMENT=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main(self):
            return self.getTypedRuleContext(BKITParser.MainContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.main()
            self.state = 11
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare(self):
            return self.getTypedRuleContext(BKITParser.Var_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_main

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain" ):
                return visitor.visitMain(self)
            else:
                return visitor.visitChildren(self)




    def main(self):

        localctx = BKITParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.var_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_normal(self):
            return self.getTypedRuleContext(BKITParser.Var_normalContext,0)


        def var_array(self):
            return self.getTypedRuleContext(BKITParser.Var_arrayContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = BKITParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 15
                self.var_normal()

            elif la_ == 2:
                self.state = 16
                self.var_array()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_normalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT)
            else:
                return self.getToken(BKITParser.INT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.FLOAT)
            else:
                return self.getToken(BKITParser.FLOAT, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_normal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal" ):
                return visitor.visitVar_normal(self)
            else:
                return visitor.visitChildren(self)




    def var_normal(self):

        localctx = BKITParser.Var_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(BKITParser.VAR)
            self.state = 20
            self.match(BKITParser.COLON)
            self.state = 21
            self.match(BKITParser.ID)
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 22
                self.match(BKITParser.EQ)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 23
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.INT or _la==BKITParser.FLOAT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 26 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BKITParser.INT or _la==BKITParser.FLOAT):
                        break



            self.state = 30
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_arrayContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT)
            else:
                return self.getToken(BKITParser.INT, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_array" ):
                return visitor.visitVar_array(self)
            else:
                return visitor.visitChildren(self)




    def var_array(self):

        localctx = BKITParser.Var_arrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_array)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(BKITParser.VAR)
            self.state = 33
            self.match(BKITParser.COLON)
            self.state = 34
            self.match(BKITParser.ID)

            self.state = 35
            self.match(BKITParser.T__0)
            self.state = 36
            self.match(BKITParser.INT)
            self.state = 37
            self.match(BKITParser.T__1)
            self.state = 39
            self.match(BKITParser.EQ)

            self.state = 40
            self.match(BKITParser.T__2)
            self.state = 41
            self.match(BKITParser.INT)
            self.state = 42
            self.match(BKITParser.T__3)
            self.state = 44
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





