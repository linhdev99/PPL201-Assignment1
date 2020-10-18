# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u0232\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\5\2\u00a2\n\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00aa\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4")
        buf.write("\u00b2\n\4\3\5\3\5\3\6\3\6\3\6\7\6\u00b9\n\6\f\6\16\6")
        buf.write("\u00bc\13\6\5\6\u00be\n\6\3\7\3\7\3\7\3\7\5\7\u00c4\n")
        buf.write("\7\3\7\6\7\u00c7\n\7\r\7\16\7\u00c8\3\b\3\b\3\b\3\b\5")
        buf.write("\b\u00cf\n\b\3\b\6\b\u00d2\n\b\r\b\16\b\u00d3\3\t\3\t")
        buf.write("\3\n\3\n\5\n\u00da\n\n\3\n\6\n\u00dd\n\n\r\n\16\n\u00de")
        buf.write("\3\13\6\13\u00e2\n\13\r\13\16\13\u00e3\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\7\f\u00ec\n\f\f\f\16\f\u00ef\13\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3#\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+")
        buf.write("\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3")
        buf.write("@\3A\3A\3B\3B\3C\3C\3D\3D\3D\5D\u01d1\nD\3E\3E\3E\3E\6")
        buf.write("E\u01d7\nE\rE\16E\u01d8\3E\5E\u01dc\nE\5E\u01de\nE\3E")
        buf.write("\3E\3E\5E\u01e3\nE\3F\3F\7F\u01e7\nF\fF\16F\u01ea\13F")
        buf.write("\3G\3G\7G\u01ee\nG\fG\16G\u01f1\13G\3G\3G\3G\3H\3H\7H")
        buf.write("\u01f8\nH\fH\16H\u01fb\13H\3H\3H\3H\3H\5H\u0201\nH\3H")
        buf.write("\3H\3I\3I\3I\3I\7I\u0209\nI\fI\16I\u020c\13I\3I\5I\u020f")
        buf.write("\nI\3I\3I\3J\3J\7J\u0215\nJ\fJ\16J\u0218\13J\3J\3J\3J")
        buf.write("\3K\3K\3K\3L\3L\5L\u0222\nL\3M\3M\3M\3M\5M\u0228\nM\3")
        buf.write("N\3N\3N\3N\3N\5N\u022f\nN\3O\3O\3\u00ed\2P\3\3\5\4\7\5")
        buf.write("\t\2\13\2\r\2\17\2\21\2\23\2\25\6\27\7\31\b\33\t\35\n")
        buf.write("\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26")
        buf.write("\67\279\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&")
        buf.write("W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8")
        buf.write("{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\u008d")
        buf.write("B\u008fC\u0091D\u0093E\u0095F\u0097\2\u0099\2\u009b\2")
        buf.write("\u009d\2\3\2\20\3\2\62;\3\2\63;\4\2\62;CH\3\2\629\4\2")
        buf.write("GGgg\4\2--//\5\2\13\f\17\17\"\"\3\2c|\6\2\62;C\\aac|\5")
        buf.write("\2\n\f\16\17^^\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3")
        buf.write("\2$$\3\2,,\2\u024f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u00a1\3\2\2")
        buf.write("\2\5\u00a9\3\2\2\2\7\u00b1\3\2\2\2\t\u00b3\3\2\2\2\13")
        buf.write("\u00bd\3\2\2\2\r\u00c3\3\2\2\2\17\u00ce\3\2\2\2\21\u00d5")
        buf.write("\3\2\2\2\23\u00d7\3\2\2\2\25\u00e1\3\2\2\2\27\u00e7\3")
        buf.write("\2\2\2\31\u00f5\3\2\2\2\33\u00fe\3\2\2\2\35\u0108\3\2")
        buf.write("\2\2\37\u010d\3\2\2\2!\u0115\3\2\2\2#\u0118\3\2\2\2%\u011d")
        buf.write("\3\2\2\2\'\u0124\3\2\2\2)\u0129\3\2\2\2+\u012f\3\2\2\2")
        buf.write("-\u0133\3\2\2\2/\u013a\3\2\2\2\61\u013d\3\2\2\2\63\u0143")
        buf.write("\3\2\2\2\65\u0149\3\2\2\2\67\u0152\3\2\2\29\u0159\3\2")
        buf.write("\2\2;\u015f\3\2\2\2=\u0168\3\2\2\2?\u016d\3\2\2\2A\u0173")
        buf.write("\3\2\2\2C\u0177\3\2\2\2E\u0179\3\2\2\2G\u017c\3\2\2\2")
        buf.write("I\u017f\3\2\2\2K\u0181\3\2\2\2M\u0183\3\2\2\2O\u0185\3")
        buf.write("\2\2\2Q\u0187\3\2\2\2S\u0189\3\2\2\2U\u018c\3\2\2\2W\u018f")
        buf.write("\3\2\2\2Y\u0192\3\2\2\2[\u0195\3\2\2\2]\u0197\3\2\2\2")
        buf.write("_\u019a\3\2\2\2a\u019d\3\2\2\2c\u019f\3\2\2\2e\u01a2\3")
        buf.write("\2\2\2g\u01a4\3\2\2\2i\u01a7\3\2\2\2k\u01ab\3\2\2\2m\u01ae")
        buf.write("\3\2\2\2o\u01b2\3\2\2\2q\u01b5\3\2\2\2s\u01b9\3\2\2\2")
        buf.write("u\u01bb\3\2\2\2w\u01bd\3\2\2\2y\u01bf\3\2\2\2{\u01c1\3")
        buf.write("\2\2\2}\u01c3\3\2\2\2\177\u01c5\3\2\2\2\u0081\u01c7\3")
        buf.write("\2\2\2\u0083\u01c9\3\2\2\2\u0085\u01cb\3\2\2\2\u0087\u01d0")
        buf.write("\3\2\2\2\u0089\u01e2\3\2\2\2\u008b\u01e4\3\2\2\2\u008d")
        buf.write("\u01eb\3\2\2\2\u008f\u01f5\3\2\2\2\u0091\u0204\3\2\2\2")
        buf.write("\u0093\u0212\3\2\2\2\u0095\u021c\3\2\2\2\u0097\u0221\3")
        buf.write("\2\2\2\u0099\u0227\3\2\2\2\u009b\u022e\3\2\2\2\u009d\u0230")
        buf.write("\3\2\2\2\u009f\u00a2\5\7\4\2\u00a0\u00a2\5\5\3\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\4\3\2\2\2\u00a3")
        buf.write("\u00aa\5]/\2\u00a4\u00aa\5_\60\2\u00a5\u00aa\5e\63\2\u00a6")
        buf.write("\u00aa\5a\61\2\u00a7\u00aa\5g\64\2\u00a8\u00aa\5c\62\2")
        buf.write("\u00a9\u00a3\3\2\2\2\u00a9\u00a4\3\2\2\2\u00a9\u00a5\3")
        buf.write("\2\2\2\u00a9\u00a6\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00a8")
        buf.write("\3\2\2\2\u00aa\6\3\2\2\2\u00ab\u00b2\5]/\2\u00ac\u00b2")
        buf.write("\5i\65\2\u00ad\u00b2\5o8\2\u00ae\u00b2\5k\66\2\u00af\u00b2")
        buf.write("\5q9\2\u00b0\u00b2\5m\67\2\u00b1\u00ab\3\2\2\2\u00b1\u00ac")
        buf.write("\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\b\3\2\2\2\u00b3")
        buf.write("\u00b4\t\2\2\2\u00b4\n\3\2\2\2\u00b5\u00be\7\62\2\2\u00b6")
        buf.write("\u00ba\t\3\2\2\u00b7\u00b9\5\t\5\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00b5")
        buf.write("\3\2\2\2\u00bd\u00b6\3\2\2\2\u00be\f\3\2\2\2\u00bf\u00c0")
        buf.write("\7\62\2\2\u00c0\u00c4\7z\2\2\u00c1\u00c2\7\62\2\2\u00c2")
        buf.write("\u00c4\7Z\2\2\u00c3\u00bf\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c4\u00c6\3\2\2\2\u00c5\u00c7\t\4\2\2\u00c6\u00c5\3")
        buf.write("\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00c6\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\16\3\2\2\2\u00ca\u00cb\7\62\2\2\u00cb\u00cf")
        buf.write("\7q\2\2\u00cc\u00cd\7\62\2\2\u00cd\u00cf\7Q\2\2\u00ce")
        buf.write("\u00ca\3\2\2\2\u00ce\u00cc\3\2\2\2\u00cf\u00d1\3\2\2\2")
        buf.write("\u00d0\u00d2\t\5\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\20")
        buf.write("\3\2\2\2\u00d5\u00d6\t\6\2\2\u00d6\22\3\2\2\2\u00d7\u00d9")
        buf.write("\5\21\t\2\u00d8\u00da\t\7\2\2\u00d9\u00d8\3\2\2\2\u00d9")
        buf.write("\u00da\3\2\2\2\u00da\u00dc\3\2\2\2\u00db\u00dd\5\t\5\2")
        buf.write("\u00dc\u00db\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00dc\3")
        buf.write("\2\2\2\u00de\u00df\3\2\2\2\u00df\24\3\2\2\2\u00e0\u00e2")
        buf.write("\t\b\2\2\u00e1\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5\u00e6\b\13\2\2\u00e6\26\3\2\2\2\u00e7\u00e8\7,")
        buf.write("\2\2\u00e8\u00e9\7,\2\2\u00e9\u00ed\3\2\2\2\u00ea\u00ec")
        buf.write("\13\2\2\2\u00eb\u00ea\3\2\2\2\u00ec\u00ef\3\2\2\2\u00ed")
        buf.write("\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ee\u00f0\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00f0\u00f1\7,\2\2\u00f1\u00f2\7")
        buf.write(",\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f4\b\f\2\2\u00f4\30")
        buf.write("\3\2\2\2\u00f5\u00f6\7H\2\2\u00f6\u00f7\7w\2\2\u00f7\u00f8")
        buf.write("\7p\2\2\u00f8\u00f9\7e\2\2\u00f9\u00fa\7v\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7p\2\2\u00fd\32")
        buf.write("\3\2\2\2\u00fe\u00ff\7R\2\2\u00ff\u0100\7c\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7c\2\2\u0102\u0103\7o\2\2\u0103\u0104")
        buf.write("\7g\2\2\u0104\u0105\7v\2\2\u0105\u0106\7g\2\2\u0106\u0107")
        buf.write("\7t\2\2\u0107\34\3\2\2\2\u0108\u0109\7D\2\2\u0109\u010a")
        buf.write("\7q\2\2\u010a\u010b\7f\2\2\u010b\u010c\7{\2\2\u010c\36")
        buf.write("\3\2\2\2\u010d\u010e\7G\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7f\2\2\u0110\u0111\7D\2\2\u0111\u0112\7q\2\2\u0112\u0113")
        buf.write("\7f\2\2\u0113\u0114\7{\2\2\u0114 \3\2\2\2\u0115\u0116")
        buf.write("\7K\2\2\u0116\u0117\7h\2\2\u0117\"\3\2\2\2\u0118\u0119")
        buf.write("\7V\2\2\u0119\u011a\7j\2\2\u011a\u011b\7g\2\2\u011b\u011c")
        buf.write("\7p\2\2\u011c$\3\2\2\2\u011d\u011e\7G\2\2\u011e\u011f")
        buf.write("\7n\2\2\u011f\u0120\7u\2\2\u0120\u0121\7g\2\2\u0121\u0122")
        buf.write("\7K\2\2\u0122\u0123\7h\2\2\u0123&\3\2\2\2\u0124\u0125")
        buf.write("\7G\2\2\u0125\u0126\7n\2\2\u0126\u0127\7u\2\2\u0127\u0128")
        buf.write("\7g\2\2\u0128(\3\2\2\2\u0129\u012a\7G\2\2\u012a\u012b")
        buf.write("\7p\2\2\u012b\u012c\7f\2\2\u012c\u012d\7K\2\2\u012d\u012e")
        buf.write("\7h\2\2\u012e*\3\2\2\2\u012f\u0130\7H\2\2\u0130\u0131")
        buf.write("\7q\2\2\u0131\u0132\7t\2\2\u0132,\3\2\2\2\u0133\u0134")
        buf.write("\7G\2\2\u0134\u0135\7p\2\2\u0135\u0136\7f\2\2\u0136\u0137")
        buf.write("\7H\2\2\u0137\u0138\7q\2\2\u0138\u0139\7t\2\2\u0139.\3")
        buf.write("\2\2\2\u013a\u013b\7F\2\2\u013b\u013c\7q\2\2\u013c\60")
        buf.write("\3\2\2\2\u013d\u013e\7G\2\2\u013e\u013f\7p\2\2\u013f\u0140")
        buf.write("\7f\2\2\u0140\u0141\7F\2\2\u0141\u0142\7q\2\2\u0142\62")
        buf.write("\3\2\2\2\u0143\u0144\7Y\2\2\u0144\u0145\7j\2\2\u0145\u0146")
        buf.write("\7k\2\2\u0146\u0147\7n\2\2\u0147\u0148\7g\2\2\u0148\64")
        buf.write("\3\2\2\2\u0149\u014a\7G\2\2\u014a\u014b\7p\2\2\u014b\u014c")
        buf.write("\7f\2\2\u014c\u014d\7Y\2\2\u014d\u014e\7j\2\2\u014e\u014f")
        buf.write("\7k\2\2\u014f\u0150\7n\2\2\u0150\u0151\7g\2\2\u0151\66")
        buf.write("\3\2\2\2\u0152\u0153\7T\2\2\u0153\u0154\7g\2\2\u0154\u0155")
        buf.write("\7v\2\2\u0155\u0156\7w\2\2\u0156\u0157\7t\2\2\u0157\u0158")
        buf.write("\7p\2\2\u01588\3\2\2\2\u0159\u015a\7D\2\2\u015a\u015b")
        buf.write("\7t\2\2\u015b\u015c\7g\2\2\u015c\u015d\7c\2\2\u015d\u015e")
        buf.write("\7m\2\2\u015e:\3\2\2\2\u015f\u0160\7E\2\2\u0160\u0161")
        buf.write("\7q\2\2\u0161\u0162\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7k\2\2\u0164\u0165\7p\2\2\u0165\u0166\7w\2\2\u0166\u0167")
        buf.write("\7g\2\2\u0167<\3\2\2\2\u0168\u0169\7V\2\2\u0169\u016a")
        buf.write("\7t\2\2\u016a\u016b\7w\2\2\u016b\u016c\7g\2\2\u016c>\3")
        buf.write("\2\2\2\u016d\u016e\7H\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7n\2\2\u0170\u0171\7u\2\2\u0171\u0172\7g\2\2\u0172@\3")
        buf.write("\2\2\2\u0173\u0174\7X\2\2\u0174\u0175\7c\2\2\u0175\u0176")
        buf.write("\7t\2\2\u0176B\3\2\2\2\u0177\u0178\7#\2\2\u0178D\3\2\2")
        buf.write("\2\u0179\u017a\7(\2\2\u017a\u017b\7(\2\2\u017bF\3\2\2")
        buf.write("\2\u017c\u017d\7~\2\2\u017d\u017e\7~\2\2\u017eH\3\2\2")
        buf.write("\2\u017f\u0180\7-\2\2\u0180J\3\2\2\2\u0181\u0182\7/\2")
        buf.write("\2\u0182L\3\2\2\2\u0183\u0184\7,\2\2\u0184N\3\2\2\2\u0185")
        buf.write("\u0186\7^\2\2\u0186P\3\2\2\2\u0187\u0188\7\'\2\2\u0188")
        buf.write("R\3\2\2\2\u0189\u018a\5I%\2\u018a\u018b\5\u0085C\2\u018b")
        buf.write("T\3\2\2\2\u018c\u018d\5K&\2\u018d\u018e\5\u0085C\2\u018e")
        buf.write("V\3\2\2\2\u018f\u0190\5M\'\2\u0190\u0191\5\u0085C\2\u0191")
        buf.write("X\3\2\2\2\u0192\u0193\5O(\2\u0193\u0194\5\u0085C\2\u0194")
        buf.write("Z\3\2\2\2\u0195\u0196\7?\2\2\u0196\\\3\2\2\2\u0197\u0198")
        buf.write("\5[.\2\u0198\u0199\5[.\2\u0199^\3\2\2\2\u019a\u019b\5")
        buf.write("C\"\2\u019b\u019c\5[.\2\u019c`\3\2\2\2\u019d\u019e\7>")
        buf.write("\2\2\u019eb\3\2\2\2\u019f\u01a0\5a\61\2\u01a0\u01a1\5")
        buf.write("[.\2\u01a1d\3\2\2\2\u01a2\u01a3\7@\2\2\u01a3f\3\2\2\2")
        buf.write("\u01a4\u01a5\5e\63\2\u01a5\u01a6\5[.\2\u01a6h\3\2\2\2")
        buf.write("\u01a7\u01a8\5[.\2\u01a8\u01a9\7\61\2\2\u01a9\u01aa\5")
        buf.write("[.\2\u01aaj\3\2\2\2\u01ab\u01ac\5a\61\2\u01ac\u01ad\5")
        buf.write("\u0085C\2\u01adl\3\2\2\2\u01ae\u01af\5a\61\2\u01af\u01b0")
        buf.write("\5[.\2\u01b0\u01b1\5\u0085C\2\u01b1n\3\2\2\2\u01b2\u01b3")
        buf.write("\5e\63\2\u01b3\u01b4\5\u0085C\2\u01b4p\3\2\2\2\u01b5\u01b6")
        buf.write("\5e\63\2\u01b6\u01b7\5[.\2\u01b7\u01b8\5\u0085C\2\u01b8")
        buf.write("r\3\2\2\2\u01b9\u01ba\7*\2\2\u01bat\3\2\2\2\u01bb\u01bc")
        buf.write("\7+\2\2\u01bcv\3\2\2\2\u01bd\u01be\7}\2\2\u01bex\3\2\2")
        buf.write("\2\u01bf\u01c0\7\177\2\2\u01c0z\3\2\2\2\u01c1\u01c2\7")
        buf.write("]\2\2\u01c2|\3\2\2\2\u01c3\u01c4\7_\2\2\u01c4~\3\2\2\2")
        buf.write("\u01c5\u01c6\7=\2\2\u01c6\u0080\3\2\2\2\u01c7\u01c8\7")
        buf.write("<\2\2\u01c8\u0082\3\2\2\2\u01c9\u01ca\7.\2\2\u01ca\u0084")
        buf.write("\3\2\2\2\u01cb\u01cc\7\60\2\2\u01cc\u0086\3\2\2\2\u01cd")
        buf.write("\u01d1\5\13\6\2\u01ce\u01d1\5\r\7\2\u01cf\u01d1\5\17\b")
        buf.write("\2\u01d0\u01cd\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u0088\3\2\2\2\u01d2\u01d3\5\13\6\2\u01d3")
        buf.write("\u01dd\5\u0085C\2\u01d4\u01de\5\23\n\2\u01d5\u01d7\5\t")
        buf.write("\5\2\u01d6\u01d5\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d6")
        buf.write("\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01db\3\2\2\2\u01da")
        buf.write("\u01dc\5\23\n\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2")
        buf.write("\2\u01dc\u01de\3\2\2\2\u01dd\u01d4\3\2\2\2\u01dd\u01d6")
        buf.write("\3\2\2\2\u01dd\u01de\3\2\2\2\u01de\u01e3\3\2\2\2\u01df")
        buf.write("\u01e0\5\13\6\2\u01e0\u01e1\5\23\n\2\u01e1\u01e3\3\2\2")
        buf.write("\2\u01e2\u01d2\3\2\2\2\u01e2\u01df\3\2\2\2\u01e3\u008a")
        buf.write("\3\2\2\2\u01e4\u01e8\t\t\2\2\u01e5\u01e7\t\n\2\2\u01e6")
        buf.write("\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e8\u01e9\3\2\2\2\u01e9\u008c\3\2\2\2\u01ea\u01e8\3")
        buf.write("\2\2\2\u01eb\u01ef\7$\2\2\u01ec\u01ee\5\u0097L\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2")
        buf.write("\u01ef\u01f0\3\2\2\2\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3")
        buf.write("\2\2\2\u01f2\u01f3\5\u009bN\2\u01f3\u01f4\bG\3\2\u01f4")
        buf.write("\u008e\3\2\2\2\u01f5\u01f9\7$\2\2\u01f6\u01f8\5\u0097")
        buf.write("L\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u0200\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u0201\t\13\2\2\u01fd\u01fe\7)\2\2")
        buf.write("\u01fe\u0201\7$\2\2\u01ff\u0201\7\2\2\3\u0200\u01fc\3")
        buf.write("\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0203\bH\4\2\u0203\u0090\3\2\2\2\u0204")
        buf.write("\u0205\7,\2\2\u0205\u0206\7,\2\2\u0206\u020a\3\2\2\2\u0207")
        buf.write("\u0209\5\u009dO\2\u0208\u0207\3\2\2\2\u0209\u020c\3\2")
        buf.write("\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020e")
        buf.write("\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020f\7,\2\2\u020e")
        buf.write("\u020d\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210\u0211\bI\5\2\u0211\u0092\3\2\2\2\u0212\u0216\7")
        buf.write("$\2\2\u0213\u0215\5\u0097L\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219\u021a\7")
        buf.write("$\2\2\u021a\u021b\bJ\6\2\u021b\u0094\3\2\2\2\u021c\u021d")
        buf.write("\13\2\2\2\u021d\u021e\bK\7\2\u021e\u0096\3\2\2\2\u021f")
        buf.write("\u0222\n\f\2\2\u0220\u0222\5\u0099M\2\u0221\u021f\3\2")
        buf.write("\2\2\u0221\u0220\3\2\2\2\u0222\u0098\3\2\2\2\u0223\u0224")
        buf.write("\7^\2\2\u0224\u0228\t\r\2\2\u0225\u0226\7)\2\2\u0226\u0228")
        buf.write("\7$\2\2\u0227\u0223\3\2\2\2\u0227\u0225\3\2\2\2\u0228")
        buf.write("\u009a\3\2\2\2\u0229\u022a\7^\2\2\u022a\u022f\n\r\2\2")
        buf.write("\u022b\u022f\7)\2\2\u022c\u022d\7)\2\2\u022d\u022f\n\16")
        buf.write("\2\2\u022e\u0229\3\2\2\2\u022e\u022b\3\2\2\2\u022e\u022c")
        buf.write("\3\2\2\2\u022f\u009c\3\2\2\2\u0230\u0231\n\17\2\2\u0231")
        buf.write("\u009e\3\2\2\2\37\2\u00a1\u00a9\u00b1\u00ba\u00bd\u00c3")
        buf.write("\u00c8\u00ce\u00d3\u00d9\u00de\u00e3\u00ed\u01d0\u01d8")
        buf.write("\u01db\u01dd\u01e2\u01e8\u01ef\u01f9\u0200\u020a\u020e")
        buf.write("\u0216\u0221\u0227\u022e\b\b\2\2\3G\2\3H\3\3I\4\3J\5\3")
        buf.write("K\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RELATIONAL = 1
    RELATIONAL_INT = 2
    RELATIONAL_FLOAT = 3
    WS = 4
    BCMT = 5
    FUNCTION = 6
    PARAMETER = 7
    BODY = 8
    ENDBODY = 9
    IF = 10
    THEN = 11
    ELSEIF = 12
    ELSE = 13
    ENDIF = 14
    FOR = 15
    ENDFOR = 16
    DO = 17
    ENDDO = 18
    WHILE = 19
    ENDWHILE = 20
    RETURN = 21
    BREAK = 22
    CONTINUE = 23
    TRUE = 24
    FALSE = 25
    VAR = 26
    NOT = 27
    AND = 28
    OR = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    ADDDOT = 35
    SUBDOT = 36
    MULDOT = 37
    DIVDOT = 38
    EQ = 39
    EQINT = 40
    NEQINT = 41
    LTINT = 42
    LTEINT = 43
    GTINT = 44
    GTEINT = 45
    NEQF = 46
    LTF = 47
    LTEF = 48
    GTF = 49
    GTEF = 50
    LP = 51
    RP = 52
    LCB = 53
    RCB = 54
    LSB = 55
    RSB = 56
    SEMI = 57
    COLON = 58
    COMMA = 59
    DOT = 60
    INTLIT = 61
    FLOATLIT = 62
    ID = 63
    ILLEGAL_ESCAPE = 64
    UNCLOSE_STRING = 65
    UNTERMINATED_COMMENT = 66
    STRINGLIT = 67
    ERROR_CHAR = 68

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
            "RELATIONAL", "RELATIONAL_INT", "RELATIONAL_FLOAT", "WS", "BCMT", 
            "FUNCTION", "PARAMETER", "BODY", "ENDBODY", "IF", "THEN", "ELSEIF", 
            "ELSE", "ENDIF", "FOR", "ENDFOR", "DO", "ENDDO", "WHILE", "ENDWHILE", 
            "RETURN", "BREAK", "CONTINUE", "TRUE", "FALSE", "VAR", "NOT", 
            "AND", "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDDOT", "SUBDOT", 
            "MULDOT", "DIVDOT", "EQ", "EQINT", "NEQINT", "LTINT", "LTEINT", 
            "GTINT", "GTEINT", "NEQF", "LTF", "LTEF", "GTF", "GTEF", "LP", 
            "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COLON", "COMMA", 
            "DOT", "INTLIT", "FLOATLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "STRINGLIT", "ERROR_CHAR" ]

    ruleNames = [ "RELATIONAL", "RELATIONAL_INT", "RELATIONAL_FLOAT", "DIGIT", 
                  "DEC", "HEX", "OCT", "EXP", "EXPONENT", "WS", "BCMT", 
                  "FUNCTION", "PARAMETER", "BODY", "ENDBODY", "IF", "THEN", 
                  "ELSEIF", "ELSE", "ENDIF", "FOR", "ENDFOR", "DO", "ENDDO", 
                  "WHILE", "ENDWHILE", "RETURN", "BREAK", "CONTINUE", "TRUE", 
                  "FALSE", "VAR", "NOT", "AND", "OR", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", 
                  "EQ", "EQINT", "NEQINT", "LTINT", "LTEINT", "GTINT", "GTEINT", 
                  "NEQF", "LTF", "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", 
                  "RCB", "LSB", "RSB", "SEMI", "COLON", "COMMA", "DOT", 
                  "INTLIT", "FLOATLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "STRINGLIT", "ERROR_CHAR", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL", "UNT_CMT" ]

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
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.UNTERMINATED_COMMENT_action 
            actions[72] = self.STRINGLIT_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		value = str(self.text)
            		raise IllegalEscape(value[1:])
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		value = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '\'"', '\\']
            		if value[-1] in possible:
            			raise UncloseString(value[1:-1])
            		else:
            			raise UncloseString(value[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    raise UnterminatedComment()
                
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		value = str(self.text)
            		self.text = value[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		raise ErrorToken(self.text)
            	
     


