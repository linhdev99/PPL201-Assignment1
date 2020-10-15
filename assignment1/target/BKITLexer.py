# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u027e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\3\2\3\2\3\3\3\3\3\3\7\3\u00d5\n\3\f\3\16\3\u00d8")
        buf.write("\13\3\5\3\u00da\n\3\3\4\3\4\3\4\3\4\5\4\u00e0\n\4\3\4")
        buf.write("\6\4\u00e3\n\4\r\4\16\4\u00e4\3\5\3\5\3\5\3\5\5\5\u00eb")
        buf.write("\n\5\3\5\6\5\u00ee\n\5\r\5\16\5\u00ef\3\6\3\6\3\7\3\7")
        buf.write("\5\7\u00f6\n\7\3\7\6\7\u00f9\n\7\r\7\16\7\u00fa\3\b\6")
        buf.write("\b\u00fe\n\b\r\b\16\b\u00ff\3\b\3\b\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u0108\n\t\f\t\16\t\u010b\13\t\3\t\3\t\3\t\3\t\3\t\3")
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
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3A\5A\u01ec\nA\3B\3B\3B\3B\6B\u01f2")
        buf.write("\nB\rB\16B\u01f3\3B\5B\u01f7\nB\5B\u01f9\nB\3B\3B\3B\5")
        buf.write("B\u01fe\nB\3C\3C\5C\u0202\nC\3D\3D\7D\u0206\nD\fD\16D")
        buf.write("\u0209\13D\3E\3E\3E\3F\3F\7F\u0210\nF\fF\16F\u0213\13")
        buf.write("F\3F\3F\3F\3G\3G\7G\u021a\nG\fG\16G\u021d\13G\3G\5G\u0220")
        buf.write("\nG\3G\3G\3H\3H\3H\3H\7H\u0228\nH\fH\16H\u022b\13H\3H")
        buf.write("\5H\u022e\nH\3H\3H\3I\3I\7I\u0234\nI\fI\16I\u0237\13I")
        buf.write("\3I\3I\3I\3J\3J\5J\u023e\nJ\3K\3K\3K\3K\5K\u0244\nK\3")
        buf.write("L\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3")
        buf.write("T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3")
        buf.write("]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3")
        buf.write("f\3f\3g\3g\3\u0109\2h\3\2\5\2\7\2\t\2\13\2\r\2\17\3\21")
        buf.write("\4\23\5\25\6\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'\17")
        buf.write(")\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32?")
        buf.write("\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/")
        buf.write("i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\u008dB\u008fC\u0091D\u0093")
        buf.write("\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d\2\u009f\2\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af")
        buf.write("\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd")
        buf.write("\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb")
        buf.write("\2\u00cd\2\3\2(\3\2\62;\3\2\63;\4\2\62;CH\3\2\629\4\2")
        buf.write("GGgg\4\2--//\5\2\13\f\17\17\"\"\3\2c|\6\2\62;C\\aac|\3")
        buf.write("\3\f\f\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2,,\4\2")
        buf.write("CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4")
        buf.write("\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQq")
        buf.write("q\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2")
        buf.write("XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u0273\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u00cf\3\2\2")
        buf.write("\2\5\u00d9\3\2\2\2\7\u00df\3\2\2\2\t\u00ea\3\2\2\2\13")
        buf.write("\u00f1\3\2\2\2\r\u00f3\3\2\2\2\17\u00fd\3\2\2\2\21\u0103")
        buf.write("\3\2\2\2\23\u0111\3\2\2\2\25\u011a\3\2\2\2\27\u0124\3")
        buf.write("\2\2\2\31\u0129\3\2\2\2\33\u0131\3\2\2\2\35\u0134\3\2")
        buf.write("\2\2\37\u0139\3\2\2\2!\u0140\3\2\2\2#\u0145\3\2\2\2%\u014b")
        buf.write("\3\2\2\2\'\u014f\3\2\2\2)\u0156\3\2\2\2+\u0159\3\2\2\2")
        buf.write("-\u015f\3\2\2\2/\u0165\3\2\2\2\61\u016e\3\2\2\2\63\u0175")
        buf.write("\3\2\2\2\65\u017b\3\2\2\2\67\u0184\3\2\2\29\u0189\3\2")
        buf.write("\2\2;\u018f\3\2\2\2=\u0193\3\2\2\2?\u0195\3\2\2\2A\u0198")
        buf.write("\3\2\2\2C\u019b\3\2\2\2E\u019d\3\2\2\2G\u019f\3\2\2\2")
        buf.write("I\u01a1\3\2\2\2K\u01a3\3\2\2\2M\u01a5\3\2\2\2O\u01a8\3")
        buf.write("\2\2\2Q\u01ab\3\2\2\2S\u01ae\3\2\2\2U\u01b1\3\2\2\2W\u01b3")
        buf.write("\3\2\2\2Y\u01b6\3\2\2\2[\u01b9\3\2\2\2]\u01bb\3\2\2\2")
        buf.write("_\u01be\3\2\2\2a\u01c0\3\2\2\2c\u01c3\3\2\2\2e\u01c7\3")
        buf.write("\2\2\2g\u01ca\3\2\2\2i\u01ce\3\2\2\2k\u01d1\3\2\2\2m\u01d4")
        buf.write("\3\2\2\2o\u01d6\3\2\2\2q\u01d8\3\2\2\2s\u01da\3\2\2\2")
        buf.write("u\u01dc\3\2\2\2w\u01de\3\2\2\2y\u01e0\3\2\2\2{\u01e2\3")
        buf.write("\2\2\2}\u01e4\3\2\2\2\177\u01e6\3\2\2\2\u0081\u01eb\3")
        buf.write("\2\2\2\u0083\u01fd\3\2\2\2\u0085\u0201\3\2\2\2\u0087\u0203")
        buf.write("\3\2\2\2\u0089\u020a\3\2\2\2\u008b\u020d\3\2\2\2\u008d")
        buf.write("\u0217\3\2\2\2\u008f\u0223\3\2\2\2\u0091\u0231\3\2\2\2")
        buf.write("\u0093\u023d\3\2\2\2\u0095\u0243\3\2\2\2\u0097\u0245\3")
        buf.write("\2\2\2\u0099\u0248\3\2\2\2\u009b\u024a\3\2\2\2\u009d\u024c")
        buf.write("\3\2\2\2\u009f\u024e\3\2\2\2\u00a1\u0250\3\2\2\2\u00a3")
        buf.write("\u0252\3\2\2\2\u00a5\u0254\3\2\2\2\u00a7\u0256\3\2\2\2")
        buf.write("\u00a9\u0258\3\2\2\2\u00ab\u025a\3\2\2\2\u00ad\u025c\3")
        buf.write("\2\2\2\u00af\u025e\3\2\2\2\u00b1\u0260\3\2\2\2\u00b3\u0262")
        buf.write("\3\2\2\2\u00b5\u0264\3\2\2\2\u00b7\u0266\3\2\2\2\u00b9")
        buf.write("\u0268\3\2\2\2\u00bb\u026a\3\2\2\2\u00bd\u026c\3\2\2\2")
        buf.write("\u00bf\u026e\3\2\2\2\u00c1\u0270\3\2\2\2\u00c3\u0272\3")
        buf.write("\2\2\2\u00c5\u0274\3\2\2\2\u00c7\u0276\3\2\2\2\u00c9\u0278")
        buf.write("\3\2\2\2\u00cb\u027a\3\2\2\2\u00cd\u027c\3\2\2\2\u00cf")
        buf.write("\u00d0\t\2\2\2\u00d0\4\3\2\2\2\u00d1\u00da\7\62\2\2\u00d2")
        buf.write("\u00d6\t\3\2\2\u00d3\u00d5\5\3\2\2\u00d4\u00d3\3\2\2\2")
        buf.write("\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00d1")
        buf.write("\3\2\2\2\u00d9\u00d2\3\2\2\2\u00da\6\3\2\2\2\u00db\u00dc")
        buf.write("\7\62\2\2\u00dc\u00e0\7z\2\2\u00dd\u00de\7\62\2\2\u00de")
        buf.write("\u00e0\7Z\2\2\u00df\u00db\3\2\2\2\u00df\u00dd\3\2\2\2")
        buf.write("\u00e0\u00e2\3\2\2\2\u00e1\u00e3\t\4\2\2\u00e2\u00e1\3")
        buf.write("\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5")
        buf.write("\3\2\2\2\u00e5\b\3\2\2\2\u00e6\u00e7\7\62\2\2\u00e7\u00eb")
        buf.write("\7q\2\2\u00e8\u00e9\7\62\2\2\u00e9\u00eb\7Q\2\2\u00ea")
        buf.write("\u00e6\3\2\2\2\u00ea\u00e8\3\2\2\2\u00eb\u00ed\3\2\2\2")
        buf.write("\u00ec\u00ee\t\5\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef\3")
        buf.write("\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\n")
        buf.write("\3\2\2\2\u00f1\u00f2\t\6\2\2\u00f2\f\3\2\2\2\u00f3\u00f5")
        buf.write("\5\13\6\2\u00f4\u00f6\t\7\2\2\u00f5\u00f4\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f8\3\2\2\2\u00f7\u00f9\5\3\2\2")
        buf.write("\u00f8\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8\3")
        buf.write("\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\16\3\2\2\2\u00fc\u00fe")
        buf.write("\t\b\2\2\u00fd\u00fc\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u0102\b\b\2\2\u0102\20\3\2\2\2\u0103\u0104\7,\2")
        buf.write("\2\u0104\u0105\7,\2\2\u0105\u0109\3\2\2\2\u0106\u0108")
        buf.write("\13\2\2\2\u0107\u0106\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u010c\3\2\2\2")
        buf.write("\u010b\u0109\3\2\2\2\u010c\u010d\7,\2\2\u010d\u010e\7")
        buf.write(",\2\2\u010e\u010f\3\2\2\2\u010f\u0110\b\t\2\2\u0110\22")
        buf.write("\3\2\2\2\u0111\u0112\7H\2\2\u0112\u0113\7w\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7e\2\2\u0115\u0116\7v\2\2\u0116\u0117")
        buf.write("\7k\2\2\u0117\u0118\7q\2\2\u0118\u0119\7p\2\2\u0119\24")
        buf.write("\3\2\2\2\u011a\u011b\7R\2\2\u011b\u011c\7c\2\2\u011c\u011d")
        buf.write("\7t\2\2\u011d\u011e\7c\2\2\u011e\u011f\7o\2\2\u011f\u0120")
        buf.write("\7g\2\2\u0120\u0121\7v\2\2\u0121\u0122\7g\2\2\u0122\u0123")
        buf.write("\7t\2\2\u0123\26\3\2\2\2\u0124\u0125\7D\2\2\u0125\u0126")
        buf.write("\7q\2\2\u0126\u0127\7f\2\2\u0127\u0128\7{\2\2\u0128\30")
        buf.write("\3\2\2\2\u0129\u012a\7G\2\2\u012a\u012b\7p\2\2\u012b\u012c")
        buf.write("\7f\2\2\u012c\u012d\7D\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7f\2\2\u012f\u0130\7{\2\2\u0130\32\3\2\2\2\u0131\u0132")
        buf.write("\7K\2\2\u0132\u0133\7h\2\2\u0133\34\3\2\2\2\u0134\u0135")
        buf.write("\7V\2\2\u0135\u0136\5\u00a9U\2\u0136\u0137\5\u00a3R\2")
        buf.write("\u0137\u0138\5\u00b5[\2\u0138\36\3\2\2\2\u0139\u013a\7")
        buf.write("G\2\2\u013a\u013b\5\u00b1Y\2\u013b\u013c\5\u00bf`\2\u013c")
        buf.write("\u013d\5\u00a3R\2\u013d\u013e\5\u00abV\2\u013e\u013f\5")
        buf.write("\u00a5S\2\u013f \3\2\2\2\u0140\u0141\7G\2\2\u0141\u0142")
        buf.write("\5\u00b1Y\2\u0142\u0143\5\u00bf`\2\u0143\u0144\5\u00a3")
        buf.write("R\2\u0144\"\3\2\2\2\u0145\u0146\7G\2\2\u0146\u0147\5\u00b5")
        buf.write("[\2\u0147\u0148\5\u00a1Q\2\u0148\u0149\5\u00abV\2\u0149")
        buf.write("\u014a\5\u00a5S\2\u014a$\3\2\2\2\u014b\u014c\7H\2\2\u014c")
        buf.write("\u014d\5\u00b7\\\2\u014d\u014e\5\u00bd_\2\u014e&\3\2\2")
        buf.write("\2\u014f\u0150\7G\2\2\u0150\u0151\5\u00b5[\2\u0151\u0152")
        buf.write("\5\u00a1Q\2\u0152\u0153\5\u00a5S\2\u0153\u0154\5\u00b7")
        buf.write("\\\2\u0154\u0155\5\u00bd_\2\u0155(\3\2\2\2\u0156\u0157")
        buf.write("\7F\2\2\u0157\u0158\5\u00b7\\\2\u0158*\3\2\2\2\u0159\u015a")
        buf.write("\7G\2\2\u015a\u015b\5\u00b5[\2\u015b\u015c\5\u00a1Q\2")
        buf.write("\u015c\u015d\5\u00a1Q\2\u015d\u015e\5\u00b7\\\2\u015e")
        buf.write(",\3\2\2\2\u015f\u0160\7Y\2\2\u0160\u0161\5\u00a9U\2\u0161")
        buf.write("\u0162\5\u00abV\2\u0162\u0163\5\u00b1Y\2\u0163\u0164\5")
        buf.write("\u00a3R\2\u0164.\3\2\2\2\u0165\u0166\7G\2\2\u0166\u0167")
        buf.write("\5\u00b5[\2\u0167\u0168\5\u00a1Q\2\u0168\u0169\5\u00c7")
        buf.write("d\2\u0169\u016a\5\u00a9U\2\u016a\u016b\5\u00abV\2\u016b")
        buf.write("\u016c\5\u00b1Y\2\u016c\u016d\5\u00a3R\2\u016d\60\3\2")
        buf.write("\2\2\u016e\u016f\7T\2\2\u016f\u0170\5\u00a3R\2\u0170\u0171")
        buf.write("\5\u00c1a\2\u0171\u0172\5\u00c3b\2\u0172\u0173\5\u00bd")
        buf.write("_\2\u0173\u0174\5\u00b5[\2\u0174\62\3\2\2\2\u0175\u0176")
        buf.write("\7D\2\2\u0176\u0177\5\u00bd_\2\u0177\u0178\5\u00a3R\2")
        buf.write("\u0178\u0179\5\u009bN\2\u0179\u017a\5\u00afX\2\u017a\64")
        buf.write("\3\2\2\2\u017b\u017c\7E\2\2\u017c\u017d\5\u00b7\\\2\u017d")
        buf.write("\u017e\5\u00b5[\2\u017e\u017f\5\u00c1a\2\u017f\u0180\5")
        buf.write("\u00abV\2\u0180\u0181\5\u00b5[\2\u0181\u0182\5\u00c3b")
        buf.write("\2\u0182\u0183\5\u00a3R\2\u0183\66\3\2\2\2\u0184\u0185")
        buf.write("\7V\2\2\u0185\u0186\5\u00bd_\2\u0186\u0187\5\u00c3b\2")
        buf.write("\u0187\u0188\5\u00a3R\2\u01888\3\2\2\2\u0189\u018a\7H")
        buf.write("\2\2\u018a\u018b\5\u009bN\2\u018b\u018c\5\u00b1Y\2\u018c")
        buf.write("\u018d\5\u00bf`\2\u018d\u018e\5\u00a3R\2\u018e:\3\2\2")
        buf.write("\2\u018f\u0190\7X\2\2\u0190\u0191\5\u009bN\2\u0191\u0192")
        buf.write("\5\u00bd_\2\u0192<\3\2\2\2\u0193\u0194\7#\2\2\u0194>\3")
        buf.write("\2\2\2\u0195\u0196\7(\2\2\u0196\u0197\7(\2\2\u0197@\3")
        buf.write("\2\2\2\u0198\u0199\7~\2\2\u0199\u019a\7~\2\2\u019aB\3")
        buf.write("\2\2\2\u019b\u019c\7-\2\2\u019cD\3\2\2\2\u019d\u019e\7")
        buf.write("/\2\2\u019eF\3\2\2\2\u019f\u01a0\7,\2\2\u01a0H\3\2\2\2")
        buf.write("\u01a1\u01a2\7^\2\2\u01a2J\3\2\2\2\u01a3\u01a4\7\'\2\2")
        buf.write("\u01a4L\3\2\2\2\u01a5\u01a6\5C\"\2\u01a6\u01a7\5\177@")
        buf.write("\2\u01a7N\3\2\2\2\u01a8\u01a9\5E#\2\u01a9\u01aa\5\177")
        buf.write("@\2\u01aaP\3\2\2\2\u01ab\u01ac\5G$\2\u01ac\u01ad\5\177")
        buf.write("@\2\u01adR\3\2\2\2\u01ae\u01af\5I%\2\u01af\u01b0\5\177")
        buf.write("@\2\u01b0T\3\2\2\2\u01b1\u01b2\7?\2\2\u01b2V\3\2\2\2\u01b3")
        buf.write("\u01b4\5U+\2\u01b4\u01b5\5U+\2\u01b5X\3\2\2\2\u01b6\u01b7")
        buf.write("\5=\37\2\u01b7\u01b8\5U+\2\u01b8Z\3\2\2\2\u01b9\u01ba")
        buf.write("\7>\2\2\u01ba\\\3\2\2\2\u01bb\u01bc\5[.\2\u01bc\u01bd")
        buf.write("\5U+\2\u01bd^\3\2\2\2\u01be\u01bf\7@\2\2\u01bf`\3\2\2")
        buf.write("\2\u01c0\u01c1\5_\60\2\u01c1\u01c2\5U+\2\u01c2b\3\2\2")
        buf.write("\2\u01c3\u01c4\5U+\2\u01c4\u01c5\7\61\2\2\u01c5\u01c6")
        buf.write("\5U+\2\u01c6d\3\2\2\2\u01c7\u01c8\5[.\2\u01c8\u01c9\5")
        buf.write("\177@\2\u01c9f\3\2\2\2\u01ca\u01cb\5[.\2\u01cb\u01cc\5")
        buf.write("U+\2\u01cc\u01cd\5\177@\2\u01cdh\3\2\2\2\u01ce\u01cf\5")
        buf.write("_\60\2\u01cf\u01d0\5\177@\2\u01d0j\3\2\2\2\u01d1\u01d2")
        buf.write("\5i\65\2\u01d2\u01d3\5U+\2\u01d3l\3\2\2\2\u01d4\u01d5")
        buf.write("\7*\2\2\u01d5n\3\2\2\2\u01d6\u01d7\7+\2\2\u01d7p\3\2\2")
        buf.write("\2\u01d8\u01d9\7}\2\2\u01d9r\3\2\2\2\u01da\u01db\7\177")
        buf.write("\2\2\u01dbt\3\2\2\2\u01dc\u01dd\7]\2\2\u01ddv\3\2\2\2")
        buf.write("\u01de\u01df\7_\2\2\u01dfx\3\2\2\2\u01e0\u01e1\7=\2\2")
        buf.write("\u01e1z\3\2\2\2\u01e2\u01e3\7<\2\2\u01e3|\3\2\2\2\u01e4")
        buf.write("\u01e5\7.\2\2\u01e5~\3\2\2\2\u01e6\u01e7\7\60\2\2\u01e7")
        buf.write("\u0080\3\2\2\2\u01e8\u01ec\5\5\3\2\u01e9\u01ec\5\7\4\2")
        buf.write("\u01ea\u01ec\5\t\5\2\u01eb\u01e8\3\2\2\2\u01eb\u01e9\3")
        buf.write("\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u0082\3\2\2\2\u01ed\u01ee")
        buf.write("\5\5\3\2\u01ee\u01f8\5\177@\2\u01ef\u01f9\5\r\7\2\u01f0")
        buf.write("\u01f2\5\3\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2")
        buf.write("\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6\3")
        buf.write("\2\2\2\u01f5\u01f7\5\r\7\2\u01f6\u01f5\3\2\2\2\u01f6\u01f7")
        buf.write("\3\2\2\2\u01f7\u01f9\3\2\2\2\u01f8\u01ef\3\2\2\2\u01f8")
        buf.write("\u01f1\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fe\3\2\2\2")
        buf.write("\u01fa\u01fb\5\5\3\2\u01fb\u01fc\5\r\7\2\u01fc\u01fe\3")
        buf.write("\2\2\2\u01fd\u01ed\3\2\2\2\u01fd\u01fa\3\2\2\2\u01fe\u0084")
        buf.write("\3\2\2\2\u01ff\u0202\5\67\34\2\u0200\u0202\59\35\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0200\3\2\2\2\u0202\u0086\3\2\2\2")
        buf.write("\u0203\u0207\t\t\2\2\u0204\u0206\t\n\2\2\u0205\u0204\3")
        buf.write("\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u0088\3\2\2\2\u0209\u0207\3\2\2\2\u020a")
        buf.write("\u020b\13\2\2\2\u020b\u020c\bE\3\2\u020c\u008a\3\2\2\2")
        buf.write("\u020d\u0211\7$\2\2\u020e\u0210\5\u0093J\2\u020f\u020e")
        buf.write("\3\2\2\2\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u0214\3\2\2\2\u0213\u0211\3\2\2\2")
        buf.write("\u0214\u0215\5\u0097L\2\u0215\u0216\bF\4\2\u0216\u008c")
        buf.write("\3\2\2\2\u0217\u021b\7$\2\2\u0218\u021a\5\u0093J\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u0220\t\13\2\2\u021f\u021e\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0221\u0222\bG\5\2\u0222\u008e\3\2\2\2")
        buf.write("\u0223\u0224\7,\2\2\u0224\u0225\7,\2\2\u0225\u0229\3\2")
        buf.write("\2\2\u0226\u0228\5\u0099M\2\u0227\u0226\3\2\2\2\u0228")
        buf.write("\u022b\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2")
        buf.write("\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022e\7")
        buf.write(",\2\2\u022d\u022c\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f")
        buf.write("\3\2\2\2\u022f\u0230\bH\6\2\u0230\u0090\3\2\2\2\u0231")
        buf.write("\u0235\7$\2\2\u0232\u0234\5\u0093J\2\u0233\u0232\3\2\2")
        buf.write("\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0236")
        buf.write("\3\2\2\2\u0236\u0238\3\2\2\2\u0237\u0235\3\2\2\2\u0238")
        buf.write("\u0239\7$\2\2\u0239\u023a\bI\7\2\u023a\u0092\3\2\2\2\u023b")
        buf.write("\u023e\n\f\2\2\u023c\u023e\5\u0095K\2\u023d\u023b\3\2")
        buf.write("\2\2\u023d\u023c\3\2\2\2\u023e\u0094\3\2\2\2\u023f\u0240")
        buf.write("\7^\2\2\u0240\u0244\t\r\2\2\u0241\u0242\7)\2\2\u0242\u0244")
        buf.write("\7$\2\2\u0243\u023f\3\2\2\2\u0243\u0241\3\2\2\2\u0244")
        buf.write("\u0096\3\2\2\2\u0245\u0246\7^\2\2\u0246\u0247\n\r\2\2")
        buf.write("\u0247\u0098\3\2\2\2\u0248\u0249\n\16\2\2\u0249\u009a")
        buf.write("\3\2\2\2\u024a\u024b\t\17\2\2\u024b\u009c\3\2\2\2\u024c")
        buf.write("\u024d\t\20\2\2\u024d\u009e\3\2\2\2\u024e\u024f\t\21\2")
        buf.write("\2\u024f\u00a0\3\2\2\2\u0250\u0251\t\22\2\2\u0251\u00a2")
        buf.write("\3\2\2\2\u0252\u0253\t\6\2\2\u0253\u00a4\3\2\2\2\u0254")
        buf.write("\u0255\t\23\2\2\u0255\u00a6\3\2\2\2\u0256\u0257\t\24\2")
        buf.write("\2\u0257\u00a8\3\2\2\2\u0258\u0259\t\25\2\2\u0259\u00aa")
        buf.write("\3\2\2\2\u025a\u025b\t\26\2\2\u025b\u00ac\3\2\2\2\u025c")
        buf.write("\u025d\t\27\2\2\u025d\u00ae\3\2\2\2\u025e\u025f\t\30\2")
        buf.write("\2\u025f\u00b0\3\2\2\2\u0260\u0261\t\31\2\2\u0261\u00b2")
        buf.write("\3\2\2\2\u0262\u0263\t\32\2\2\u0263\u00b4\3\2\2\2\u0264")
        buf.write("\u0265\t\33\2\2\u0265\u00b6\3\2\2\2\u0266\u0267\t\34\2")
        buf.write("\2\u0267\u00b8\3\2\2\2\u0268\u0269\t\35\2\2\u0269\u00ba")
        buf.write("\3\2\2\2\u026a\u026b\t\36\2\2\u026b\u00bc\3\2\2\2\u026c")
        buf.write("\u026d\t\37\2\2\u026d\u00be\3\2\2\2\u026e\u026f\t \2\2")
        buf.write("\u026f\u00c0\3\2\2\2\u0270\u0271\t!\2\2\u0271\u00c2\3")
        buf.write("\2\2\2\u0272\u0273\t\"\2\2\u0273\u00c4\3\2\2\2\u0274\u0275")
        buf.write("\t#\2\2\u0275\u00c6\3\2\2\2\u0276\u0277\t$\2\2\u0277\u00c8")
        buf.write("\3\2\2\2\u0278\u0279\t%\2\2\u0279\u00ca\3\2\2\2\u027a")
        buf.write("\u027b\t&\2\2\u027b\u00cc\3\2\2\2\u027c\u027d\t\'\2\2")
        buf.write("\u027d\u00ce\3\2\2\2\34\2\u00d6\u00d9\u00df\u00e4\u00ea")
        buf.write("\u00ef\u00f5\u00fa\u00ff\u0109\u01eb\u01f3\u01f6\u01f8")
        buf.write("\u01fd\u0201\u0207\u0211\u021b\u021f\u0229\u022d\u0235")
        buf.write("\u023d\u0243\b\b\2\2\3E\2\3F\3\3G\4\3H\5\3I\6")
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
            "'!'", "'&&'", "'||'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", 
            "'<'", "'>'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "':'", "','", "'.'" ]

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
                  "STRINGLIT", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "UNT_CMT", 
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z" ]

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
            	
     


