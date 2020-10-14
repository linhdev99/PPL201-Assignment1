# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u02ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\3\2\3\2\3\3\3")
        buf.write("\3\3\3\7\3\u00e1\n\3\f\3\16\3\u00e4\13\3\5\3\u00e6\n\3")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u00ec\n\4\3\4\6\4\u00ef\n\4\r\4\16")
        buf.write("\4\u00f0\3\5\3\5\3\5\3\5\5\5\u00f7\n\5\3\5\6\5\u00fa\n")
        buf.write("\5\r\5\16\5\u00fb\3\6\3\6\3\7\3\7\5\7\u0102\n\7\3\7\6")
        buf.write("\7\u0105\n\7\r\7\16\7\u0106\3\b\6\b\u010a\n\b\r\b\16\b")
        buf.write("\u010b\3\b\3\b\3\t\3\t\3\t\3\t\7\t\u0114\n\t\f\t\16\t")
        buf.write("\u0117\13\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\5\37\u01a3\n\37\3 \3 \3 \5 ")
        buf.write("\u01a8\n \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3")
        buf.write("$\3$\3$\3$\5$\u01bb\n$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\5.\u01d5\n")
        buf.write(".\3/\3/\3/\3/\3/\3/\5/\u01dd\n/\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u01f6\n")
        buf.write("\67\38\38\38\38\39\39\39\3:\3:\3:\3:\3;\3;\3;\3<\3<\3")
        buf.write("<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3")
        buf.write("E\3F\3F\3G\3G\5G\u021f\nG\3G\3G\3G\5G\u0224\nG\3H\3H\5")
        buf.write("H\u0228\nH\3H\6H\u022b\nH\rH\16H\u022c\3H\3H\3H\3H\6H")
        buf.write("\u0233\nH\rH\16H\u0234\3H\3H\3H\7H\u023a\nH\fH\16H\u023d")
        buf.write("\13H\3H\3H\6H\u0241\nH\rH\16H\u0242\3H\5H\u0246\nH\5H")
        buf.write("\u0248\nH\5H\u024a\nH\3I\3I\5I\u024e\nI\3J\3J\7J\u0252")
        buf.write("\nJ\fJ\16J\u0255\13J\3K\3K\3K\3L\3L\7L\u025c\nL\fL\16")
        buf.write("L\u025f\13L\3L\3L\3L\3M\3M\7M\u0266\nM\fM\16M\u0269\13")
        buf.write("M\3M\5M\u026c\nM\3M\3M\3N\3N\3N\3N\7N\u0274\nN\fN\16N")
        buf.write("\u0277\13N\3N\5N\u027a\nN\3N\3N\3O\3O\7O\u0280\nO\fO\16")
        buf.write("O\u0283\13O\3O\3O\3O\3P\3P\5P\u028a\nP\3Q\3Q\3Q\3Q\5Q")
        buf.write("\u0290\nQ\3R\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3")
        buf.write("X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3")
        buf.write("a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3f\3g\3g\3h\3h\3i\3i\3")
        buf.write("j\3j\3k\3k\3l\3l\3m\3m\3\u0115\2n\3\2\5\2\7\2\t\2\13\2")
        buf.write("\r\2\17\3\21\4\23\5\25\6\27\7\31\b\33\t\35\n\37\13!\f")
        buf.write("#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279")
        buf.write("\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)")
        buf.write("]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177")
        buf.write(";\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\u008dB\u008f")
        buf.write("C\u0091D\u0093E\u0095F\u0097G\u0099H\u009bI\u009dJ\u009f")
        buf.write("\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad")
        buf.write("\2\u00af\2\u00b1\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb")
        buf.write("\2\u00bd\2\u00bf\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9")
        buf.write("\2\u00cb\2\u00cd\2\u00cf\2\u00d1\2\u00d3\2\u00d5\2\u00d7")
        buf.write("\2\u00d9\2\3\2(\3\2\62;\3\2\63;\4\2\62;CH\3\2\629\4\2")
        buf.write("GGgg\4\2--//\5\2\13\f\17\17\"\"\3\2c|\5\2\62;C\\c|\3\3")
        buf.write("\f\f\7\2\n\f\16\17$$))^^\t\2))^^ddhhppttvv\3\2,,\4\2C")
        buf.write("Ccc\4\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4")
        buf.write("\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQq")
        buf.write("q\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2")
        buf.write("XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u02dc\2\17\3")
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
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\3\u00db\3\2\2\2\5\u00e5\3\2\2")
        buf.write("\2\7\u00eb\3\2\2\2\t\u00f6\3\2\2\2\13\u00fd\3\2\2\2\r")
        buf.write("\u00ff\3\2\2\2\17\u0109\3\2\2\2\21\u010f\3\2\2\2\23\u011d")
        buf.write("\3\2\2\2\25\u0122\3\2\2\2\27\u0128\3\2\2\2\31\u0131\3")
        buf.write("\2\2\2\33\u0134\3\2\2\2\35\u0139\3\2\2\2\37\u0140\3\2")
        buf.write("\2\2!\u0148\3\2\2\2#\u014e\3\2\2\2%\u0155\3\2\2\2\'\u015e")
        buf.write("\3\2\2\2)\u0162\3\2\2\2+\u016b\3\2\2\2-\u016e\3\2\2\2")
        buf.write("/\u0178\3\2\2\2\61\u017f\3\2\2\2\63\u0184\3\2\2\2\65\u0188")
        buf.write("\3\2\2\2\67\u018e\3\2\2\29\u0193\3\2\2\2;\u0199\3\2\2")
        buf.write("\2=\u01a2\3\2\2\2?\u01a7\3\2\2\2A\u01a9\3\2\2\2C\u01ab")
        buf.write("\3\2\2\2E\u01ae\3\2\2\2G\u01ba\3\2\2\2I\u01bc\3\2\2\2")
        buf.write("K\u01be\3\2\2\2M\u01c0\3\2\2\2O\u01c2\3\2\2\2Q\u01c4\3")
        buf.write("\2\2\2S\u01c6\3\2\2\2U\u01c9\3\2\2\2W\u01cc\3\2\2\2Y\u01cf")
        buf.write("\3\2\2\2[\u01d4\3\2\2\2]\u01dc\3\2\2\2_\u01de\3\2\2\2")
        buf.write("a\u01e0\3\2\2\2c\u01e3\3\2\2\2e\u01e6\3\2\2\2g\u01e8\3")
        buf.write("\2\2\2i\u01eb\3\2\2\2k\u01ed\3\2\2\2m\u01f5\3\2\2\2o\u01f7")
        buf.write("\3\2\2\2q\u01fb\3\2\2\2s\u01fe\3\2\2\2u\u0202\3\2\2\2")
        buf.write("w\u0205\3\2\2\2y\u0208\3\2\2\2{\u020a\3\2\2\2}\u020c\3")
        buf.write("\2\2\2\177\u020e\3\2\2\2\u0081\u0210\3\2\2\2\u0083\u0212")
        buf.write("\3\2\2\2\u0085\u0214\3\2\2\2\u0087\u0216\3\2\2\2\u0089")
        buf.write("\u0218\3\2\2\2\u008b\u021a\3\2\2\2\u008d\u021e\3\2\2\2")
        buf.write("\u008f\u0227\3\2\2\2\u0091\u024d\3\2\2\2\u0093\u024f\3")
        buf.write("\2\2\2\u0095\u0256\3\2\2\2\u0097\u0259\3\2\2\2\u0099\u0263")
        buf.write("\3\2\2\2\u009b\u026f\3\2\2\2\u009d\u027d\3\2\2\2\u009f")
        buf.write("\u0289\3\2\2\2\u00a1\u028f\3\2\2\2\u00a3\u0291\3\2\2\2")
        buf.write("\u00a5\u0294\3\2\2\2\u00a7\u0296\3\2\2\2\u00a9\u0298\3")
        buf.write("\2\2\2\u00ab\u029a\3\2\2\2\u00ad\u029c\3\2\2\2\u00af\u029e")
        buf.write("\3\2\2\2\u00b1\u02a0\3\2\2\2\u00b3\u02a2\3\2\2\2\u00b5")
        buf.write("\u02a4\3\2\2\2\u00b7\u02a6\3\2\2\2\u00b9\u02a8\3\2\2\2")
        buf.write("\u00bb\u02aa\3\2\2\2\u00bd\u02ac\3\2\2\2\u00bf\u02ae\3")
        buf.write("\2\2\2\u00c1\u02b0\3\2\2\2\u00c3\u02b2\3\2\2\2\u00c5\u02b4")
        buf.write("\3\2\2\2\u00c7\u02b6\3\2\2\2\u00c9\u02b8\3\2\2\2\u00cb")
        buf.write("\u02ba\3\2\2\2\u00cd\u02bc\3\2\2\2\u00cf\u02be\3\2\2\2")
        buf.write("\u00d1\u02c0\3\2\2\2\u00d3\u02c2\3\2\2\2\u00d5\u02c4\3")
        buf.write("\2\2\2\u00d7\u02c6\3\2\2\2\u00d9\u02c8\3\2\2\2\u00db\u00dc")
        buf.write("\t\2\2\2\u00dc\4\3\2\2\2\u00dd\u00e6\7\62\2\2\u00de\u00e2")
        buf.write("\t\3\2\2\u00df\u00e1\5\3\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\u00e4\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00dd\3")
        buf.write("\2\2\2\u00e5\u00de\3\2\2\2\u00e6\6\3\2\2\2\u00e7\u00e8")
        buf.write("\7\62\2\2\u00e8\u00ec\7z\2\2\u00e9\u00ea\7\62\2\2\u00ea")
        buf.write("\u00ec\7Z\2\2\u00eb\u00e7\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ee\3\2\2\2\u00ed\u00ef\t\4\2\2\u00ee\u00ed\3")
        buf.write("\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1")
        buf.write("\3\2\2\2\u00f1\b\3\2\2\2\u00f2\u00f3\7\62\2\2\u00f3\u00f7")
        buf.write("\7q\2\2\u00f4\u00f5\7\62\2\2\u00f5\u00f7\7Q\2\2\u00f6")
        buf.write("\u00f2\3\2\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00f9\3\2\2\2")
        buf.write("\u00f8\u00fa\t\5\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3")
        buf.write("\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\n")
        buf.write("\3\2\2\2\u00fd\u00fe\t\6\2\2\u00fe\f\3\2\2\2\u00ff\u0101")
        buf.write("\5\13\6\2\u0100\u0102\t\7\2\2\u0101\u0100\3\2\2\2\u0101")
        buf.write("\u0102\3\2\2\2\u0102\u0104\3\2\2\2\u0103\u0105\5\3\2\2")
        buf.write("\u0104\u0103\3\2\2\2\u0105\u0106\3\2\2\2\u0106\u0104\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107\16\3\2\2\2\u0108\u010a")
        buf.write("\t\b\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010e\b\b\2\2\u010e\20\3\2\2\2\u010f\u0110\7,\2")
        buf.write("\2\u0110\u0111\7,\2\2\u0111\u0115\3\2\2\2\u0112\u0114")
        buf.write("\13\2\2\2\u0113\u0112\3\2\2\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0116\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0118\3\2\2\2")
        buf.write("\u0117\u0115\3\2\2\2\u0118\u0119\7,\2\2\u0119\u011a\7")
        buf.write(",\2\2\u011a\u011b\3\2\2\2\u011b\u011c\b\t\2\2\u011c\22")
        buf.write("\3\2\2\2\u011d\u011e\7D\2\2\u011e\u011f\5\u00c3b\2\u011f")
        buf.write("\u0120\5\u00adW\2\u0120\u0121\5\u00d7l\2\u0121\24\3\2")
        buf.write("\2\2\u0122\u0123\7D\2\2\u0123\u0124\5\u00c9e\2\u0124\u0125")
        buf.write("\5\u00afX\2\u0125\u0126\5\u00a7T\2\u0126\u0127\5\u00bb")
        buf.write("^\2\u0127\26\3\2\2\2\u0128\u0129\7E\2\2\u0129\u012a\5")
        buf.write("\u00c3b\2\u012a\u012b\5\u00c1a\2\u012b\u012c\5\u00cdg")
        buf.write("\2\u012c\u012d\5\u00b7\\\2\u012d\u012e\5\u00c1a\2\u012e")
        buf.write("\u012f\5\u00cfh\2\u012f\u0130\5\u00afX\2\u0130\30\3\2")
        buf.write("\2\2\u0131\u0132\7F\2\2\u0132\u0133\5\u00c3b\2\u0133\32")
        buf.write("\3\2\2\2\u0134\u0135\7G\2\2\u0135\u0136\5\u00bd_\2\u0136")
        buf.write("\u0137\5\u00cbf\2\u0137\u0138\5\u00afX\2\u0138\34\3\2")
        buf.write("\2\2\u0139\u013a\7G\2\2\u013a\u013b\5\u00bd_\2\u013b\u013c")
        buf.write("\5\u00cbf\2\u013c\u013d\5\u00afX\2\u013d\u013e\5\u00b7")
        buf.write("\\\2\u013e\u013f\5\u00b1Y\2\u013f\36\3\2\2\2\u0140\u0141")
        buf.write("\7G\2\2\u0141\u0142\5\u00c1a\2\u0142\u0143\5\u00adW\2")
        buf.write("\u0143\u0144\5\u00a9U\2\u0144\u0145\5\u00c3b\2\u0145\u0146")
        buf.write("\5\u00adW\2\u0146\u0147\5\u00d7l\2\u0147 \3\2\2\2\u0148")
        buf.write("\u0149\7G\2\2\u0149\u014a\5\u00c1a\2\u014a\u014b\5\u00ad")
        buf.write("W\2\u014b\u014c\5\u00b7\\\2\u014c\u014d\5\u00b1Y\2\u014d")
        buf.write("\"\3\2\2\2\u014e\u014f\7G\2\2\u014f\u0150\5\u00c1a\2\u0150")
        buf.write("\u0151\5\u00adW\2\u0151\u0152\5\u00b1Y\2\u0152\u0153\5")
        buf.write("\u00c3b\2\u0153\u0154\5\u00c9e\2\u0154$\3\2\2\2\u0155")
        buf.write("\u0156\7G\2\2\u0156\u0157\5\u00c1a\2\u0157\u0158\5\u00ad")
        buf.write("W\2\u0158\u0159\5\u00d3j\2\u0159\u015a\5\u00b5[\2\u015a")
        buf.write("\u015b\5\u00b7\\\2\u015b\u015c\5\u00bd_\2\u015c\u015d")
        buf.write("\5\u00afX\2\u015d&\3\2\2\2\u015e\u015f\7H\2\2\u015f\u0160")
        buf.write("\5\u00c3b\2\u0160\u0161\5\u00c9e\2\u0161(\3\2\2\2\u0162")
        buf.write("\u0163\7H\2\2\u0163\u0164\5\u00cfh\2\u0164\u0165\5\u00c1")
        buf.write("a\2\u0165\u0166\5\u00abV\2\u0166\u0167\5\u00cdg\2\u0167")
        buf.write("\u0168\5\u00b7\\\2\u0168\u0169\5\u00c3b\2\u0169\u016a")
        buf.write("\5\u00c1a\2\u016a*\3\2\2\2\u016b\u016c\7K\2\2\u016c\u016d")
        buf.write("\5\u00b1Y\2\u016d,\3\2\2\2\u016e\u016f\7R\2\2\u016f\u0170")
        buf.write("\5\u00a7T\2\u0170\u0171\5\u00c9e\2\u0171\u0172\5\u00a7")
        buf.write("T\2\u0172\u0173\5\u00bf`\2\u0173\u0174\5\u00afX\2\u0174")
        buf.write("\u0175\5\u00cdg\2\u0175\u0176\5\u00afX\2\u0176\u0177\5")
        buf.write("\u00c9e\2\u0177.\3\2\2\2\u0178\u0179\7T\2\2\u0179\u017a")
        buf.write("\5\u00afX\2\u017a\u017b\5\u00cdg\2\u017b\u017c\5\u00cf")
        buf.write("h\2\u017c\u017d\5\u00c9e\2\u017d\u017e\5\u00c1a\2\u017e")
        buf.write("\60\3\2\2\2\u017f\u0180\7V\2\2\u0180\u0181\5\u00b5[\2")
        buf.write("\u0181\u0182\5\u00afX\2\u0182\u0183\5\u00c1a\2\u0183\62")
        buf.write("\3\2\2\2\u0184\u0185\7X\2\2\u0185\u0186\5\u00a7T\2\u0186")
        buf.write("\u0187\5\u00c9e\2\u0187\64\3\2\2\2\u0188\u0189\7Y\2\2")
        buf.write("\u0189\u018a\5\u00b5[\2\u018a\u018b\5\u00b7\\\2\u018b")
        buf.write("\u018c\5\u00bd_\2\u018c\u018d\5\u00afX\2\u018d\66\3\2")
        buf.write("\2\2\u018e\u018f\7V\2\2\u018f\u0190\5\u00c9e\2\u0190\u0191")
        buf.write("\5\u00cfh\2\u0191\u0192\5\u00afX\2\u01928\3\2\2\2\u0193")
        buf.write("\u0194\7H\2\2\u0194\u0195\5\u00a7T\2\u0195\u0196\5\u00bd")
        buf.write("_\2\u0196\u0197\5\u00cbf\2\u0197\u0198\5\u00afX\2\u0198")
        buf.write(":\3\2\2\2\u0199\u019a\7G\2\2\u019a\u019b\5\u00c1a\2\u019b")
        buf.write("\u019c\5\u00adW\2\u019c\u019d\5\u00adW\2\u019d\u019e\5")
        buf.write("\u00c3b\2\u019e<\3\2\2\2\u019f\u01a3\5? \2\u01a0\u01a3")
        buf.write("\5G$\2\u01a1\u01a3\5[.\2\u01a2\u019f\3\2\2\2\u01a2\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3>\3\2\2\2\u01a4\u01a8")
        buf.write("\5A!\2\u01a5\u01a8\5C\"\2\u01a6\u01a8\5E#\2\u01a7\u01a4")
        buf.write("\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8")
        buf.write("@\3\2\2\2\u01a9\u01aa\7#\2\2\u01aaB\3\2\2\2\u01ab\u01ac")
        buf.write("\7(\2\2\u01ac\u01ad\7(\2\2\u01adD\3\2\2\2\u01ae\u01af")
        buf.write("\7~\2\2\u01af\u01b0\7~\2\2\u01b0F\3\2\2\2\u01b1\u01bb")
        buf.write("\5I%\2\u01b2\u01bb\5K&\2\u01b3\u01bb\5M\'\2\u01b4\u01bb")
        buf.write("\5O(\2\u01b5\u01bb\5Q)\2\u01b6\u01bb\5S*\2\u01b7\u01bb")
        buf.write("\5U+\2\u01b8\u01bb\5W,\2\u01b9\u01bb\5Y-\2\u01ba\u01b1")
        buf.write("\3\2\2\2\u01ba\u01b2\3\2\2\2\u01ba\u01b3\3\2\2\2\u01ba")
        buf.write("\u01b4\3\2\2\2\u01ba\u01b5\3\2\2\2\u01ba\u01b6\3\2\2\2")
        buf.write("\u01ba\u01b7\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3")
        buf.write("\2\2\2\u01bbH\3\2\2\2\u01bc\u01bd\7-\2\2\u01bdJ\3\2\2")
        buf.write("\2\u01be\u01bf\7/\2\2\u01bfL\3\2\2\2\u01c0\u01c1\7,\2")
        buf.write("\2\u01c1N\3\2\2\2\u01c2\u01c3\7^\2\2\u01c3P\3\2\2\2\u01c4")
        buf.write("\u01c5\7\'\2\2\u01c5R\3\2\2\2\u01c6\u01c7\5I%\2\u01c7")
        buf.write("\u01c8\5\u008bF\2\u01c8T\3\2\2\2\u01c9\u01ca\5K&\2\u01ca")
        buf.write("\u01cb\5\u008bF\2\u01cbV\3\2\2\2\u01cc\u01cd\5M\'\2\u01cd")
        buf.write("\u01ce\5\u008bF\2\u01ceX\3\2\2\2\u01cf\u01d0\5O(\2\u01d0")
        buf.write("\u01d1\5\u008bF\2\u01d1Z\3\2\2\2\u01d2\u01d5\5]/\2\u01d3")
        buf.write("\u01d5\5m\67\2\u01d4\u01d2\3\2\2\2\u01d4\u01d3\3\2\2\2")
        buf.write("\u01d5\\\3\2\2\2\u01d6\u01dd\5a\61\2\u01d7\u01dd\5c\62")
        buf.write("\2\u01d8\u01dd\5e\63\2\u01d9\u01dd\5g\64\2\u01da\u01dd")
        buf.write("\5i\65\2\u01db\u01dd\5k\66\2\u01dc\u01d6\3\2\2\2\u01dc")
        buf.write("\u01d7\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01d9\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd^\3\2\2")
        buf.write("\2\u01de\u01df\7?\2\2\u01df`\3\2\2\2\u01e0\u01e1\5_\60")
        buf.write("\2\u01e1\u01e2\5_\60\2\u01e2b\3\2\2\2\u01e3\u01e4\5A!")
        buf.write("\2\u01e4\u01e5\5_\60\2\u01e5d\3\2\2\2\u01e6\u01e7\7>\2")
        buf.write("\2\u01e7f\3\2\2\2\u01e8\u01e9\5e\63\2\u01e9\u01ea\5_\60")
        buf.write("\2\u01eah\3\2\2\2\u01eb\u01ec\7@\2\2\u01ecj\3\2\2\2\u01ed")
        buf.write("\u01ee\5i\65\2\u01ee\u01ef\5_\60\2\u01efl\3\2\2\2\u01f0")
        buf.write("\u01f6\5o8\2\u01f1\u01f6\5q9\2\u01f2\u01f6\5s:\2\u01f3")
        buf.write("\u01f6\5u;\2\u01f4\u01f6\5w<\2\u01f5\u01f0\3\2\2\2\u01f5")
        buf.write("\u01f1\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f4\3\2\2\2\u01f6n\3\2\2\2\u01f7\u01f8\5_\60")
        buf.write("\2\u01f8\u01f9\7\61\2\2\u01f9\u01fa\5_\60\2\u01fap\3\2")
        buf.write("\2\2\u01fb\u01fc\5e\63\2\u01fc\u01fd\5\u008bF\2\u01fd")
        buf.write("r\3\2\2\2\u01fe\u01ff\5e\63\2\u01ff\u0200\5_\60\2\u0200")
        buf.write("\u0201\5\u008bF\2\u0201t\3\2\2\2\u0202\u0203\5i\65\2\u0203")
        buf.write("\u0204\5\u008bF\2\u0204v\3\2\2\2\u0205\u0206\5u;\2\u0206")
        buf.write("\u0207\5_\60\2\u0207x\3\2\2\2\u0208\u0209\7*\2\2\u0209")
        buf.write("z\3\2\2\2\u020a\u020b\7+\2\2\u020b|\3\2\2\2\u020c\u020d")
        buf.write("\7}\2\2\u020d~\3\2\2\2\u020e\u020f\7\177\2\2\u020f\u0080")
        buf.write("\3\2\2\2\u0210\u0211\7]\2\2\u0211\u0082\3\2\2\2\u0212")
        buf.write("\u0213\7_\2\2\u0213\u0084\3\2\2\2\u0214\u0215\7=\2\2\u0215")
        buf.write("\u0086\3\2\2\2\u0216\u0217\7<\2\2\u0217\u0088\3\2\2\2")
        buf.write("\u0218\u0219\7.\2\2\u0219\u008a\3\2\2\2\u021a\u021b\7")
        buf.write("\60\2\2\u021b\u008c\3\2\2\2\u021c\u021f\5I%\2\u021d\u021f")
        buf.write("\5K&\2\u021e\u021c\3\2\2\2\u021e\u021d\3\2\2\2\u021e\u021f")
        buf.write("\3\2\2\2\u021f\u0223\3\2\2\2\u0220\u0224\5\5\3\2\u0221")
        buf.write("\u0224\5\7\4\2\u0222\u0224\5\t\5\2\u0223\u0220\3\2\2\2")
        buf.write("\u0223\u0221\3\2\2\2\u0223\u0222\3\2\2\2\u0224\u008e\3")
        buf.write("\2\2\2\u0225\u0228\5I%\2\u0226\u0228\5K&\2\u0227\u0225")
        buf.write("\3\2\2\2\u0227\u0226\3\2\2\2\u0227\u0228\3\2\2\2\u0228")
        buf.write("\u0249\3\2\2\2\u0229\u022b\5\3\2\2\u022a\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3")
        buf.write("\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\5\u008bF\2\u022f")
        buf.write("\u0230\5\r\7\2\u0230\u024a\3\2\2\2\u0231\u0233\5\3\2\2")
        buf.write("\u0232\u0231\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0234\u0235\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0237")
        buf.write("\5\r\7\2\u0237\u024a\3\2\2\2\u0238\u023a\5\3\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023a\u023d\3\2\2\2\u023b\u0239\3\2\2\2")
        buf.write("\u023b\u023c\3\2\2\2\u023c\u023e\3\2\2\2\u023d\u023b\3")
        buf.write("\2\2\2\u023e\u0247\5\u008bF\2\u023f\u0241\5\3\2\2\u0240")
        buf.write("\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2")
        buf.write("\u0242\u0243\3\2\2\2\u0243\u0245\3\2\2\2\u0244\u0246\5")
        buf.write("\r\7\2\u0245\u0244\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0248")
        buf.write("\3\2\2\2\u0247\u0240\3\2\2\2\u0247\u0248\3\2\2\2\u0248")
        buf.write("\u024a\3\2\2\2\u0249\u022a\3\2\2\2\u0249\u0232\3\2\2\2")
        buf.write("\u0249\u023b\3\2\2\2\u024a\u0090\3\2\2\2\u024b\u024e\5")
        buf.write("\67\34\2\u024c\u024e\59\35\2\u024d\u024b\3\2\2\2\u024d")
        buf.write("\u024c\3\2\2\2\u024e\u0092\3\2\2\2\u024f\u0253\t\t\2\2")
        buf.write("\u0250\u0252\t\n\2\2\u0251\u0250\3\2\2\2\u0252\u0255\3")
        buf.write("\2\2\2\u0253\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0094")
        buf.write("\3\2\2\2\u0255\u0253\3\2\2\2\u0256\u0257\13\2\2\2\u0257")
        buf.write("\u0258\bK\3\2\u0258\u0096\3\2\2\2\u0259\u025d\7$\2\2\u025a")
        buf.write("\u025c\5\u009fP\2\u025b\u025a\3\2\2\2\u025c\u025f\3\2")
        buf.write("\2\2\u025d\u025b\3\2\2\2\u025d\u025e\3\2\2\2\u025e\u0260")
        buf.write("\3\2\2\2\u025f\u025d\3\2\2\2\u0260\u0261\5\u00a3R\2\u0261")
        buf.write("\u0262\bL\4\2\u0262\u0098\3\2\2\2\u0263\u0267\7$\2\2\u0264")
        buf.write("\u0266\5\u009fP\2\u0265\u0264\3\2\2\2\u0266\u0269\3\2")
        buf.write("\2\2\u0267\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u026b")
        buf.write("\3\2\2\2\u0269\u0267\3\2\2\2\u026a\u026c\t\13\2\2\u026b")
        buf.write("\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u026e\bM\5\2")
        buf.write("\u026e\u009a\3\2\2\2\u026f\u0270\7,\2\2\u0270\u0271\7")
        buf.write(",\2\2\u0271\u0275\3\2\2\2\u0272\u0274\5\u00a5S\2\u0273")
        buf.write("\u0272\3\2\2\2\u0274\u0277\3\2\2\2\u0275\u0273\3\2\2\2")
        buf.write("\u0275\u0276\3\2\2\2\u0276\u0279\3\2\2\2\u0277\u0275\3")
        buf.write("\2\2\2\u0278\u027a\7,\2\2\u0279\u0278\3\2\2\2\u0279\u027a")
        buf.write("\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u027c\bN\6\2\u027c")
        buf.write("\u009c\3\2\2\2\u027d\u0281\7$\2\2\u027e\u0280\5\u009f")
        buf.write("P\2\u027f\u027e\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f")
        buf.write("\3\2\2\2\u0281\u0282\3\2\2\2\u0282\u0284\3\2\2\2\u0283")
        buf.write("\u0281\3\2\2\2\u0284\u0285\7$\2\2\u0285\u0286\bO\7\2\u0286")
        buf.write("\u009e\3\2\2\2\u0287\u028a\n\f\2\2\u0288\u028a\5\u00a1")
        buf.write("Q\2\u0289\u0287\3\2\2\2\u0289\u0288\3\2\2\2\u028a\u00a0")
        buf.write("\3\2\2\2\u028b\u028c\7^\2\2\u028c\u0290\t\r\2\2\u028d")
        buf.write("\u028e\7)\2\2\u028e\u0290\7$\2\2\u028f\u028b\3\2\2\2\u028f")
        buf.write("\u028d\3\2\2\2\u0290\u00a2\3\2\2\2\u0291\u0292\7^\2\2")
        buf.write("\u0292\u0293\n\r\2\2\u0293\u00a4\3\2\2\2\u0294\u0295\n")
        buf.write("\16\2\2\u0295\u00a6\3\2\2\2\u0296\u0297\t\17\2\2\u0297")
        buf.write("\u00a8\3\2\2\2\u0298\u0299\t\20\2\2\u0299\u00aa\3\2\2")
        buf.write("\2\u029a\u029b\t\21\2\2\u029b\u00ac\3\2\2\2\u029c\u029d")
        buf.write("\t\22\2\2\u029d\u00ae\3\2\2\2\u029e\u029f\t\6\2\2\u029f")
        buf.write("\u00b0\3\2\2\2\u02a0\u02a1\t\23\2\2\u02a1\u00b2\3\2\2")
        buf.write("\2\u02a2\u02a3\t\24\2\2\u02a3\u00b4\3\2\2\2\u02a4\u02a5")
        buf.write("\t\25\2\2\u02a5\u00b6\3\2\2\2\u02a6\u02a7\t\26\2\2\u02a7")
        buf.write("\u00b8\3\2\2\2\u02a8\u02a9\t\27\2\2\u02a9\u00ba\3\2\2")
        buf.write("\2\u02aa\u02ab\t\30\2\2\u02ab\u00bc\3\2\2\2\u02ac\u02ad")
        buf.write("\t\31\2\2\u02ad\u00be\3\2\2\2\u02ae\u02af\t\32\2\2\u02af")
        buf.write("\u00c0\3\2\2\2\u02b0\u02b1\t\33\2\2\u02b1\u00c2\3\2\2")
        buf.write("\2\u02b2\u02b3\t\34\2\2\u02b3\u00c4\3\2\2\2\u02b4\u02b5")
        buf.write("\t\35\2\2\u02b5\u00c6\3\2\2\2\u02b6\u02b7\t\36\2\2\u02b7")
        buf.write("\u00c8\3\2\2\2\u02b8\u02b9\t\37\2\2\u02b9\u00ca\3\2\2")
        buf.write("\2\u02ba\u02bb\t \2\2\u02bb\u00cc\3\2\2\2\u02bc\u02bd")
        buf.write("\t!\2\2\u02bd\u00ce\3\2\2\2\u02be\u02bf\t\"\2\2\u02bf")
        buf.write("\u00d0\3\2\2\2\u02c0\u02c1\t#\2\2\u02c1\u00d2\3\2\2\2")
        buf.write("\u02c2\u02c3\t$\2\2\u02c3\u00d4\3\2\2\2\u02c4\u02c5\t")
        buf.write("%\2\2\u02c5\u00d6\3\2\2\2\u02c6\u02c7\t&\2\2\u02c7\u00d8")
        buf.write("\3\2\2\2\u02c8\u02c9\t\'\2\2\u02c9\u00da\3\2\2\2\'\2\u00e2")
        buf.write("\u00e5\u00eb\u00f0\u00f6\u00fb\u0101\u0106\u010b\u0115")
        buf.write("\u01a2\u01a7\u01ba\u01d4\u01dc\u01f5\u021e\u0223\u0227")
        buf.write("\u022c\u0234\u023b\u0242\u0245\u0247\u0249\u024d\u0253")
        buf.write("\u025d\u0267\u026b\u0275\u0279\u0281\u0289\u028f\b\b\2")
        buf.write("\2\3K\2\3L\3\3M\4\3N\5\3O\6")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    BCMT = 2
    BODY = 3
    BREAK = 4
    CONTINUE = 5
    DO = 6
    ELSE = 7
    ELSEIF = 8
    ENDBODY = 9
    ENDIF = 10
    ENDFOR = 11
    ENDWHILE = 12
    FOR = 13
    FUNCTION = 14
    IF = 15
    PARAMETER = 16
    RETURN = 17
    THEN = 18
    VAR = 19
    WHILE = 20
    TRUE = 21
    FALSE = 22
    ENDDO = 23
    OPERATOR = 24
    BOOL_OPERATOR = 25
    NOT = 26
    AND = 27
    OR = 28
    ARITHMETIC_OPERATOR = 29
    ADD = 30
    SUB = 31
    MUL = 32
    DIV = 33
    MOD = 34
    ADDDOT = 35
    SUBDOT = 36
    MULDOT = 37
    DIVDOT = 38
    RELATIONAL_OPERATOR = 39
    RELATIONAL_OPERATOR_INT = 40
    EQ = 41
    EQINT = 42
    NEQINT = 43
    LTINT = 44
    LTEINT = 45
    GTINT = 46
    GTEINT = 47
    RELATIONAL_OPERATOR_FLOAT = 48
    NEQF = 49
    LTF = 50
    LTEF = 51
    GTF = 52
    GTEF = 53
    LP = 54
    RP = 55
    LCB = 56
    RCB = 57
    LSB = 58
    RSB = 59
    SEMI = 60
    COLON = 61
    COMMA = 62
    DOT = 63
    INTLIT = 64
    FLOATLIT = 65
    BOOLEANLIT = 66
    ID = 67
    ERROR_CHAR = 68
    ILLEGAL_ESCAPE = 69
    UNCLOSE_STRING = 70
    UNTERMINATED_COMMENT = 71
    STRINGLIT = 72

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'!'", "'&&'", "'||'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'='", 
            "'<'", "'>'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "':'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BCMT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
            "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
            "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
            "FALSE", "ENDDO", "OPERATOR", "BOOL_OPERATOR", "NOT", "AND", 
            "OR", "ARITHMETIC_OPERATOR", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", "RELATIONAL_OPERATOR", 
            "RELATIONAL_OPERATOR_INT", "EQ", "EQINT", "NEQINT", "LTINT", 
            "LTEINT", "GTINT", "GTEINT", "RELATIONAL_OPERATOR_FLOAT", "NEQF", 
            "LTF", "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", "RCB", "LSB", 
            "RSB", "SEMI", "COLON", "COMMA", "DOT", "INTLIT", "FLOATLIT", 
            "BOOLEANLIT", "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
            "UNTERMINATED_COMMENT", "STRINGLIT" ]

    ruleNames = [ "DIGIT", "DEC", "HEX", "OCT", "EXP", "EXPONENT", "WS", 
                  "BCMT", "BODY", "BREAK", "CONTINUE", "DO", "ELSE", "ELSEIF", 
                  "ENDBODY", "ENDIF", "ENDFOR", "ENDWHILE", "FOR", "FUNCTION", 
                  "IF", "PARAMETER", "RETURN", "THEN", "VAR", "WHILE", "TRUE", 
                  "FALSE", "ENDDO", "OPERATOR", "BOOL_OPERATOR", "NOT", 
                  "AND", "OR", "ARITHMETIC_OPERATOR", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "ADDDOT", "SUBDOT", "MULDOT", "DIVDOT", 
                  "RELATIONAL_OPERATOR", "RELATIONAL_OPERATOR_INT", "EQ", 
                  "EQINT", "NEQINT", "LTINT", "LTEINT", "GTINT", "GTEINT", 
                  "RELATIONAL_OPERATOR_FLOAT", "NEQF", "LTF", "LTEF", "GTF", 
                  "GTEF", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", 
                  "COLON", "COMMA", "DOT", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                  "ID", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                  "UNTERMINATED_COMMENT", "STRINGLIT", "STR_CHAR", "ESC_SEQ", 
                  "ESC_ILLEGAL", "UNT_CMT", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

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
            actions[73] = self.ERROR_CHAR_action 
            actions[74] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.UNTERMINATED_COMMENT_action 
            actions[77] = self.STRINGLIT_action 
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
            	
     


