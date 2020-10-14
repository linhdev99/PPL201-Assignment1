# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u02a1\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\3\2\3\2\3\3\3\3\3\3\7\3\u00dd")
        buf.write("\n\3\f\3\16\3\u00e0\13\3\5\3\u00e2\n\3\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u00e8\n\4\3\4\6\4\u00eb\n\4\r\4\16\4\u00ec\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u00f3\n\5\3\5\6\5\u00f6\n\5\r\5\16\5\u00f7")
        buf.write("\3\6\3\6\3\7\3\7\5\7\u00fe\n\7\3\7\6\7\u0101\n\7\r\7\16")
        buf.write("\7\u0102\3\b\6\b\u0106\n\b\r\b\16\b\u0107\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\7\t\u0110\n\t\f\t\16\t\u0113\13\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\5\37\u019f\n\37\3 \3 \3 \5 \u01a4\n \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01b7\n")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\5.\u01d1\n.\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u01d9\n/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u01f2\n\67\38\38\38\38\39\39\39\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\5G\u021b\nG\3")
        buf.write("G\3G\3G\5G\u0220\nG\3H\3H\5H\u0224\nH\3H\6H\u0227\nH\r")
        buf.write("H\16H\u0228\3H\3H\3H\3H\6H\u022f\nH\rH\16H\u0230\3H\3")
        buf.write("H\3H\7H\u0236\nH\fH\16H\u0239\13H\3H\3H\6H\u023d\nH\r")
        buf.write("H\16H\u023e\3H\5H\u0242\nH\5H\u0244\nH\5H\u0246\nH\3I")
        buf.write("\3I\5I\u024a\nI\3J\3J\7J\u024e\nJ\fJ\16J\u0251\13J\3J")
        buf.write("\3J\3K\3K\5K\u0257\nK\3L\3L\3L\3L\5L\u025d\nL\3M\3M\7")
        buf.write("M\u0261\nM\fM\16M\u0264\13M\3N\3N\3O\3O\3P\3P\3Q\3Q\3")
        buf.write("R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Z\3Z\3")
        buf.write("[\3[\3\\\3\\\3]\3]\3^\3^\3_\3_\3`\3`\3a\3a\3b\3b\3c\3")
        buf.write("c\3d\3d\3e\3e\3f\3f\3g\3g\3h\3h\3i\3i\3j\3j\3k\3k\3\u0111")
        buf.write("\2l\3\2\5\2\7\2\t\2\13\2\r\2\17\3\21\4\23\5\25\6\27\7")
        buf.write("\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61")
        buf.write("\24\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37")
        buf.write("I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64")
        buf.write("s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\u0093E\u0095\2\u0097\2\u0099")
        buf.write("F\u009bG\u009dH\u009fI\u00a1J\u00a3\2\u00a5\2\u00a7\2")
        buf.write("\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5")
        buf.write("\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf\2\u00c1\2\u00c3")
        buf.write("\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd\2\u00cf\2\u00d1")
        buf.write("\2\u00d3\2\u00d5\2\3\2&\3\2\62;\3\2\63;\4\2\62;CH\3\2")
        buf.write("\629\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\7\2\n\f\16\17")
        buf.write("$$))^^\t\2))^^ddhhppttvv\3\2c|\5\2\62;C\\c|\4\2CCcc\4")
        buf.write("\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKk")
        buf.write("k\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2")
        buf.write("RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4")
        buf.write("\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\2\u02b1\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\3\u00d7\3\2\2\2\5\u00e1\3\2\2")
        buf.write("\2\7\u00e7\3\2\2\2\t\u00f2\3\2\2\2\13\u00f9\3\2\2\2\r")
        buf.write("\u00fb\3\2\2\2\17\u0105\3\2\2\2\21\u010b\3\2\2\2\23\u0119")
        buf.write("\3\2\2\2\25\u011e\3\2\2\2\27\u0124\3\2\2\2\31\u012d\3")
        buf.write("\2\2\2\33\u0130\3\2\2\2\35\u0135\3\2\2\2\37\u013c\3\2")
        buf.write("\2\2!\u0144\3\2\2\2#\u014a\3\2\2\2%\u0151\3\2\2\2\'\u015a")
        buf.write("\3\2\2\2)\u015e\3\2\2\2+\u0167\3\2\2\2-\u016a\3\2\2\2")
        buf.write("/\u0174\3\2\2\2\61\u017b\3\2\2\2\63\u0180\3\2\2\2\65\u0184")
        buf.write("\3\2\2\2\67\u018a\3\2\2\29\u018f\3\2\2\2;\u0195\3\2\2")
        buf.write("\2=\u019e\3\2\2\2?\u01a3\3\2\2\2A\u01a5\3\2\2\2C\u01a7")
        buf.write("\3\2\2\2E\u01aa\3\2\2\2G\u01b6\3\2\2\2I\u01b8\3\2\2\2")
        buf.write("K\u01ba\3\2\2\2M\u01bc\3\2\2\2O\u01be\3\2\2\2Q\u01c0\3")
        buf.write("\2\2\2S\u01c2\3\2\2\2U\u01c5\3\2\2\2W\u01c8\3\2\2\2Y\u01cb")
        buf.write("\3\2\2\2[\u01d0\3\2\2\2]\u01d8\3\2\2\2_\u01da\3\2\2\2")
        buf.write("a\u01dc\3\2\2\2c\u01df\3\2\2\2e\u01e2\3\2\2\2g\u01e4\3")
        buf.write("\2\2\2i\u01e7\3\2\2\2k\u01e9\3\2\2\2m\u01f1\3\2\2\2o\u01f3")
        buf.write("\3\2\2\2q\u01f7\3\2\2\2s\u01fa\3\2\2\2u\u01fe\3\2\2\2")
        buf.write("w\u0201\3\2\2\2y\u0204\3\2\2\2{\u0206\3\2\2\2}\u0208\3")
        buf.write("\2\2\2\177\u020a\3\2\2\2\u0081\u020c\3\2\2\2\u0083\u020e")
        buf.write("\3\2\2\2\u0085\u0210\3\2\2\2\u0087\u0212\3\2\2\2\u0089")
        buf.write("\u0214\3\2\2\2\u008b\u0216\3\2\2\2\u008d\u021a\3\2\2\2")
        buf.write("\u008f\u0223\3\2\2\2\u0091\u0249\3\2\2\2\u0093\u024b\3")
        buf.write("\2\2\2\u0095\u0256\3\2\2\2\u0097\u025c\3\2\2\2\u0099\u025e")
        buf.write("\3\2\2\2\u009b\u0265\3\2\2\2\u009d\u0267\3\2\2\2\u009f")
        buf.write("\u0269\3\2\2\2\u00a1\u026b\3\2\2\2\u00a3\u026d\3\2\2\2")
        buf.write("\u00a5\u026f\3\2\2\2\u00a7\u0271\3\2\2\2\u00a9\u0273\3")
        buf.write("\2\2\2\u00ab\u0275\3\2\2\2\u00ad\u0277\3\2\2\2\u00af\u0279")
        buf.write("\3\2\2\2\u00b1\u027b\3\2\2\2\u00b3\u027d\3\2\2\2\u00b5")
        buf.write("\u027f\3\2\2\2\u00b7\u0281\3\2\2\2\u00b9\u0283\3\2\2\2")
        buf.write("\u00bb\u0285\3\2\2\2\u00bd\u0287\3\2\2\2\u00bf\u0289\3")
        buf.write("\2\2\2\u00c1\u028b\3\2\2\2\u00c3\u028d\3\2\2\2\u00c5\u028f")
        buf.write("\3\2\2\2\u00c7\u0291\3\2\2\2\u00c9\u0293\3\2\2\2\u00cb")
        buf.write("\u0295\3\2\2\2\u00cd\u0297\3\2\2\2\u00cf\u0299\3\2\2\2")
        buf.write("\u00d1\u029b\3\2\2\2\u00d3\u029d\3\2\2\2\u00d5\u029f\3")
        buf.write("\2\2\2\u00d7\u00d8\t\2\2\2\u00d8\4\3\2\2\2\u00d9\u00e2")
        buf.write("\7\62\2\2\u00da\u00de\t\3\2\2\u00db\u00dd\5\3\2\2\u00dc")
        buf.write("\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00de\u00df\3\2\2\2\u00df\u00e2\3\2\2\2\u00e0\u00de\3")
        buf.write("\2\2\2\u00e1\u00d9\3\2\2\2\u00e1\u00da\3\2\2\2\u00e2\6")
        buf.write("\3\2\2\2\u00e3\u00e4\7\62\2\2\u00e4\u00e8\7z\2\2\u00e5")
        buf.write("\u00e6\7\62\2\2\u00e6\u00e8\7Z\2\2\u00e7\u00e3\3\2\2\2")
        buf.write("\u00e7\u00e5\3\2\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00eb\t")
        buf.write("\4\2\2\u00ea\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\b\3\2\2\2\u00ee\u00ef")
        buf.write("\7\62\2\2\u00ef\u00f3\7q\2\2\u00f0\u00f1\7\62\2\2\u00f1")
        buf.write("\u00f3\7Q\2\2\u00f2\u00ee\3\2\2\2\u00f2\u00f0\3\2\2\2")
        buf.write("\u00f3\u00f5\3\2\2\2\u00f4\u00f6\t\5\2\2\u00f5\u00f4\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8")
        buf.write("\3\2\2\2\u00f8\n\3\2\2\2\u00f9\u00fa\t\6\2\2\u00fa\f\3")
        buf.write("\2\2\2\u00fb\u00fd\5\13\6\2\u00fc\u00fe\t\7\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2")
        buf.write("\u00ff\u0101\5\3\2\2\u0100\u00ff\3\2\2\2\u0101\u0102\3")
        buf.write("\2\2\2\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\16")
        buf.write("\3\2\2\2\u0104\u0106\t\b\2\2\u0105\u0104\3\2\2\2\u0106")
        buf.write("\u0107\3\2\2\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2")
        buf.write("\u0108\u0109\3\2\2\2\u0109\u010a\b\b\2\2\u010a\20\3\2")
        buf.write("\2\2\u010b\u010c\7,\2\2\u010c\u010d\7,\2\2\u010d\u0111")
        buf.write("\3\2\2\2\u010e\u0110\13\2\2\2\u010f\u010e\3\2\2\2\u0110")
        buf.write("\u0113\3\2\2\2\u0111\u0112\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115\7")
        buf.write(",\2\2\u0115\u0116\7,\2\2\u0116\u0117\3\2\2\2\u0117\u0118")
        buf.write("\b\t\2\2\u0118\22\3\2\2\2\u0119\u011a\7D\2\2\u011a\u011b")
        buf.write("\5\u00bf`\2\u011b\u011c\5\u00a9U\2\u011c\u011d\5\u00d3")
        buf.write("j\2\u011d\24\3\2\2\2\u011e\u011f\7D\2\2\u011f\u0120\5")
        buf.write("\u00c5c\2\u0120\u0121\5\u00abV\2\u0121\u0122\5\u00a3R")
        buf.write("\2\u0122\u0123\5\u00b7\\\2\u0123\26\3\2\2\2\u0124\u0125")
        buf.write("\7E\2\2\u0125\u0126\5\u00bf`\2\u0126\u0127\5\u00bd_\2")
        buf.write("\u0127\u0128\5\u00c9e\2\u0128\u0129\5\u00b3Z\2\u0129\u012a")
        buf.write("\5\u00bd_\2\u012a\u012b\5\u00cbf\2\u012b\u012c\5\u00ab")
        buf.write("V\2\u012c\30\3\2\2\2\u012d\u012e\7F\2\2\u012e\u012f\5")
        buf.write("\u00bf`\2\u012f\32\3\2\2\2\u0130\u0131\7G\2\2\u0131\u0132")
        buf.write("\5\u00b9]\2\u0132\u0133\5\u00c7d\2\u0133\u0134\5\u00ab")
        buf.write("V\2\u0134\34\3\2\2\2\u0135\u0136\7G\2\2\u0136\u0137\5")
        buf.write("\u00b9]\2\u0137\u0138\5\u00c7d\2\u0138\u0139\5\u00abV")
        buf.write("\2\u0139\u013a\5\u00b3Z\2\u013a\u013b\5\u00adW\2\u013b")
        buf.write("\36\3\2\2\2\u013c\u013d\7G\2\2\u013d\u013e\5\u00bd_\2")
        buf.write("\u013e\u013f\5\u00a9U\2\u013f\u0140\5\u00a5S\2\u0140\u0141")
        buf.write("\5\u00bf`\2\u0141\u0142\5\u00a9U\2\u0142\u0143\5\u00d3")
        buf.write("j\2\u0143 \3\2\2\2\u0144\u0145\7G\2\2\u0145\u0146\5\u00bd")
        buf.write("_\2\u0146\u0147\5\u00a9U\2\u0147\u0148\5\u00b3Z\2\u0148")
        buf.write("\u0149\5\u00adW\2\u0149\"\3\2\2\2\u014a\u014b\7G\2\2\u014b")
        buf.write("\u014c\5\u00bd_\2\u014c\u014d\5\u00a9U\2\u014d\u014e\5")
        buf.write("\u00adW\2\u014e\u014f\5\u00bf`\2\u014f\u0150\5\u00c5c")
        buf.write("\2\u0150$\3\2\2\2\u0151\u0152\7G\2\2\u0152\u0153\5\u00bd")
        buf.write("_\2\u0153\u0154\5\u00a9U\2\u0154\u0155\5\u00cfh\2\u0155")
        buf.write("\u0156\5\u00b1Y\2\u0156\u0157\5\u00b3Z\2\u0157\u0158\5")
        buf.write("\u00b9]\2\u0158\u0159\5\u00abV\2\u0159&\3\2\2\2\u015a")
        buf.write("\u015b\7H\2\2\u015b\u015c\5\u00bf`\2\u015c\u015d\5\u00c5")
        buf.write("c\2\u015d(\3\2\2\2\u015e\u015f\7H\2\2\u015f\u0160\5\u00cb")
        buf.write("f\2\u0160\u0161\5\u00bd_\2\u0161\u0162\5\u00a7T\2\u0162")
        buf.write("\u0163\5\u00c9e\2\u0163\u0164\5\u00b3Z\2\u0164\u0165\5")
        buf.write("\u00bf`\2\u0165\u0166\5\u00bd_\2\u0166*\3\2\2\2\u0167")
        buf.write("\u0168\7K\2\2\u0168\u0169\5\u00adW\2\u0169,\3\2\2\2\u016a")
        buf.write("\u016b\7R\2\2\u016b\u016c\5\u00a3R\2\u016c\u016d\5\u00c5")
        buf.write("c\2\u016d\u016e\5\u00a3R\2\u016e\u016f\5\u00bb^\2\u016f")
        buf.write("\u0170\5\u00abV\2\u0170\u0171\5\u00c9e\2\u0171\u0172\5")
        buf.write("\u00abV\2\u0172\u0173\5\u00c5c\2\u0173.\3\2\2\2\u0174")
        buf.write("\u0175\7T\2\2\u0175\u0176\5\u00abV\2\u0176\u0177\5\u00c9")
        buf.write("e\2\u0177\u0178\5\u00cbf\2\u0178\u0179\5\u00c5c\2\u0179")
        buf.write("\u017a\5\u00bd_\2\u017a\60\3\2\2\2\u017b\u017c\7V\2\2")
        buf.write("\u017c\u017d\5\u00b1Y\2\u017d\u017e\5\u00abV\2\u017e\u017f")
        buf.write("\5\u00bd_\2\u017f\62\3\2\2\2\u0180\u0181\7X\2\2\u0181")
        buf.write("\u0182\5\u00a3R\2\u0182\u0183\5\u00c5c\2\u0183\64\3\2")
        buf.write("\2\2\u0184\u0185\7Y\2\2\u0185\u0186\5\u00b1Y\2\u0186\u0187")
        buf.write("\5\u00b3Z\2\u0187\u0188\5\u00b9]\2\u0188\u0189\5\u00ab")
        buf.write("V\2\u0189\66\3\2\2\2\u018a\u018b\7V\2\2\u018b\u018c\5")
        buf.write("\u00c5c\2\u018c\u018d\5\u00cbf\2\u018d\u018e\5\u00abV")
        buf.write("\2\u018e8\3\2\2\2\u018f\u0190\7H\2\2\u0190\u0191\5\u00a3")
        buf.write("R\2\u0191\u0192\5\u00b9]\2\u0192\u0193\5\u00c7d\2\u0193")
        buf.write("\u0194\5\u00abV\2\u0194:\3\2\2\2\u0195\u0196\7G\2\2\u0196")
        buf.write("\u0197\5\u00bd_\2\u0197\u0198\5\u00a9U\2\u0198\u0199\5")
        buf.write("\u00a9U\2\u0199\u019a\5\u00bf`\2\u019a<\3\2\2\2\u019b")
        buf.write("\u019f\5? \2\u019c\u019f\5G$\2\u019d\u019f\5[.\2\u019e")
        buf.write("\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2")
        buf.write("\u019f>\3\2\2\2\u01a0\u01a4\5A!\2\u01a1\u01a4\5C\"\2\u01a2")
        buf.write("\u01a4\5E#\2\u01a3\u01a0\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3")
        buf.write("\u01a2\3\2\2\2\u01a4@\3\2\2\2\u01a5\u01a6\7#\2\2\u01a6")
        buf.write("B\3\2\2\2\u01a7\u01a8\7(\2\2\u01a8\u01a9\7(\2\2\u01a9")
        buf.write("D\3\2\2\2\u01aa\u01ab\7~\2\2\u01ab\u01ac\7~\2\2\u01ac")
        buf.write("F\3\2\2\2\u01ad\u01b7\5I%\2\u01ae\u01b7\5K&\2\u01af\u01b7")
        buf.write("\5M\'\2\u01b0\u01b7\5O(\2\u01b1\u01b7\5Q)\2\u01b2\u01b7")
        buf.write("\5S*\2\u01b3\u01b7\5U+\2\u01b4\u01b7\5W,\2\u01b5\u01b7")
        buf.write("\5Y-\2\u01b6\u01ad\3\2\2\2\u01b6\u01ae\3\2\2\2\u01b6\u01af")
        buf.write("\3\2\2\2\u01b6\u01b0\3\2\2\2\u01b6\u01b1\3\2\2\2\u01b6")
        buf.write("\u01b2\3\2\2\2\u01b6\u01b3\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b5\3\2\2\2\u01b7H\3\2\2\2\u01b8\u01b9\7-\2\2")
        buf.write("\u01b9J\3\2\2\2\u01ba\u01bb\7/\2\2\u01bbL\3\2\2\2\u01bc")
        buf.write("\u01bd\7,\2\2\u01bdN\3\2\2\2\u01be\u01bf\7^\2\2\u01bf")
        buf.write("P\3\2\2\2\u01c0\u01c1\7\'\2\2\u01c1R\3\2\2\2\u01c2\u01c3")
        buf.write("\5I%\2\u01c3\u01c4\5\u008bF\2\u01c4T\3\2\2\2\u01c5\u01c6")
        buf.write("\5K&\2\u01c6\u01c7\5\u008bF\2\u01c7V\3\2\2\2\u01c8\u01c9")
        buf.write("\5M\'\2\u01c9\u01ca\5\u008bF\2\u01caX\3\2\2\2\u01cb\u01cc")
        buf.write("\5O(\2\u01cc\u01cd\5\u008bF\2\u01cdZ\3\2\2\2\u01ce\u01d1")
        buf.write("\5]/\2\u01cf\u01d1\5m\67\2\u01d0\u01ce\3\2\2\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\\\3\2\2\2\u01d2\u01d9\5a\61\2\u01d3\u01d9")
        buf.write("\5c\62\2\u01d4\u01d9\5e\63\2\u01d5\u01d9\5g\64\2\u01d6")
        buf.write("\u01d9\5i\65\2\u01d7\u01d9\5k\66\2\u01d8\u01d2\3\2\2\2")
        buf.write("\u01d8\u01d3\3\2\2\2\u01d8\u01d4\3\2\2\2\u01d8\u01d5\3")
        buf.write("\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d7\3\2\2\2\u01d9^")
        buf.write("\3\2\2\2\u01da\u01db\7?\2\2\u01db`\3\2\2\2\u01dc\u01dd")
        buf.write("\5_\60\2\u01dd\u01de\5_\60\2\u01deb\3\2\2\2\u01df\u01e0")
        buf.write("\5A!\2\u01e0\u01e1\5_\60\2\u01e1d\3\2\2\2\u01e2\u01e3")
        buf.write("\7>\2\2\u01e3f\3\2\2\2\u01e4\u01e5\5e\63\2\u01e5\u01e6")
        buf.write("\5_\60\2\u01e6h\3\2\2\2\u01e7\u01e8\7@\2\2\u01e8j\3\2")
        buf.write("\2\2\u01e9\u01ea\5i\65\2\u01ea\u01eb\5_\60\2\u01ebl\3")
        buf.write("\2\2\2\u01ec\u01f2\5o8\2\u01ed\u01f2\5q9\2\u01ee\u01f2")
        buf.write("\5s:\2\u01ef\u01f2\5u;\2\u01f0\u01f2\5w<\2\u01f1\u01ec")
        buf.write("\3\2\2\2\u01f1\u01ed\3\2\2\2\u01f1\u01ee\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2n\3\2\2\2\u01f3")
        buf.write("\u01f4\5_\60\2\u01f4\u01f5\7\61\2\2\u01f5\u01f6\5_\60")
        buf.write("\2\u01f6p\3\2\2\2\u01f7\u01f8\5e\63\2\u01f8\u01f9\5\u008b")
        buf.write("F\2\u01f9r\3\2\2\2\u01fa\u01fb\5e\63\2\u01fb\u01fc\5_")
        buf.write("\60\2\u01fc\u01fd\5\u008bF\2\u01fdt\3\2\2\2\u01fe\u01ff")
        buf.write("\5i\65\2\u01ff\u0200\5\u008bF\2\u0200v\3\2\2\2\u0201\u0202")
        buf.write("\5u;\2\u0202\u0203\5_\60\2\u0203x\3\2\2\2\u0204\u0205")
        buf.write("\7*\2\2\u0205z\3\2\2\2\u0206\u0207\7+\2\2\u0207|\3\2\2")
        buf.write("\2\u0208\u0209\7}\2\2\u0209~\3\2\2\2\u020a\u020b\7\177")
        buf.write("\2\2\u020b\u0080\3\2\2\2\u020c\u020d\7]\2\2\u020d\u0082")
        buf.write("\3\2\2\2\u020e\u020f\7_\2\2\u020f\u0084\3\2\2\2\u0210")
        buf.write("\u0211\7=\2\2\u0211\u0086\3\2\2\2\u0212\u0213\7<\2\2\u0213")
        buf.write("\u0088\3\2\2\2\u0214\u0215\7.\2\2\u0215\u008a\3\2\2\2")
        buf.write("\u0216\u0217\7\60\2\2\u0217\u008c\3\2\2\2\u0218\u021b")
        buf.write("\5I%\2\u0219\u021b\5K&\2\u021a\u0218\3\2\2\2\u021a\u0219")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021f\3\2\2\2\u021c")
        buf.write("\u0220\5\5\3\2\u021d\u0220\5\7\4\2\u021e\u0220\5\t\5\2")
        buf.write("\u021f\u021c\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u021e\3")
        buf.write("\2\2\2\u0220\u008e\3\2\2\2\u0221\u0224\5I%\2\u0222\u0224")
        buf.write("\5K&\2\u0223\u0221\3\2\2\2\u0223\u0222\3\2\2\2\u0223\u0224")
        buf.write("\3\2\2\2\u0224\u0245\3\2\2\2\u0225\u0227\5\3\2\2\u0226")
        buf.write("\u0225\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229\u022a\3\2\2\2\u022a\u022b\5")
        buf.write("\u008bF\2\u022b\u022c\5\r\7\2\u022c\u0246\3\2\2\2\u022d")
        buf.write("\u022f\5\3\2\2\u022e\u022d\3\2\2\2\u022f\u0230\3\2\2\2")
        buf.write("\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0232\3")
        buf.write("\2\2\2\u0232\u0233\5\r\7\2\u0233\u0246\3\2\2\2\u0234\u0236")
        buf.write("\5\3\2\2\u0235\u0234\3\2\2\2\u0236\u0239\3\2\2\2\u0237")
        buf.write("\u0235\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u023a\3\2\2\2")
        buf.write("\u0239\u0237\3\2\2\2\u023a\u0243\5\u008bF\2\u023b\u023d")
        buf.write("\5\3\2\2\u023c\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0241\3\2\2\2")
        buf.write("\u0240\u0242\5\r\7\2\u0241\u0240\3\2\2\2\u0241\u0242\3")
        buf.write("\2\2\2\u0242\u0244\3\2\2\2\u0243\u023c\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0246\3\2\2\2\u0245\u0226\3\2\2\2\u0245")
        buf.write("\u022e\3\2\2\2\u0245\u0237\3\2\2\2\u0246\u0090\3\2\2\2")
        buf.write("\u0247\u024a\5\67\34\2\u0248\u024a\59\35\2\u0249\u0247")
        buf.write("\3\2\2\2\u0249\u0248\3\2\2\2\u024a\u0092\3\2\2\2\u024b")
        buf.write("\u024f\7$\2\2\u024c\u024e\5\u0095K\2\u024d\u024c\3\2\2")
        buf.write("\2\u024e\u0251\3\2\2\2\u024f\u024d\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u0252\3\2\2\2\u0251\u024f\3\2\2\2\u0252")
        buf.write("\u0253\7$\2\2\u0253\u0094\3\2\2\2\u0254\u0257\n\t\2\2")
        buf.write("\u0255\u0257\5\u0097L\2\u0256\u0254\3\2\2\2\u0256\u0255")
        buf.write("\3\2\2\2\u0257\u0096\3\2\2\2\u0258\u0259\7^\2\2\u0259")
        buf.write("\u025d\t\n\2\2\u025a\u025b\7)\2\2\u025b\u025d\7$\2\2\u025c")
        buf.write("\u0258\3\2\2\2\u025c\u025a\3\2\2\2\u025d\u0098\3\2\2\2")
        buf.write("\u025e\u0262\t\13\2\2\u025f\u0261\t\f\2\2\u0260\u025f")
        buf.write("\3\2\2\2\u0261\u0264\3\2\2\2\u0262\u0260\3\2\2\2\u0262")
        buf.write("\u0263\3\2\2\2\u0263\u009a\3\2\2\2\u0264\u0262\3\2\2\2")
        buf.write("\u0265\u0266\13\2\2\2\u0266\u009c\3\2\2\2\u0267\u0268")
        buf.write("\13\2\2\2\u0268\u009e\3\2\2\2\u0269\u026a\13\2\2\2\u026a")
        buf.write("\u00a0\3\2\2\2\u026b\u026c\13\2\2\2\u026c\u00a2\3\2\2")
        buf.write("\2\u026d\u026e\t\r\2\2\u026e\u00a4\3\2\2\2\u026f\u0270")
        buf.write("\t\16\2\2\u0270\u00a6\3\2\2\2\u0271\u0272\t\17\2\2\u0272")
        buf.write("\u00a8\3\2\2\2\u0273\u0274\t\20\2\2\u0274\u00aa\3\2\2")
        buf.write("\2\u0275\u0276\t\6\2\2\u0276\u00ac\3\2\2\2\u0277\u0278")
        buf.write("\t\21\2\2\u0278\u00ae\3\2\2\2\u0279\u027a\t\22\2\2\u027a")
        buf.write("\u00b0\3\2\2\2\u027b\u027c\t\23\2\2\u027c\u00b2\3\2\2")
        buf.write("\2\u027d\u027e\t\24\2\2\u027e\u00b4\3\2\2\2\u027f\u0280")
        buf.write("\t\25\2\2\u0280\u00b6\3\2\2\2\u0281\u0282\t\26\2\2\u0282")
        buf.write("\u00b8\3\2\2\2\u0283\u0284\t\27\2\2\u0284\u00ba\3\2\2")
        buf.write("\2\u0285\u0286\t\30\2\2\u0286\u00bc\3\2\2\2\u0287\u0288")
        buf.write("\t\31\2\2\u0288\u00be\3\2\2\2\u0289\u028a\t\32\2\2\u028a")
        buf.write("\u00c0\3\2\2\2\u028b\u028c\t\33\2\2\u028c\u00c2\3\2\2")
        buf.write("\2\u028d\u028e\t\34\2\2\u028e\u00c4\3\2\2\2\u028f\u0290")
        buf.write("\t\35\2\2\u0290\u00c6\3\2\2\2\u0291\u0292\t\36\2\2\u0292")
        buf.write("\u00c8\3\2\2\2\u0293\u0294\t\37\2\2\u0294\u00ca\3\2\2")
        buf.write("\2\u0295\u0296\t \2\2\u0296\u00cc\3\2\2\2\u0297\u0298")
        buf.write("\t!\2\2\u0298\u00ce\3\2\2\2\u0299\u029a\t\"\2\2\u029a")
        buf.write("\u00d0\3\2\2\2\u029b\u029c\t#\2\2\u029c\u00d2\3\2\2\2")
        buf.write("\u029d\u029e\t$\2\2\u029e\u00d4\3\2\2\2\u029f\u02a0\t")
        buf.write("%\2\2\u02a0\u00d6\3\2\2\2\"\2\u00de\u00e1\u00e7\u00ec")
        buf.write("\u00f2\u00f7\u00fd\u0102\u0107\u0111\u019e\u01a3\u01b6")
        buf.write("\u01d0\u01d8\u01f1\u021a\u021f\u0223\u0228\u0230\u0237")
        buf.write("\u023e\u0241\u0243\u0245\u0249\u024f\u0256\u025c\u0262")
        buf.write("\3\b\2\2")
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
    STRINGLIT = 67
    ID = 68
    ERROR_CHAR = 69
    UNCLOSE_STRING = 70
    ILLEGAL_ESCAPE = 71
    UNTERMINATED_COMMENT = 72

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
            "BOOLEANLIT", "STRINGLIT", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
                  "STRINGLIT", "STR_CHAR", "ESC_SEQ", "ID", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
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


