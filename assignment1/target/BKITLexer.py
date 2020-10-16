# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0217\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\3\2\3\2\3\3\3\3\3\3\7\3\u00a1\n\3\f\3\16\3\u00a4")
        buf.write("\13\3\5\3\u00a6\n\3\3\4\3\4\3\4\3\4\5\4\u00ac\n\4\3\4")
        buf.write("\6\4\u00af\n\4\r\4\16\4\u00b0\3\5\3\5\3\5\3\5\5\5\u00b7")
        buf.write("\n\5\3\5\6\5\u00ba\n\5\r\5\16\5\u00bb\3\6\3\6\3\7\3\7")
        buf.write("\5\7\u00c2\n\7\3\7\6\7\u00c5\n\7\r\7\16\7\u00c6\3\b\6")
        buf.write("\b\u00ca\n\b\r\b\16\b\u00cb\3\b\3\b\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u00d4\n\t\f\t\16\t\u00d7\13\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(")
        buf.write("\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=")
        buf.write("\3=\3>\3>\3?\3?\3@\3@\3A\3A\3A\5A\u01b9\nA\3B\3B\3B\3")
        buf.write("B\6B\u01bf\nB\rB\16B\u01c0\3B\5B\u01c4\nB\5B\u01c6\nB")
        buf.write("\3B\3B\3B\5B\u01cb\nB\3C\3C\5C\u01cf\nC\3D\3D\7D\u01d3")
        buf.write("\nD\fD\16D\u01d6\13D\3E\3E\3E\3F\3F\7F\u01dd\nF\fF\16")
        buf.write("F\u01e0\13F\3F\3F\3F\3G\3G\7G\u01e7\nG\fG\16G\u01ea\13")
        buf.write("G\3G\5G\u01ed\nG\3G\3G\3H\3H\3H\3H\7H\u01f5\nH\fH\16H")
        buf.write("\u01f8\13H\3H\5H\u01fb\nH\3H\3H\3I\3I\7I\u0201\nI\fI\16")
        buf.write("I\u0204\13I\3I\3I\3I\3J\3J\5J\u020b\nJ\3K\3K\3K\3K\5K")
        buf.write("\u0211\nK\3L\3L\3L\3M\3M\3\u00d5\2N\3\2\5\2\7\2\t\2\13")
        buf.write("\2\r\2\17\3\21\4\23\5\25\6\27\7\31\b\33\t\35\n\37\13!")
        buf.write("\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\27")
        buf.write("9\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([")
        buf.write(")]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177")
        buf.write(";\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\u008dB\u008f")
        buf.write("C\u0091D\u0093\2\u0095\2\u0097\2\u0099\2\3\2\17\3\2\62")
        buf.write(";\3\2\63;\4\2\62;CH\3\2\629\4\2GGgg\4\2--//\5\2\13\f\17")
        buf.write("\17\"\"\3\2c|\6\2\62;C\\aac|\3\3\f\f\7\2\n\f\16\17$$)")
        buf.write(")^^\t\2))^^ddhhppttvv\3\2,,\2\u0226\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u009b\3\2\2\2\5\u00a5")
        buf.write("\3\2\2\2\7\u00ab\3\2\2\2\t\u00b6\3\2\2\2\13\u00bd\3\2")
        buf.write("\2\2\r\u00bf\3\2\2\2\17\u00c9\3\2\2\2\21\u00cf\3\2\2\2")
        buf.write("\23\u00dd\3\2\2\2\25\u00e6\3\2\2\2\27\u00f0\3\2\2\2\31")
        buf.write("\u00f5\3\2\2\2\33\u00fd\3\2\2\2\35\u0100\3\2\2\2\37\u0105")
        buf.write("\3\2\2\2!\u010c\3\2\2\2#\u0111\3\2\2\2%\u0117\3\2\2\2")
        buf.write("\'\u011b\3\2\2\2)\u0122\3\2\2\2+\u0125\3\2\2\2-\u012b")
        buf.write("\3\2\2\2/\u0131\3\2\2\2\61\u013a\3\2\2\2\63\u0141\3\2")
        buf.write("\2\2\65\u0147\3\2\2\2\67\u0150\3\2\2\29\u0155\3\2\2\2")
        buf.write(";\u015b\3\2\2\2=\u015f\3\2\2\2?\u0161\3\2\2\2A\u0164\3")
        buf.write("\2\2\2C\u0167\3\2\2\2E\u0169\3\2\2\2G\u016b\3\2\2\2I\u016d")
        buf.write("\3\2\2\2K\u016f\3\2\2\2M\u0171\3\2\2\2O\u0174\3\2\2\2")
        buf.write("Q\u0177\3\2\2\2S\u017a\3\2\2\2U\u017d\3\2\2\2W\u017f\3")
        buf.write("\2\2\2Y\u0182\3\2\2\2[\u0185\3\2\2\2]\u0187\3\2\2\2_\u018a")
        buf.write("\3\2\2\2a\u018c\3\2\2\2c\u018f\3\2\2\2e\u0193\3\2\2\2")
        buf.write("g\u0196\3\2\2\2i\u019a\3\2\2\2k\u019d\3\2\2\2m\u01a1\3")
        buf.write("\2\2\2o\u01a3\3\2\2\2q\u01a5\3\2\2\2s\u01a7\3\2\2\2u\u01a9")
        buf.write("\3\2\2\2w\u01ab\3\2\2\2y\u01ad\3\2\2\2{\u01af\3\2\2\2")
        buf.write("}\u01b1\3\2\2\2\177\u01b3\3\2\2\2\u0081\u01b8\3\2\2\2")
        buf.write("\u0083\u01ca\3\2\2\2\u0085\u01ce\3\2\2\2\u0087\u01d0\3")
        buf.write("\2\2\2\u0089\u01d7\3\2\2\2\u008b\u01da\3\2\2\2\u008d\u01e4")
        buf.write("\3\2\2\2\u008f\u01f0\3\2\2\2\u0091\u01fe\3\2\2\2\u0093")
        buf.write("\u020a\3\2\2\2\u0095\u0210\3\2\2\2\u0097\u0212\3\2\2\2")
        buf.write("\u0099\u0215\3\2\2\2\u009b\u009c\t\2\2\2\u009c\4\3\2\2")
        buf.write("\2\u009d\u00a6\7\62\2\2\u009e\u00a2\t\3\2\2\u009f\u00a1")
        buf.write("\5\3\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a4\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a6\3\2\2\2")
        buf.write("\u00a4\u00a2\3\2\2\2\u00a5\u009d\3\2\2\2\u00a5\u009e\3")
        buf.write("\2\2\2\u00a6\6\3\2\2\2\u00a7\u00a8\7\62\2\2\u00a8\u00ac")
        buf.write("\7z\2\2\u00a9\u00aa\7\62\2\2\u00aa\u00ac\7Z\2\2\u00ab")
        buf.write("\u00a7\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac\u00ae\3\2\2\2")
        buf.write("\u00ad\u00af\t\4\2\2\u00ae\u00ad\3\2\2\2\u00af\u00b0\3")
        buf.write("\2\2\2\u00b0\u00ae\3\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\b")
        buf.write("\3\2\2\2\u00b2\u00b3\7\62\2\2\u00b3\u00b7\7q\2\2\u00b4")
        buf.write("\u00b5\7\62\2\2\u00b5\u00b7\7Q\2\2\u00b6\u00b2\3\2\2\2")
        buf.write("\u00b6\u00b4\3\2\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00ba\t")
        buf.write("\5\2\2\u00b9\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00b9")
        buf.write("\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\n\3\2\2\2\u00bd\u00be")
        buf.write("\t\6\2\2\u00be\f\3\2\2\2\u00bf\u00c1\5\13\6\2\u00c0\u00c2")
        buf.write("\t\7\2\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2")
        buf.write("\u00c4\3\2\2\2\u00c3\u00c5\5\3\2\2\u00c4\u00c3\3\2\2\2")
        buf.write("\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3")
        buf.write("\2\2\2\u00c7\16\3\2\2\2\u00c8\u00ca\t\b\2\2\u00c9\u00c8")
        buf.write("\3\2\2\2\u00ca\u00cb\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cb")
        buf.write("\u00cc\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00ce\b\b\2\2")
        buf.write("\u00ce\20\3\2\2\2\u00cf\u00d0\7,\2\2\u00d0\u00d1\7,\2")
        buf.write("\2\u00d1\u00d5\3\2\2\2\u00d2\u00d4\13\2\2\2\u00d3\u00d2")
        buf.write("\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d5")
        buf.write("\u00d3\3\2\2\2\u00d6\u00d8\3\2\2\2\u00d7\u00d5\3\2\2\2")
        buf.write("\u00d8\u00d9\7,\2\2\u00d9\u00da\7,\2\2\u00da\u00db\3\2")
        buf.write("\2\2\u00db\u00dc\b\t\2\2\u00dc\22\3\2\2\2\u00dd\u00de")
        buf.write("\7H\2\2\u00de\u00df\7w\2\2\u00df\u00e0\7p\2\2\u00e0\u00e1")
        buf.write("\7e\2\2\u00e1\u00e2\7v\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4")
        buf.write("\7q\2\2\u00e4\u00e5\7p\2\2\u00e5\24\3\2\2\2\u00e6\u00e7")
        buf.write("\7R\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea")
        buf.write("\7c\2\2\u00ea\u00eb\7o\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7v\2\2\u00ed\u00ee\7g\2\2\u00ee\u00ef\7t\2\2\u00ef\26")
        buf.write("\3\2\2\2\u00f0\u00f1\7D\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3")
        buf.write("\7f\2\2\u00f3\u00f4\7{\2\2\u00f4\30\3\2\2\2\u00f5\u00f6")
        buf.write("\7G\2\2\u00f6\u00f7\7p\2\2\u00f7\u00f8\7f\2\2\u00f8\u00f9")
        buf.write("\7D\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7f\2\2\u00fb\u00fc")
        buf.write("\7{\2\2\u00fc\32\3\2\2\2\u00fd\u00fe\7K\2\2\u00fe\u00ff")
        buf.write("\7h\2\2\u00ff\34\3\2\2\2\u0100\u0101\7V\2\2\u0101\u0102")
        buf.write("\7j\2\2\u0102\u0103\7g\2\2\u0103\u0104\7p\2\2\u0104\36")
        buf.write("\3\2\2\2\u0105\u0106\7G\2\2\u0106\u0107\7n\2\2\u0107\u0108")
        buf.write("\7u\2\2\u0108\u0109\7g\2\2\u0109\u010a\7K\2\2\u010a\u010b")
        buf.write("\7h\2\2\u010b \3\2\2\2\u010c\u010d\7G\2\2\u010d\u010e")
        buf.write("\7n\2\2\u010e\u010f\7u\2\2\u010f\u0110\7g\2\2\u0110\"")
        buf.write("\3\2\2\2\u0111\u0112\7G\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7f\2\2\u0114\u0115\7K\2\2\u0115\u0116\7h\2\2\u0116$\3")
        buf.write("\2\2\2\u0117\u0118\7H\2\2\u0118\u0119\7q\2\2\u0119\u011a")
        buf.write("\7t\2\2\u011a&\3\2\2\2\u011b\u011c\7G\2\2\u011c\u011d")
        buf.write("\7p\2\2\u011d\u011e\7f\2\2\u011e\u011f\7H\2\2\u011f\u0120")
        buf.write("\7q\2\2\u0120\u0121\7t\2\2\u0121(\3\2\2\2\u0122\u0123")
        buf.write("\7F\2\2\u0123\u0124\7q\2\2\u0124*\3\2\2\2\u0125\u0126")
        buf.write("\7G\2\2\u0126\u0127\7p\2\2\u0127\u0128\7f\2\2\u0128\u0129")
        buf.write("\7F\2\2\u0129\u012a\7q\2\2\u012a,\3\2\2\2\u012b\u012c")
        buf.write("\7Y\2\2\u012c\u012d\7j\2\2\u012d\u012e\7k\2\2\u012e\u012f")
        buf.write("\7n\2\2\u012f\u0130\7g\2\2\u0130.\3\2\2\2\u0131\u0132")
        buf.write("\7G\2\2\u0132\u0133\7p\2\2\u0133\u0134\7f\2\2\u0134\u0135")
        buf.write("\7Y\2\2\u0135\u0136\7j\2\2\u0136\u0137\7k\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7g\2\2\u0139\60\3\2\2\2\u013a\u013b")
        buf.write("\7T\2\2\u013b\u013c\7g\2\2\u013c\u013d\7v\2\2\u013d\u013e")
        buf.write("\7w\2\2\u013e\u013f\7t\2\2\u013f\u0140\7p\2\2\u0140\62")
        buf.write("\3\2\2\2\u0141\u0142\7D\2\2\u0142\u0143\7t\2\2\u0143\u0144")
        buf.write("\7g\2\2\u0144\u0145\7c\2\2\u0145\u0146\7m\2\2\u0146\64")
        buf.write("\3\2\2\2\u0147\u0148\7E\2\2\u0148\u0149\7q\2\2\u0149\u014a")
        buf.write("\7p\2\2\u014a\u014b\7v\2\2\u014b\u014c\7k\2\2\u014c\u014d")
        buf.write("\7p\2\2\u014d\u014e\7w\2\2\u014e\u014f\7g\2\2\u014f\66")
        buf.write("\3\2\2\2\u0150\u0151\7V\2\2\u0151\u0152\7t\2\2\u0152\u0153")
        buf.write("\7w\2\2\u0153\u0154\7g\2\2\u01548\3\2\2\2\u0155\u0156")
        buf.write("\7H\2\2\u0156\u0157\7c\2\2\u0157\u0158\7n\2\2\u0158\u0159")
        buf.write("\7u\2\2\u0159\u015a\7g\2\2\u015a:\3\2\2\2\u015b\u015c")
        buf.write("\7X\2\2\u015c\u015d\7c\2\2\u015d\u015e\7t\2\2\u015e<\3")
        buf.write("\2\2\2\u015f\u0160\7#\2\2\u0160>\3\2\2\2\u0161\u0162\7")
        buf.write("(\2\2\u0162\u0163\7(\2\2\u0163@\3\2\2\2\u0164\u0165\7")
        buf.write("~\2\2\u0165\u0166\7~\2\2\u0166B\3\2\2\2\u0167\u0168\7")
        buf.write("-\2\2\u0168D\3\2\2\2\u0169\u016a\7/\2\2\u016aF\3\2\2\2")
        buf.write("\u016b\u016c\7,\2\2\u016cH\3\2\2\2\u016d\u016e\7^\2\2")
        buf.write("\u016eJ\3\2\2\2\u016f\u0170\7\'\2\2\u0170L\3\2\2\2\u0171")
        buf.write("\u0172\5C\"\2\u0172\u0173\5\177@\2\u0173N\3\2\2\2\u0174")
        buf.write("\u0175\5E#\2\u0175\u0176\5\177@\2\u0176P\3\2\2\2\u0177")
        buf.write("\u0178\5G$\2\u0178\u0179\5\177@\2\u0179R\3\2\2\2\u017a")
        buf.write("\u017b\5I%\2\u017b\u017c\5\177@\2\u017cT\3\2\2\2\u017d")
        buf.write("\u017e\7?\2\2\u017eV\3\2\2\2\u017f\u0180\5U+\2\u0180\u0181")
        buf.write("\5U+\2\u0181X\3\2\2\2\u0182\u0183\5=\37\2\u0183\u0184")
        buf.write("\5U+\2\u0184Z\3\2\2\2\u0185\u0186\7>\2\2\u0186\\\3\2\2")
        buf.write("\2\u0187\u0188\5[.\2\u0188\u0189\5U+\2\u0189^\3\2\2\2")
        buf.write("\u018a\u018b\7@\2\2\u018b`\3\2\2\2\u018c\u018d\5_\60\2")
        buf.write("\u018d\u018e\5U+\2\u018eb\3\2\2\2\u018f\u0190\5U+\2\u0190")
        buf.write("\u0191\7\61\2\2\u0191\u0192\5U+\2\u0192d\3\2\2\2\u0193")
        buf.write("\u0194\5[.\2\u0194\u0195\5\177@\2\u0195f\3\2\2\2\u0196")
        buf.write("\u0197\5[.\2\u0197\u0198\5U+\2\u0198\u0199\5\177@\2\u0199")
        buf.write("h\3\2\2\2\u019a\u019b\5_\60\2\u019b\u019c\5\177@\2\u019c")
        buf.write("j\3\2\2\2\u019d\u019e\5_\60\2\u019e\u019f\5U+\2\u019f")
        buf.write("\u01a0\5\177@\2\u01a0l\3\2\2\2\u01a1\u01a2\7*\2\2\u01a2")
        buf.write("n\3\2\2\2\u01a3\u01a4\7+\2\2\u01a4p\3\2\2\2\u01a5\u01a6")
        buf.write("\7}\2\2\u01a6r\3\2\2\2\u01a7\u01a8\7\177\2\2\u01a8t\3")
        buf.write("\2\2\2\u01a9\u01aa\7]\2\2\u01aav\3\2\2\2\u01ab\u01ac\7")
        buf.write("_\2\2\u01acx\3\2\2\2\u01ad\u01ae\7=\2\2\u01aez\3\2\2\2")
        buf.write("\u01af\u01b0\7<\2\2\u01b0|\3\2\2\2\u01b1\u01b2\7.\2\2")
        buf.write("\u01b2~\3\2\2\2\u01b3\u01b4\7\60\2\2\u01b4\u0080\3\2\2")
        buf.write("\2\u01b5\u01b9\5\5\3\2\u01b6\u01b9\5\7\4\2\u01b7\u01b9")
        buf.write("\5\t\5\2\u01b8\u01b5\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9\u0082\3\2\2\2\u01ba\u01bb\5\5\3\2")
        buf.write("\u01bb\u01c5\5\177@\2\u01bc\u01c6\5\r\7\2\u01bd\u01bf")
        buf.write("\5\3\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0")
        buf.write("\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c3\3\2\2\2")
        buf.write("\u01c2\u01c4\5\r\7\2\u01c3\u01c2\3\2\2\2\u01c3\u01c4\3")
        buf.write("\2\2\2\u01c4\u01c6\3\2\2\2\u01c5\u01bc\3\2\2\2\u01c5\u01be")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01cb\3\2\2\2\u01c7")
        buf.write("\u01c8\5\5\3\2\u01c8\u01c9\5\r\7\2\u01c9\u01cb\3\2\2\2")
        buf.write("\u01ca\u01ba\3\2\2\2\u01ca\u01c7\3\2\2\2\u01cb\u0084\3")
        buf.write("\2\2\2\u01cc\u01cf\5\67\34\2\u01cd\u01cf\59\35\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u0086\3\2\2\2")
        buf.write("\u01d0\u01d4\t\t\2\2\u01d1\u01d3\t\n\2\2\u01d2\u01d1\3")
        buf.write("\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5")
        buf.write("\3\2\2\2\u01d5\u0088\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7")
        buf.write("\u01d8\13\2\2\2\u01d8\u01d9\bE\3\2\u01d9\u008a\3\2\2\2")
        buf.write("\u01da\u01de\7$\2\2\u01db\u01dd\5\u0093J\2\u01dc\u01db")
        buf.write("\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e1\u01e2\5\u0097L\2\u01e2\u01e3\bF\4\2\u01e3\u008c")
        buf.write("\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5\u01e7\5\u0093J\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3")
        buf.write("\2\2\2\u01eb\u01ed\t\13\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write("\u01ee\3\2\2\2\u01ee\u01ef\bG\5\2\u01ef\u008e\3\2\2\2")
        buf.write("\u01f0\u01f1\7,\2\2\u01f1\u01f2\7,\2\2\u01f2\u01f6\3\2")
        buf.write("\2\2\u01f3\u01f5\5\u0099M\2\u01f4\u01f3\3\2\2\2\u01f5")
        buf.write("\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2")
        buf.write("\u01f7\u01fa\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\7")
        buf.write(",\2\2\u01fa\u01f9\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fc")
        buf.write("\3\2\2\2\u01fc\u01fd\bH\6\2\u01fd\u0090\3\2\2\2\u01fe")
        buf.write("\u0202\7$\2\2\u01ff\u0201\5\u0093J\2\u0200\u01ff\3\2\2")
        buf.write("\2\u0201\u0204\3\2\2\2\u0202\u0200\3\2\2\2\u0202\u0203")
        buf.write("\3\2\2\2\u0203\u0205\3\2\2\2\u0204\u0202\3\2\2\2\u0205")
        buf.write("\u0206\7$\2\2\u0206\u0207\bI\7\2\u0207\u0092\3\2\2\2\u0208")
        buf.write("\u020b\n\f\2\2\u0209\u020b\5\u0095K\2\u020a\u0208\3\2")
        buf.write("\2\2\u020a\u0209\3\2\2\2\u020b\u0094\3\2\2\2\u020c\u020d")
        buf.write("\7^\2\2\u020d\u0211\t\r\2\2\u020e\u020f\7)\2\2\u020f\u0211")
        buf.write("\7$\2\2\u0210\u020c\3\2\2\2\u0210\u020e\3\2\2\2\u0211")
        buf.write("\u0096\3\2\2\2\u0212\u0213\7^\2\2\u0213\u0214\n\r\2\2")
        buf.write("\u0214\u0098\3\2\2\2\u0215\u0216\n\16\2\2\u0216\u009a")
        buf.write("\3\2\2\2\34\2\u00a2\u00a5\u00ab\u00b0\u00b6\u00bb\u00c1")
        buf.write("\u00c6\u00cb\u00d5\u01b8\u01c0\u01c3\u01c5\u01ca\u01ce")
        buf.write("\u01d4\u01de\u01e8\u01ec\u01f6\u01fa\u0202\u020a\u0210")
        buf.write("\b\b\2\2\3E\2\3F\3\3G\4\3H\5\3I\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BCMT = 2
    FUNCTION = 3
    PARAMETER = 4
    BODY = 5
    ENDBODY = 6
    IF = 7
    THEN = 8
    ELSEIF = 9
    ELSE = 10
    ENDIF = 11
    FOR = 12
    ENDFOR = 13
    DO = 14
    ENDDO = 15
    WHILE = 16
    ENDWHILE = 17
    RETURN = 18
    BREAK = 19
    CONTINUE = 20
    TRUE = 21
    FALSE = 22
    VAR = 23
    NOT = 24
    AND = 25
    OR = 26
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    MOD = 31
    ADDDOT = 32
    SUBDOT = 33
    MULDOT = 34
    DIVDOT = 35
    EQ = 36
    EQINT = 37
    NEQINT = 38
    LTINT = 39
    LTEINT = 40
    GTINT = 41
    GTEINT = 42
    NEQF = 43
    LTF = 44
    LTEF = 45
    GTF = 46
    GTEF = 47
    LP = 48
    RP = 49
    LCB = 50
    RCB = 51
    LSB = 52
    RSB = 53
    SEMI = 54
    COLON = 55
    COMMA = 56
    DOT = 57
    INTLIT = 58
    FLOATLIT = 59
    BOOLEANLIT = 60
    ID = 61
    ERROR_CHAR = 62
    ILLEGAL_ESCAPE = 63
    UNCLOSE_STRING = 64
    UNTERMINATED_COMMENT = 65
    STRINGLIT = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Function'", "'Parameter'", "'Body'", "'EndBody'", "'If'", 
            "'Then'", "'ElseIf'", "'Else'", "'EndIf'", "'For'", "'EndFor'", 
            "'Do'", "'EndDo'", "'While'", "'EndWhile'", "'Return'", "'Break'", 
            "'Continue'", "'True'", "'False'", "'Var'", "'!'", "'&&'", "'||'", 
            "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", "'<'", "'>'", "'('", 
            "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BCMT", "FUNCTION", "PARAMETER", "BODY", "ENDBODY", "IF", 
            "THEN", "ELSEIF", "ELSE", "ENDIF", "FOR", "ENDFOR", "DO", "ENDDO", 
            "WHILE", "ENDWHILE", "RETURN", "BREAK", "CONTINUE", "TRUE", 
            "FALSE", "VAR", "NOT", "AND", "OR", "ADD", "SUB", "MUL", "DIV", 
            "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", "EQ", "EQINT", 
            "NEQINT", "LTINT", "LTEINT", "GTINT", "GTEINT", "NEQF", "LTF", 
            "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
            "SEMI", "COLON", "COMMA", "DOT", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
            "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
            "STRINGLIT" ]

    ruleNames = [ "DIGIT", "DEC", "HEX", "OCT", "EXP", "EXPONENT", "WS", 
                  "BCMT", "FUNCTION", "PARAMETER", "BODY", "ENDBODY", "IF", 
                  "THEN", "ELSEIF", "ELSE", "ENDIF", "FOR", "ENDFOR", "DO", 
                  "ENDDO", "WHILE", "ENDWHILE", "RETURN", "BREAK", "CONTINUE", 
                  "TRUE", "FALSE", "VAR", "NOT", "AND", "OR", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", 
                  "EQ", "EQINT", "NEQINT", "LTINT", "LTEINT", "GTINT", "GTEINT", 
                  "NEQF", "LTF", "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", 
                  "RCB", "LSB", "RSB", "SEMI", "COLON", "COMMA", "DOT", 
                  "INTLIT", "FLOATLIT", "BOOLEANLIT", "ID", "ERROR_CHAR", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "UNTERMINATED_COMMENT", 
                  "STRINGLIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "UNT_CMT" ]

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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[67] = self.ERROR_CHAR_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.UNTERMINATED_COMMENT_action 
            actions[71] = self.STRINGLIT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		raise ErrorToken(self.text)
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		value = str(self.text)
            		raise IllegalEscape(value[1:])
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		value = str(self.text)
            		possible = ['\n']
            		if value[-1] in possible:
            			raise UncloseString(value[1:-1])
            		else:
            			raise UncloseString(value[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UnterminatedComment()
                
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		value = str(self.text)
            		self.text = value[1:-1]
            	
     


