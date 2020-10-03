# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0249\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\7\7\u00d6\n\7\f\7\16")
        buf.write("\7\u00d9\13\7\3\b\3\b\3\b\3\b\5\b\u00df\n\b\3\b\6\b\u00e2")
        buf.write("\n\b\r\b\16\b\u00e3\3\t\3\t\3\t\3\t\5\t\u00ea\n\t\3\t")
        buf.write("\6\t\u00ed\n\t\r\t\16\t\u00ee\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\5\f\u00f7\n\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\6\17\u0100")
        buf.write("\n\17\r\17\16\17\u0101\3\17\3\17\3\20\3\20\3\20\3\20\7")
        buf.write("\20\u010a\n\20\f\20\16\20\u010d\13\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%")
        buf.write("\3&\3&\3&\5&\u0199\n&\3\'\3\'\3\'\5\'\u019e\n\'\3(\3(")
        buf.write("\3)\3)\3)\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3+\5+\u01b1")
        buf.write("\n+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\5\65\u01cb\n\65\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u01d3")
        buf.write("\n\66\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3;\3<\3")
        buf.write("<\3=\3=\3=\3>\3>\3>\3>\3>\5>\u01ec\n>\3?\3?\3?\3?\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\3B\3B\3B\3C\3C\3C\3D\3D\7D\u0201\nD\f")
        buf.write("D\16D\u0204\13D\3E\3E\3E\5E\u0209\nE\3F\3F\3F\3G\3G\3")
        buf.write("H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3")
        buf.write("Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3")
        buf.write("Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3")
        buf.write("b\3c\3c\3d\3d\3\u010b\2e\3\3\5\4\7\5\t\6\13\2\r\2\17\2")
        buf.write("\21\2\23\2\25\2\27\2\31\7\33\b\35\t\37\n!\13#\f%\r\'\16")
        buf.write(")\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31?")
        buf.write("\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-")
        buf.write("g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\u0083")
        buf.write("<\u0085=\u0087>\u0089?\u008b@\u008dA\u008fB\u0091C\u0093")
        buf.write("D\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af")
        buf.write("\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd")
        buf.write("\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\3\2$\3\2\62")
        buf.write(";\3\2\63;\4\2\62;CH\3\2\629\4\2GGgg\4\2--//\5\2\13\f\16")
        buf.write("\17\"\"\3\2c|\5\2\62;C\\c|\4\2CCcc\4\2DDdd\4\2EEee\4\2")
        buf.write("FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4")
        buf.write("\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTt")
        buf.write("t\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2")
        buf.write("[[{{\4\2\\\\||\2\u0248\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\3\u00c9\3\2\2\2\5\u00cb\3\2\2\2\7\u00cd")
        buf.write("\3\2\2\2\t\u00cf\3\2\2\2\13\u00d1\3\2\2\2\r\u00d3\3\2")
        buf.write("\2\2\17\u00de\3\2\2\2\21\u00e9\3\2\2\2\23\u00f0\3\2\2")
        buf.write("\2\25\u00f2\3\2\2\2\27\u00f4\3\2\2\2\31\u00fa\3\2\2\2")
        buf.write("\33\u00fc\3\2\2\2\35\u00ff\3\2\2\2\37\u0105\3\2\2\2!\u0113")
        buf.write("\3\2\2\2#\u0118\3\2\2\2%\u011e\3\2\2\2\'\u0127\3\2\2\2")
        buf.write(")\u012a\3\2\2\2+\u012f\3\2\2\2-\u0136\3\2\2\2/\u013e\3")
        buf.write("\2\2\2\61\u0144\3\2\2\2\63\u014b\3\2\2\2\65\u0154\3\2")
        buf.write("\2\2\67\u0158\3\2\2\29\u0161\3\2\2\2;\u0164\3\2\2\2=\u016e")
        buf.write("\3\2\2\2?\u0175\3\2\2\2A\u017a\3\2\2\2C\u017e\3\2\2\2")
        buf.write("E\u0184\3\2\2\2G\u0189\3\2\2\2I\u018f\3\2\2\2K\u0198\3")
        buf.write("\2\2\2M\u019d\3\2\2\2O\u019f\3\2\2\2Q\u01a1\3\2\2\2S\u01a4")
        buf.write("\3\2\2\2U\u01b0\3\2\2\2W\u01b2\3\2\2\2Y\u01b4\3\2\2\2")
        buf.write("[\u01b6\3\2\2\2]\u01b8\3\2\2\2_\u01ba\3\2\2\2a\u01bc\3")
        buf.write("\2\2\2c\u01bf\3\2\2\2e\u01c2\3\2\2\2g\u01c5\3\2\2\2i\u01ca")
        buf.write("\3\2\2\2k\u01d2\3\2\2\2m\u01d4\3\2\2\2o\u01d6\3\2\2\2")
        buf.write("q\u01d9\3\2\2\2s\u01dc\3\2\2\2u\u01de\3\2\2\2w\u01e1\3")
        buf.write("\2\2\2y\u01e3\3\2\2\2{\u01eb\3\2\2\2}\u01ed\3\2\2\2\177")
        buf.write("\u01f1\3\2\2\2\u0081\u01f4\3\2\2\2\u0083\u01f8\3\2\2\2")
        buf.write("\u0085\u01fb\3\2\2\2\u0087\u01fe\3\2\2\2\u0089\u0208\3")
        buf.write("\2\2\2\u008b\u020a\3\2\2\2\u008d\u020d\3\2\2\2\u008f\u020f")
        buf.write("\3\2\2\2\u0091\u0211\3\2\2\2\u0093\u0213\3\2\2\2\u0095")
        buf.write("\u0215\3\2\2\2\u0097\u0217\3\2\2\2\u0099\u0219\3\2\2\2")
        buf.write("\u009b\u021b\3\2\2\2\u009d\u021d\3\2\2\2\u009f\u021f\3")
        buf.write("\2\2\2\u00a1\u0221\3\2\2\2\u00a3\u0223\3\2\2\2\u00a5\u0225")
        buf.write("\3\2\2\2\u00a7\u0227\3\2\2\2\u00a9\u0229\3\2\2\2\u00ab")
        buf.write("\u022b\3\2\2\2\u00ad\u022d\3\2\2\2\u00af\u022f\3\2\2\2")
        buf.write("\u00b1\u0231\3\2\2\2\u00b3\u0233\3\2\2\2\u00b5\u0235\3")
        buf.write("\2\2\2\u00b7\u0237\3\2\2\2\u00b9\u0239\3\2\2\2\u00bb\u023b")
        buf.write("\3\2\2\2\u00bd\u023d\3\2\2\2\u00bf\u023f\3\2\2\2\u00c1")
        buf.write("\u0241\3\2\2\2\u00c3\u0243\3\2\2\2\u00c5\u0245\3\2\2\2")
        buf.write("\u00c7\u0247\3\2\2\2\u00c9\u00ca\7]\2\2\u00ca\4\3\2\2")
        buf.write("\2\u00cb\u00cc\7_\2\2\u00cc\6\3\2\2\2\u00cd\u00ce\7}\2")
        buf.write("\2\u00ce\b\3\2\2\2\u00cf\u00d0\7\177\2\2\u00d0\n\3\2\2")
        buf.write("\2\u00d1\u00d2\t\2\2\2\u00d2\f\3\2\2\2\u00d3\u00d7\t\3")
        buf.write("\2\2\u00d4\u00d6\5\13\6\2\u00d5\u00d4\3\2\2\2\u00d6\u00d9")
        buf.write("\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8")
        buf.write("\16\3\2\2\2\u00d9\u00d7\3\2\2\2\u00da\u00db\7\62\2\2\u00db")
        buf.write("\u00df\7z\2\2\u00dc\u00dd\7\62\2\2\u00dd\u00df\7Z\2\2")
        buf.write("\u00de\u00da\3\2\2\2\u00de\u00dc\3\2\2\2\u00df\u00e1\3")
        buf.write("\2\2\2\u00e0\u00e2\t\4\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3")
        buf.write("\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\20\3\2\2\2\u00e5\u00e6\7\62\2\2\u00e6\u00ea\7q\2\2\u00e7")
        buf.write("\u00e8\7\62\2\2\u00e8\u00ea\7Q\2\2\u00e9\u00e5\3\2\2\2")
        buf.write("\u00e9\u00e7\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00ed\t")
        buf.write("\5\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee\u00ec")
        buf.write("\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\22\3\2\2\2\u00f0\u00f1")
        buf.write("\t\6\2\2\u00f1\24\3\2\2\2\u00f2\u00f3\7\60\2\2\u00f3\26")
        buf.write("\3\2\2\2\u00f4\u00f6\5\23\n\2\u00f5\u00f7\t\7\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f9\5\r\7\2\u00f9\30\3\2\2\2\u00fa\u00fb\7=\2")
        buf.write("\2\u00fb\32\3\2\2\2\u00fc\u00fd\7<\2\2\u00fd\34\3\2\2")
        buf.write("\2\u00fe\u0100\t\b\2\2\u00ff\u00fe\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u00ff\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0104\b\17\2\2\u0104\36\3\2\2\2\u0105")
        buf.write("\u0106\7,\2\2\u0106\u0107\7,\2\2\u0107\u010b\3\2\2\2\u0108")
        buf.write("\u010a\13\2\2\2\u0109\u0108\3\2\2\2\u010a\u010d\3\2\2")
        buf.write("\2\u010b\u010c\3\2\2\2\u010b\u0109\3\2\2\2\u010c\u010e")
        buf.write("\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\7,\2\2\u010f")
        buf.write("\u0110\7,\2\2\u0110\u0111\3\2\2\2\u0111\u0112\b\20\2\2")
        buf.write("\u0112 \3\2\2\2\u0113\u0114\7D\2\2\u0114\u0115\5\u00b1")
        buf.write("Y\2\u0115\u0116\5\u009bN\2\u0116\u0117\5\u00c5c\2\u0117")
        buf.write("\"\3\2\2\2\u0118\u0119\7D\2\2\u0119\u011a\5\u00b7\\\2")
        buf.write("\u011a\u011b\5\u009dO\2\u011b\u011c\5\u0095K\2\u011c\u011d")
        buf.write("\5\u00a9U\2\u011d$\3\2\2\2\u011e\u011f\7E\2\2\u011f\u0120")
        buf.write("\5\u00b1Y\2\u0120\u0121\5\u00afX\2\u0121\u0122\5\u00bb")
        buf.write("^\2\u0122\u0123\5\u00a5S\2\u0123\u0124\5\u00afX\2\u0124")
        buf.write("\u0125\5\u00bd_\2\u0125\u0126\5\u009dO\2\u0126&\3\2\2")
        buf.write("\2\u0127\u0128\7F\2\2\u0128\u0129\5\u00b1Y\2\u0129(\3")
        buf.write("\2\2\2\u012a\u012b\7G\2\2\u012b\u012c\5\u00abV\2\u012c")
        buf.write("\u012d\5\u00b9]\2\u012d\u012e\5\u009dO\2\u012e*\3\2\2")
        buf.write("\2\u012f\u0130\7G\2\2\u0130\u0131\5\u00abV\2\u0131\u0132")
        buf.write("\5\u00b9]\2\u0132\u0133\5\u009dO\2\u0133\u0134\5\u00a5")
        buf.write("S\2\u0134\u0135\5\u009fP\2\u0135,\3\2\2\2\u0136\u0137")
        buf.write("\7G\2\2\u0137\u0138\5\u00afX\2\u0138\u0139\5\u009bN\2")
        buf.write("\u0139\u013a\5\u0097L\2\u013a\u013b\5\u00b1Y\2\u013b\u013c")
        buf.write("\5\u009bN\2\u013c\u013d\5\u00c5c\2\u013d.\3\2\2\2\u013e")
        buf.write("\u013f\7G\2\2\u013f\u0140\5\u00afX\2\u0140\u0141\5\u009b")
        buf.write("N\2\u0141\u0142\5\u00a5S\2\u0142\u0143\5\u009fP\2\u0143")
        buf.write("\60\3\2\2\2\u0144\u0145\7G\2\2\u0145\u0146\5\u00afX\2")
        buf.write("\u0146\u0147\5\u009bN\2\u0147\u0148\5\u009fP\2\u0148\u0149")
        buf.write("\5\u00b1Y\2\u0149\u014a\5\u00b7\\\2\u014a\62\3\2\2\2\u014b")
        buf.write("\u014c\7G\2\2\u014c\u014d\5\u00afX\2\u014d\u014e\5\u009b")
        buf.write("N\2\u014e\u014f\5\u00c1a\2\u014f\u0150\5\u00a3R\2\u0150")
        buf.write("\u0151\5\u00a5S\2\u0151\u0152\5\u00abV\2\u0152\u0153\5")
        buf.write("\u009dO\2\u0153\64\3\2\2\2\u0154\u0155\7H\2\2\u0155\u0156")
        buf.write("\5\u00b1Y\2\u0156\u0157\5\u00b7\\\2\u0157\66\3\2\2\2\u0158")
        buf.write("\u0159\7H\2\2\u0159\u015a\5\u00bd_\2\u015a\u015b\5\u00af")
        buf.write("X\2\u015b\u015c\5\u0099M\2\u015c\u015d\5\u00bb^\2\u015d")
        buf.write("\u015e\5\u00a5S\2\u015e\u015f\5\u00b1Y\2\u015f\u0160\5")
        buf.write("\u00afX\2\u01608\3\2\2\2\u0161\u0162\7K\2\2\u0162\u0163")
        buf.write("\5\u009fP\2\u0163:\3\2\2\2\u0164\u0165\7R\2\2\u0165\u0166")
        buf.write("\5\u0095K\2\u0166\u0167\5\u00b7\\\2\u0167\u0168\5\u0095")
        buf.write("K\2\u0168\u0169\5\u00adW\2\u0169\u016a\5\u009dO\2\u016a")
        buf.write("\u016b\5\u00bb^\2\u016b\u016c\5\u009dO\2\u016c\u016d\5")
        buf.write("\u00b7\\\2\u016d<\3\2\2\2\u016e\u016f\7T\2\2\u016f\u0170")
        buf.write("\5\u009dO\2\u0170\u0171\5\u00bb^\2\u0171\u0172\5\u00bd")
        buf.write("_\2\u0172\u0173\5\u00b7\\\2\u0173\u0174\5\u00afX\2\u0174")
        buf.write(">\3\2\2\2\u0175\u0176\7V\2\2\u0176\u0177\5\u00a3R\2\u0177")
        buf.write("\u0178\5\u009dO\2\u0178\u0179\5\u00afX\2\u0179@\3\2\2")
        buf.write("\2\u017a\u017b\7X\2\2\u017b\u017c\5\u0095K\2\u017c\u017d")
        buf.write("\5\u00b7\\\2\u017dB\3\2\2\2\u017e\u017f\7Y\2\2\u017f\u0180")
        buf.write("\5\u00a3R\2\u0180\u0181\5\u00a5S\2\u0181\u0182\5\u00ab")
        buf.write("V\2\u0182\u0183\5\u009dO\2\u0183D\3\2\2\2\u0184\u0185")
        buf.write("\7V\2\2\u0185\u0186\5\u00b7\\\2\u0186\u0187\5\u00bd_\2")
        buf.write("\u0187\u0188\5\u009dO\2\u0188F\3\2\2\2\u0189\u018a\7H")
        buf.write("\2\2\u018a\u018b\5\u0095K\2\u018b\u018c\5\u00abV\2\u018c")
        buf.write("\u018d\5\u00b9]\2\u018d\u018e\5\u009dO\2\u018eH\3\2\2")
        buf.write("\2\u018f\u0190\7G\2\2\u0190\u0191\5\u00afX\2\u0191\u0192")
        buf.write("\5\u009bN\2\u0192\u0193\5\u009bN\2\u0193\u0194\5\u00b1")
        buf.write("Y\2\u0194J\3\2\2\2\u0195\u0199\5M\'\2\u0196\u0199\5U+")
        buf.write("\2\u0197\u0199\5i\65\2\u0198\u0195\3\2\2\2\u0198\u0196")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199L\3\2\2\2\u019a\u019e")
        buf.write("\5O(\2\u019b\u019e\5Q)\2\u019c\u019e\5S*\2\u019d\u019a")
        buf.write("\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("N\3\2\2\2\u019f\u01a0\7#\2\2\u01a0P\3\2\2\2\u01a1\u01a2")
        buf.write("\7(\2\2\u01a2\u01a3\7(\2\2\u01a3R\3\2\2\2\u01a4\u01a5")
        buf.write("\7~\2\2\u01a5\u01a6\7~\2\2\u01a6T\3\2\2\2\u01a7\u01b1")
        buf.write("\5W,\2\u01a8\u01b1\5Y-\2\u01a9\u01b1\5[.\2\u01aa\u01b1")
        buf.write("\5]/\2\u01ab\u01b1\5_\60\2\u01ac\u01b1\5a\61\2\u01ad\u01b1")
        buf.write("\5c\62\2\u01ae\u01b1\5e\63\2\u01af\u01b1\5g\64\2\u01b0")
        buf.write("\u01a7\3\2\2\2\u01b0\u01a8\3\2\2\2\u01b0\u01a9\3\2\2\2")
        buf.write("\u01b0\u01aa\3\2\2\2\u01b0\u01ab\3\2\2\2\u01b0\u01ac\3")
        buf.write("\2\2\2\u01b0\u01ad\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01af")
        buf.write("\3\2\2\2\u01b1V\3\2\2\2\u01b2\u01b3\7-\2\2\u01b3X\3\2")
        buf.write("\2\2\u01b4\u01b5\7/\2\2\u01b5Z\3\2\2\2\u01b6\u01b7\7,")
        buf.write("\2\2\u01b7\\\3\2\2\2\u01b8\u01b9\7^\2\2\u01b9^\3\2\2\2")
        buf.write("\u01ba\u01bb\7\'\2\2\u01bb`\3\2\2\2\u01bc\u01bd\5W,\2")
        buf.write("\u01bd\u01be\5\25\13\2\u01beb\3\2\2\2\u01bf\u01c0\5Y-")
        buf.write("\2\u01c0\u01c1\5\25\13\2\u01c1d\3\2\2\2\u01c2\u01c3\5")
        buf.write("[.\2\u01c3\u01c4\5\25\13\2\u01c4f\3\2\2\2\u01c5\u01c6")
        buf.write("\5]/\2\u01c6\u01c7\5\25\13\2\u01c7h\3\2\2\2\u01c8\u01cb")
        buf.write("\5k\66\2\u01c9\u01cb\5{>\2\u01ca\u01c8\3\2\2\2\u01ca\u01c9")
        buf.write("\3\2\2\2\u01cbj\3\2\2\2\u01cc\u01d3\5o8\2\u01cd\u01d3")
        buf.write("\5q9\2\u01ce\u01d3\5s:\2\u01cf\u01d3\5u;\2\u01d0\u01d3")
        buf.write("\5w<\2\u01d1\u01d3\5y=\2\u01d2\u01cc\3\2\2\2\u01d2\u01cd")
        buf.write("\3\2\2\2\u01d2\u01ce\3\2\2\2\u01d2\u01cf\3\2\2\2\u01d2")
        buf.write("\u01d0\3\2\2\2\u01d2\u01d1\3\2\2\2\u01d3l\3\2\2\2\u01d4")
        buf.write("\u01d5\7?\2\2\u01d5n\3\2\2\2\u01d6\u01d7\5m\67\2\u01d7")
        buf.write("\u01d8\5m\67\2\u01d8p\3\2\2\2\u01d9\u01da\5O(\2\u01da")
        buf.write("\u01db\5m\67\2\u01dbr\3\2\2\2\u01dc\u01dd\7>\2\2\u01dd")
        buf.write("t\3\2\2\2\u01de\u01df\5s:\2\u01df\u01e0\5m\67\2\u01e0")
        buf.write("v\3\2\2\2\u01e1\u01e2\7@\2\2\u01e2x\3\2\2\2\u01e3\u01e4")
        buf.write("\5w<\2\u01e4\u01e5\5m\67\2\u01e5z\3\2\2\2\u01e6\u01ec")
        buf.write("\5}?\2\u01e7\u01ec\5\177@\2\u01e8\u01ec\5\u0081A\2\u01e9")
        buf.write("\u01ec\5\u0083B\2\u01ea\u01ec\5\u0085C\2\u01eb\u01e6\3")
        buf.write("\2\2\2\u01eb\u01e7\3\2\2\2\u01eb\u01e8\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec|\3\2\2\2\u01ed\u01ee")
        buf.write("\5m\67\2\u01ee\u01ef\7\61\2\2\u01ef\u01f0\5m\67\2\u01f0")
        buf.write("~\3\2\2\2\u01f1\u01f2\5s:\2\u01f2\u01f3\5\25\13\2\u01f3")
        buf.write("\u0080\3\2\2\2\u01f4\u01f5\5s:\2\u01f5\u01f6\5m\67\2\u01f6")
        buf.write("\u01f7\5\25\13\2\u01f7\u0082\3\2\2\2\u01f8\u01f9\5w<\2")
        buf.write("\u01f9\u01fa\5\25\13\2\u01fa\u0084\3\2\2\2\u01fb\u01fc")
        buf.write("\5\u0083B\2\u01fc\u01fd\5m\67\2\u01fd\u0086\3\2\2\2\u01fe")
        buf.write("\u0202\t\t\2\2\u01ff\u0201\t\n\2\2\u0200\u01ff\3\2\2\2")
        buf.write("\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203\3")
        buf.write("\2\2\2\u0203\u0088\3\2\2\2\u0204\u0202\3\2\2\2\u0205\u0209")
        buf.write("\5\r\7\2\u0206\u0209\5\17\b\2\u0207\u0209\5\21\t\2\u0208")
        buf.write("\u0205\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0207\3\2\2\2")
        buf.write("\u0209\u008a\3\2\2\2\u020a\u020b\5\r\7\2\u020b\u020c\5")
        buf.write("\27\f\2\u020c\u008c\3\2\2\2\u020d\u020e\13\2\2\2\u020e")
        buf.write("\u008e\3\2\2\2\u020f\u0210\13\2\2\2\u0210\u0090\3\2\2")
        buf.write("\2\u0211\u0212\13\2\2\2\u0212\u0092\3\2\2\2\u0213\u0214")
        buf.write("\13\2\2\2\u0214\u0094\3\2\2\2\u0215\u0216\t\13\2\2\u0216")
        buf.write("\u0096\3\2\2\2\u0217\u0218\t\f\2\2\u0218\u0098\3\2\2\2")
        buf.write("\u0219\u021a\t\r\2\2\u021a\u009a\3\2\2\2\u021b\u021c\t")
        buf.write("\16\2\2\u021c\u009c\3\2\2\2\u021d\u021e\t\6\2\2\u021e")
        buf.write("\u009e\3\2\2\2\u021f\u0220\t\17\2\2\u0220\u00a0\3\2\2")
        buf.write("\2\u0221\u0222\t\20\2\2\u0222\u00a2\3\2\2\2\u0223\u0224")
        buf.write("\t\21\2\2\u0224\u00a4\3\2\2\2\u0225\u0226\t\22\2\2\u0226")
        buf.write("\u00a6\3\2\2\2\u0227\u0228\t\23\2\2\u0228\u00a8\3\2\2")
        buf.write("\2\u0229\u022a\t\24\2\2\u022a\u00aa\3\2\2\2\u022b\u022c")
        buf.write("\t\25\2\2\u022c\u00ac\3\2\2\2\u022d\u022e\t\26\2\2\u022e")
        buf.write("\u00ae\3\2\2\2\u022f\u0230\t\27\2\2\u0230\u00b0\3\2\2")
        buf.write("\2\u0231\u0232\t\30\2\2\u0232\u00b2\3\2\2\2\u0233\u0234")
        buf.write("\t\31\2\2\u0234\u00b4\3\2\2\2\u0235\u0236\t\32\2\2\u0236")
        buf.write("\u00b6\3\2\2\2\u0237\u0238\t\33\2\2\u0238\u00b8\3\2\2")
        buf.write("\2\u0239\u023a\t\34\2\2\u023a\u00ba\3\2\2\2\u023b\u023c")
        buf.write("\t\35\2\2\u023c\u00bc\3\2\2\2\u023d\u023e\t\36\2\2\u023e")
        buf.write("\u00be\3\2\2\2\u023f\u0240\t\37\2\2\u0240\u00c0\3\2\2")
        buf.write("\2\u0241\u0242\t \2\2\u0242\u00c2\3\2\2\2\u0243\u0244")
        buf.write("\t!\2\2\u0244\u00c4\3\2\2\2\u0245\u0246\t\"\2\2\u0246")
        buf.write("\u00c6\3\2\2\2\u0247\u0248\t#\2\2\u0248\u00c8\3\2\2\2")
        buf.write("\23\2\u00d7\u00de\u00e3\u00e9\u00ee\u00f6\u0101\u010b")
        buf.write("\u0198\u019d\u01b0\u01ca\u01d2\u01eb\u0202\u0208\3\b\2")
        buf.write("\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    SEMI = 5
    COLON = 6
    WS = 7
    BCMT = 8
    BODY = 9
    BREAK = 10
    CONTINUE = 11
    DO = 12
    ELSE = 13
    ELSEIF = 14
    ENDBODY = 15
    ENDIF = 16
    ENDFOR = 17
    ENDWHILE = 18
    FOR = 19
    FUNCTION = 20
    IF = 21
    PARAMETER = 22
    RETURN = 23
    THEN = 24
    VAR = 25
    WHILE = 26
    TRUE = 27
    FALSE = 28
    ENDDO = 29
    OPERATOR = 30
    BOOL_OPERATOR = 31
    NOT = 32
    AND = 33
    OR = 34
    ARITHMETIC_OPERATOR = 35
    ADD = 36
    SUB = 37
    MUL = 38
    DIV = 39
    MOD = 40
    ADDDOT = 41
    SUBDOT = 42
    MULDOT = 43
    DIVDOT = 44
    RELATIONAL_OPERATOR = 45
    RELATIONAL_OPERATOR_INT = 46
    EQ = 47
    EQINT = 48
    NEQINT = 49
    LTINT = 50
    LTEINT = 51
    GTINT = 52
    GTEINT = 53
    RELATIONAL_OPERATOR_FLOAT = 54
    NEQF = 55
    LTF = 56
    LTEF = 57
    GTF = 58
    GTEF = 59
    ID = 60
    INT = 61
    FLOAT = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    UNTERMINATED_COMMENT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'{'", "'}'", "';'", "':'", "'!'", "'&&'", "'||'", 
            "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>",
            "SEMI", "COLON", "WS", "BCMT", "BODY", "BREAK", "CONTINUE", 
            "DO", "ELSE", "ELSEIF", "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", 
            "FOR", "FUNCTION", "IF", "PARAMETER", "RETURN", "THEN", "VAR", 
            "WHILE", "TRUE", "FALSE", "ENDDO", "OPERATOR", "BOOL_OPERATOR", 
            "NOT", "AND", "OR", "ARITHMETIC_OPERATOR", "ADD", "SUB", "MUL", 
            "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", "RELATIONAL_OPERATOR", 
            "RELATIONAL_OPERATOR_INT", "EQ", "EQINT", "NEQINT", "LTINT", 
            "LTEINT", "GTINT", "GTEINT", "RELATIONAL_OPERATOR_FLOAT", "NEQF", 
            "LTF", "LTEF", "GTF", "GTEF", "ID", "INT", "FLOAT", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "DIGIT", "DEC", "HEX", 
                  "OCT", "EXP", "DOT", "EXPONENT", "SEMI", "COLON", "WS", 
                  "BCMT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                  "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                  "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "OPERATOR", "BOOL_OPERATOR", "NOT", 
                  "AND", "OR", "ARITHMETIC_OPERATOR", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", 
                  "RELATIONAL_OPERATOR", "RELATIONAL_OPERATOR_INT", "EQ", 
                  "EQINT", "NEQINT", "LTINT", "LTEINT", "GTINT", "GTEINT", 
                  "RELATIONAL_OPERATOR_FLOAT", "NEQF", "LTF", "LTEF", "GTF", 
                  "GTEF", "ID", "INT", "FLOAT", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", "A", "B", "C", 
                  "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", 
                  "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", 
                  "Z" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


