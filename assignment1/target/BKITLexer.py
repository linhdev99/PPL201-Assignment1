# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2J")
        buf.write("\u0297\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\3\2\3\2\3\3\3\3\3\3\7\3\u00db\n")
        buf.write("\3\f\3\16\3\u00de\13\3\5\3\u00e0\n\3\3\4\3\4\3\4\3\4\5")
        buf.write("\4\u00e6\n\4\3\4\6\4\u00e9\n\4\r\4\16\4\u00ea\3\5\3\5")
        buf.write("\3\5\3\5\5\5\u00f1\n\5\3\5\6\5\u00f4\n\5\r\5\16\5\u00f5")
        buf.write("\3\6\3\6\3\7\3\7\5\7\u00fc\n\7\3\7\6\7\u00ff\n\7\r\7\16")
        buf.write("\7\u0100\3\b\6\b\u0104\n\b\r\b\16\b\u0105\3\b\3\b\3\t")
        buf.write("\3\t\3\t\3\t\7\t\u010e\n\t\f\t\16\t\u0111\13\t\3\t\3\t")
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
        buf.write("\3\37\5\37\u019d\n\37\3 \3 \3 \5 \u01a2\n \3!\3!\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\5$\u01b5\n")
        buf.write("$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\5.\u01cf\n.\3/\3/\3/\3/\3/\3/\5")
        buf.write("/\u01d7\n/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u01f0\n\67\38\38\38\38\39\39\39\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3<\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3")
        buf.write("A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\5G\u0219\nG\3")
        buf.write("G\3G\3G\5G\u021e\nG\3H\3H\5H\u0222\nH\3H\6H\u0225\nH\r")
        buf.write("H\16H\u0226\3H\3H\3H\3H\6H\u022d\nH\rH\16H\u022e\3H\3")
        buf.write("H\3H\7H\u0234\nH\fH\16H\u0237\13H\3H\3H\6H\u023b\nH\r")
        buf.write("H\16H\u023c\3H\5H\u0240\nH\5H\u0242\nH\5H\u0244\nH\3I")
        buf.write("\3I\5I\u0248\nI\3J\3J\7J\u024c\nJ\fJ\16J\u024f\13J\3J")
        buf.write("\3J\3K\3K\3L\3L\7L\u0257\nL\fL\16L\u025a\13L\3M\3M\3N")
        buf.write("\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3")
        buf.write("W\3W\3X\3X\3Y\3Y\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3^\3^\3_\3")
        buf.write("_\3`\3`\3a\3a\3b\3b\3c\3c\3d\3d\3e\3e\3f\3f\3g\3g\3h\3")
        buf.write("h\3i\3i\3j\3j\3\u010f\2k\3\2\5\2\7\2\t\2\13\2\r\2\17\3")
        buf.write("\21\4\23\5\25\6\27\7\31\b\33\t\35\n\37\13!\f#\r%\16\'")
        buf.write("\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32")
        buf.write("?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g")
        buf.write("/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\u008dB\u008fC\u0091D\u0093")
        buf.write("E\u0095\2\u0097F\u0099G\u009bH\u009dI\u009fJ\u00a1\2\u00a3")
        buf.write("\2\u00a5\2\u00a7\2\u00a9\2\u00ab\2\u00ad\2\u00af\2\u00b1")
        buf.write("\2\u00b3\2\u00b5\2\u00b7\2\u00b9\2\u00bb\2\u00bd\2\u00bf")
        buf.write("\2\u00c1\2\u00c3\2\u00c5\2\u00c7\2\u00c9\2\u00cb\2\u00cd")
        buf.write("\2\u00cf\2\u00d1\2\u00d3\2\3\2%\3\2\62;\3\2\63;\4\2\62")
        buf.write(";CH\3\2\629\4\2GGgg\4\2--//\5\2\13\f\17\17\"\"\5\2\f\f")
        buf.write("\16\17$$\3\2c|\5\2\62;C\\c|\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMm")
        buf.write("m\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2")
        buf.write("TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4")
        buf.write("\2[[{{\4\2\\\\||\2\u02a6\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2")
        buf.write("\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2")
        buf.write("\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2")
        buf.write("\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2")
        buf.write("\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2")
        buf.write("\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3")
        buf.write("\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]")
        buf.write("\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2")
        buf.write("g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2")
        buf.write("\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2")
        buf.write("\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2")
        buf.write("\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2")
        buf.write("\2\3\u00d5\3\2\2\2\5\u00df\3\2\2\2\7\u00e5\3\2\2\2\t\u00f0")
        buf.write("\3\2\2\2\13\u00f7\3\2\2\2\r\u00f9\3\2\2\2\17\u0103\3\2")
        buf.write("\2\2\21\u0109\3\2\2\2\23\u0117\3\2\2\2\25\u011c\3\2\2")
        buf.write("\2\27\u0122\3\2\2\2\31\u012b\3\2\2\2\33\u012e\3\2\2\2")
        buf.write("\35\u0133\3\2\2\2\37\u013a\3\2\2\2!\u0142\3\2\2\2#\u0148")
        buf.write("\3\2\2\2%\u014f\3\2\2\2\'\u0158\3\2\2\2)\u015c\3\2\2\2")
        buf.write("+\u0165\3\2\2\2-\u0168\3\2\2\2/\u0172\3\2\2\2\61\u0179")
        buf.write("\3\2\2\2\63\u017e\3\2\2\2\65\u0182\3\2\2\2\67\u0188\3")
        buf.write("\2\2\29\u018d\3\2\2\2;\u0193\3\2\2\2=\u019c\3\2\2\2?\u01a1")
        buf.write("\3\2\2\2A\u01a3\3\2\2\2C\u01a5\3\2\2\2E\u01a8\3\2\2\2")
        buf.write("G\u01b4\3\2\2\2I\u01b6\3\2\2\2K\u01b8\3\2\2\2M\u01ba\3")
        buf.write("\2\2\2O\u01bc\3\2\2\2Q\u01be\3\2\2\2S\u01c0\3\2\2\2U\u01c3")
        buf.write("\3\2\2\2W\u01c6\3\2\2\2Y\u01c9\3\2\2\2[\u01ce\3\2\2\2")
        buf.write("]\u01d6\3\2\2\2_\u01d8\3\2\2\2a\u01da\3\2\2\2c\u01dd\3")
        buf.write("\2\2\2e\u01e0\3\2\2\2g\u01e2\3\2\2\2i\u01e5\3\2\2\2k\u01e7")
        buf.write("\3\2\2\2m\u01ef\3\2\2\2o\u01f1\3\2\2\2q\u01f5\3\2\2\2")
        buf.write("s\u01f8\3\2\2\2u\u01fc\3\2\2\2w\u01ff\3\2\2\2y\u0202\3")
        buf.write("\2\2\2{\u0204\3\2\2\2}\u0206\3\2\2\2\177\u0208\3\2\2\2")
        buf.write("\u0081\u020a\3\2\2\2\u0083\u020c\3\2\2\2\u0085\u020e\3")
        buf.write("\2\2\2\u0087\u0210\3\2\2\2\u0089\u0212\3\2\2\2\u008b\u0214")
        buf.write("\3\2\2\2\u008d\u0218\3\2\2\2\u008f\u0221\3\2\2\2\u0091")
        buf.write("\u0247\3\2\2\2\u0093\u0249\3\2\2\2\u0095\u0252\3\2\2\2")
        buf.write("\u0097\u0254\3\2\2\2\u0099\u025b\3\2\2\2\u009b\u025d\3")
        buf.write("\2\2\2\u009d\u025f\3\2\2\2\u009f\u0261\3\2\2\2\u00a1\u0263")
        buf.write("\3\2\2\2\u00a3\u0265\3\2\2\2\u00a5\u0267\3\2\2\2\u00a7")
        buf.write("\u0269\3\2\2\2\u00a9\u026b\3\2\2\2\u00ab\u026d\3\2\2\2")
        buf.write("\u00ad\u026f\3\2\2\2\u00af\u0271\3\2\2\2\u00b1\u0273\3")
        buf.write("\2\2\2\u00b3\u0275\3\2\2\2\u00b5\u0277\3\2\2\2\u00b7\u0279")
        buf.write("\3\2\2\2\u00b9\u027b\3\2\2\2\u00bb\u027d\3\2\2\2\u00bd")
        buf.write("\u027f\3\2\2\2\u00bf\u0281\3\2\2\2\u00c1\u0283\3\2\2\2")
        buf.write("\u00c3\u0285\3\2\2\2\u00c5\u0287\3\2\2\2\u00c7\u0289\3")
        buf.write("\2\2\2\u00c9\u028b\3\2\2\2\u00cb\u028d\3\2\2\2\u00cd\u028f")
        buf.write("\3\2\2\2\u00cf\u0291\3\2\2\2\u00d1\u0293\3\2\2\2\u00d3")
        buf.write("\u0295\3\2\2\2\u00d5\u00d6\t\2\2\2\u00d6\4\3\2\2\2\u00d7")
        buf.write("\u00e0\7\62\2\2\u00d8\u00dc\t\3\2\2\u00d9\u00db\5\3\2")
        buf.write("\2\u00da\u00d9\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00df\u00d7\3\2\2\2\u00df\u00d8\3\2\2\2")
        buf.write("\u00e0\6\3\2\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e6\7z\2")
        buf.write("\2\u00e3\u00e4\7\62\2\2\u00e4\u00e6\7Z\2\2\u00e5\u00e1")
        buf.write("\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\u00e8\3\2\2\2\u00e7")
        buf.write("\u00e9\t\4\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\b\3\2\2")
        buf.write("\2\u00ec\u00ed\7\62\2\2\u00ed\u00f1\7q\2\2\u00ee\u00ef")
        buf.write("\7\62\2\2\u00ef\u00f1\7Q\2\2\u00f0\u00ec\3\2\2\2\u00f0")
        buf.write("\u00ee\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f4\t\5\2\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\n\3\2\2\2\u00f7\u00f8")
        buf.write("\t\6\2\2\u00f8\f\3\2\2\2\u00f9\u00fb\5\13\6\2\u00fa\u00fc")
        buf.write("\t\7\2\2\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fe\3\2\2\2\u00fd\u00ff\5\3\2\2\u00fe\u00fd\3\2\2\2")
        buf.write("\u00ff\u0100\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3")
        buf.write("\2\2\2\u0101\16\3\2\2\2\u0102\u0104\t\b\2\2\u0103\u0102")
        buf.write("\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0108\b\b\2\2")
        buf.write("\u0108\20\3\2\2\2\u0109\u010a\7,\2\2\u010a\u010b\7,\2")
        buf.write("\2\u010b\u010f\3\2\2\2\u010c\u010e\13\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\u0111\3\2\2\2\u010f\u0110\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u010f\3\2\2\2")
        buf.write("\u0112\u0113\7,\2\2\u0113\u0114\7,\2\2\u0114\u0115\3\2")
        buf.write("\2\2\u0115\u0116\b\t\2\2\u0116\22\3\2\2\2\u0117\u0118")
        buf.write("\7D\2\2\u0118\u0119\5\u00bd_\2\u0119\u011a\5\u00a7T\2")
        buf.write("\u011a\u011b\5\u00d1i\2\u011b\24\3\2\2\2\u011c\u011d\7")
        buf.write("D\2\2\u011d\u011e\5\u00c3b\2\u011e\u011f\5\u00a9U\2\u011f")
        buf.write("\u0120\5\u00a1Q\2\u0120\u0121\5\u00b5[\2\u0121\26\3\2")
        buf.write("\2\2\u0122\u0123\7E\2\2\u0123\u0124\5\u00bd_\2\u0124\u0125")
        buf.write("\5\u00bb^\2\u0125\u0126\5\u00c7d\2\u0126\u0127\5\u00b1")
        buf.write("Y\2\u0127\u0128\5\u00bb^\2\u0128\u0129\5\u00c9e\2\u0129")
        buf.write("\u012a\5\u00a9U\2\u012a\30\3\2\2\2\u012b\u012c\7F\2\2")
        buf.write("\u012c\u012d\5\u00bd_\2\u012d\32\3\2\2\2\u012e\u012f\7")
        buf.write("G\2\2\u012f\u0130\5\u00b7\\\2\u0130\u0131\5\u00c5c\2\u0131")
        buf.write("\u0132\5\u00a9U\2\u0132\34\3\2\2\2\u0133\u0134\7G\2\2")
        buf.write("\u0134\u0135\5\u00b7\\\2\u0135\u0136\5\u00c5c\2\u0136")
        buf.write("\u0137\5\u00a9U\2\u0137\u0138\5\u00b1Y\2\u0138\u0139\5")
        buf.write("\u00abV\2\u0139\36\3\2\2\2\u013a\u013b\7G\2\2\u013b\u013c")
        buf.write("\5\u00bb^\2\u013c\u013d\5\u00a7T\2\u013d\u013e\5\u00a3")
        buf.write("R\2\u013e\u013f\5\u00bd_\2\u013f\u0140\5\u00a7T\2\u0140")
        buf.write("\u0141\5\u00d1i\2\u0141 \3\2\2\2\u0142\u0143\7G\2\2\u0143")
        buf.write("\u0144\5\u00bb^\2\u0144\u0145\5\u00a7T\2\u0145\u0146\5")
        buf.write("\u00b1Y\2\u0146\u0147\5\u00abV\2\u0147\"\3\2\2\2\u0148")
        buf.write("\u0149\7G\2\2\u0149\u014a\5\u00bb^\2\u014a\u014b\5\u00a7")
        buf.write("T\2\u014b\u014c\5\u00abV\2\u014c\u014d\5\u00bd_\2\u014d")
        buf.write("\u014e\5\u00c3b\2\u014e$\3\2\2\2\u014f\u0150\7G\2\2\u0150")
        buf.write("\u0151\5\u00bb^\2\u0151\u0152\5\u00a7T\2\u0152\u0153\5")
        buf.write("\u00cdg\2\u0153\u0154\5\u00afX\2\u0154\u0155\5\u00b1Y")
        buf.write("\2\u0155\u0156\5\u00b7\\\2\u0156\u0157\5\u00a9U\2\u0157")
        buf.write("&\3\2\2\2\u0158\u0159\7H\2\2\u0159\u015a\5\u00bd_\2\u015a")
        buf.write("\u015b\5\u00c3b\2\u015b(\3\2\2\2\u015c\u015d\7H\2\2\u015d")
        buf.write("\u015e\5\u00c9e\2\u015e\u015f\5\u00bb^\2\u015f\u0160\5")
        buf.write("\u00a5S\2\u0160\u0161\5\u00c7d\2\u0161\u0162\5\u00b1Y")
        buf.write("\2\u0162\u0163\5\u00bd_\2\u0163\u0164\5\u00bb^\2\u0164")
        buf.write("*\3\2\2\2\u0165\u0166\7K\2\2\u0166\u0167\5\u00abV\2\u0167")
        buf.write(",\3\2\2\2\u0168\u0169\7R\2\2\u0169\u016a\5\u00a1Q\2\u016a")
        buf.write("\u016b\5\u00c3b\2\u016b\u016c\5\u00a1Q\2\u016c\u016d\5")
        buf.write("\u00b9]\2\u016d\u016e\5\u00a9U\2\u016e\u016f\5\u00c7d")
        buf.write("\2\u016f\u0170\5\u00a9U\2\u0170\u0171\5\u00c3b\2\u0171")
        buf.write(".\3\2\2\2\u0172\u0173\7T\2\2\u0173\u0174\5\u00a9U\2\u0174")
        buf.write("\u0175\5\u00c7d\2\u0175\u0176\5\u00c9e\2\u0176\u0177\5")
        buf.write("\u00c3b\2\u0177\u0178\5\u00bb^\2\u0178\60\3\2\2\2\u0179")
        buf.write("\u017a\7V\2\2\u017a\u017b\5\u00afX\2\u017b\u017c\5\u00a9")
        buf.write("U\2\u017c\u017d\5\u00bb^\2\u017d\62\3\2\2\2\u017e\u017f")
        buf.write("\7X\2\2\u017f\u0180\5\u00a1Q\2\u0180\u0181\5\u00c3b\2")
        buf.write("\u0181\64\3\2\2\2\u0182\u0183\7Y\2\2\u0183\u0184\5\u00af")
        buf.write("X\2\u0184\u0185\5\u00b1Y\2\u0185\u0186\5\u00b7\\\2\u0186")
        buf.write("\u0187\5\u00a9U\2\u0187\66\3\2\2\2\u0188\u0189\7V\2\2")
        buf.write("\u0189\u018a\5\u00c3b\2\u018a\u018b\5\u00c9e\2\u018b\u018c")
        buf.write("\5\u00a9U\2\u018c8\3\2\2\2\u018d\u018e\7H\2\2\u018e\u018f")
        buf.write("\5\u00a1Q\2\u018f\u0190\5\u00b7\\\2\u0190\u0191\5\u00c5")
        buf.write("c\2\u0191\u0192\5\u00a9U\2\u0192:\3\2\2\2\u0193\u0194")
        buf.write("\7G\2\2\u0194\u0195\5\u00bb^\2\u0195\u0196\5\u00a7T\2")
        buf.write("\u0196\u0197\5\u00a7T\2\u0197\u0198\5\u00bd_\2\u0198<")
        buf.write("\3\2\2\2\u0199\u019d\5? \2\u019a\u019d\5G$\2\u019b\u019d")
        buf.write("\5[.\2\u019c\u0199\3\2\2\2\u019c\u019a\3\2\2\2\u019c\u019b")
        buf.write("\3\2\2\2\u019d>\3\2\2\2\u019e\u01a2\5A!\2\u019f\u01a2")
        buf.write("\5C\"\2\u01a0\u01a2\5E#\2\u01a1\u019e\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a2@\3\2\2\2\u01a3\u01a4")
        buf.write("\7#\2\2\u01a4B\3\2\2\2\u01a5\u01a6\7(\2\2\u01a6\u01a7")
        buf.write("\7(\2\2\u01a7D\3\2\2\2\u01a8\u01a9\7~\2\2\u01a9\u01aa")
        buf.write("\7~\2\2\u01aaF\3\2\2\2\u01ab\u01b5\5I%\2\u01ac\u01b5\5")
        buf.write("K&\2\u01ad\u01b5\5M\'\2\u01ae\u01b5\5O(\2\u01af\u01b5")
        buf.write("\5Q)\2\u01b0\u01b5\5S*\2\u01b1\u01b5\5U+\2\u01b2\u01b5")
        buf.write("\5W,\2\u01b3\u01b5\5Y-\2\u01b4\u01ab\3\2\2\2\u01b4\u01ac")
        buf.write("\3\2\2\2\u01b4\u01ad\3\2\2\2\u01b4\u01ae\3\2\2\2\u01b4")
        buf.write("\u01af\3\2\2\2\u01b4\u01b0\3\2\2\2\u01b4\u01b1\3\2\2\2")
        buf.write("\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5H\3\2\2")
        buf.write("\2\u01b6\u01b7\7-\2\2\u01b7J\3\2\2\2\u01b8\u01b9\7/\2")
        buf.write("\2\u01b9L\3\2\2\2\u01ba\u01bb\7,\2\2\u01bbN\3\2\2\2\u01bc")
        buf.write("\u01bd\7^\2\2\u01bdP\3\2\2\2\u01be\u01bf\7\'\2\2\u01bf")
        buf.write("R\3\2\2\2\u01c0\u01c1\5I%\2\u01c1\u01c2\5\u008bF\2\u01c2")
        buf.write("T\3\2\2\2\u01c3\u01c4\5K&\2\u01c4\u01c5\5\u008bF\2\u01c5")
        buf.write("V\3\2\2\2\u01c6\u01c7\5M\'\2\u01c7\u01c8\5\u008bF\2\u01c8")
        buf.write("X\3\2\2\2\u01c9\u01ca\5O(\2\u01ca\u01cb\5\u008bF\2\u01cb")
        buf.write("Z\3\2\2\2\u01cc\u01cf\5]/\2\u01cd\u01cf\5m\67\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\\\3\2\2\2\u01d0")
        buf.write("\u01d7\5a\61\2\u01d1\u01d7\5c\62\2\u01d2\u01d7\5e\63\2")
        buf.write("\u01d3\u01d7\5g\64\2\u01d4\u01d7\5i\65\2\u01d5\u01d7\5")
        buf.write("k\66\2\u01d6\u01d0\3\2\2\2\u01d6\u01d1\3\2\2\2\u01d6\u01d2")
        buf.write("\3\2\2\2\u01d6\u01d3\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d5\3\2\2\2\u01d7^\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9")
        buf.write("`\3\2\2\2\u01da\u01db\5_\60\2\u01db\u01dc\5_\60\2\u01dc")
        buf.write("b\3\2\2\2\u01dd\u01de\5A!\2\u01de\u01df\5_\60\2\u01df")
        buf.write("d\3\2\2\2\u01e0\u01e1\7>\2\2\u01e1f\3\2\2\2\u01e2\u01e3")
        buf.write("\5e\63\2\u01e3\u01e4\5_\60\2\u01e4h\3\2\2\2\u01e5\u01e6")
        buf.write("\7@\2\2\u01e6j\3\2\2\2\u01e7\u01e8\5i\65\2\u01e8\u01e9")
        buf.write("\5_\60\2\u01e9l\3\2\2\2\u01ea\u01f0\5o8\2\u01eb\u01f0")
        buf.write("\5q9\2\u01ec\u01f0\5s:\2\u01ed\u01f0\5u;\2\u01ee\u01f0")
        buf.write("\5w<\2\u01ef\u01ea\3\2\2\2\u01ef\u01eb\3\2\2\2\u01ef\u01ec")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee\3\2\2\2\u01f0")
        buf.write("n\3\2\2\2\u01f1\u01f2\5_\60\2\u01f2\u01f3\7\61\2\2\u01f3")
        buf.write("\u01f4\5_\60\2\u01f4p\3\2\2\2\u01f5\u01f6\5e\63\2\u01f6")
        buf.write("\u01f7\5\u008bF\2\u01f7r\3\2\2\2\u01f8\u01f9\5e\63\2\u01f9")
        buf.write("\u01fa\5_\60\2\u01fa\u01fb\5\u008bF\2\u01fbt\3\2\2\2\u01fc")
        buf.write("\u01fd\5i\65\2\u01fd\u01fe\5\u008bF\2\u01fev\3\2\2\2\u01ff")
        buf.write("\u0200\5u;\2\u0200\u0201\5_\60\2\u0201x\3\2\2\2\u0202")
        buf.write("\u0203\7*\2\2\u0203z\3\2\2\2\u0204\u0205\7+\2\2\u0205")
        buf.write("|\3\2\2\2\u0206\u0207\7}\2\2\u0207~\3\2\2\2\u0208\u0209")
        buf.write("\7\177\2\2\u0209\u0080\3\2\2\2\u020a\u020b\7]\2\2\u020b")
        buf.write("\u0082\3\2\2\2\u020c\u020d\7_\2\2\u020d\u0084\3\2\2\2")
        buf.write("\u020e\u020f\7=\2\2\u020f\u0086\3\2\2\2\u0210\u0211\7")
        buf.write("<\2\2\u0211\u0088\3\2\2\2\u0212\u0213\7.\2\2\u0213\u008a")
        buf.write("\3\2\2\2\u0214\u0215\7\60\2\2\u0215\u008c\3\2\2\2\u0216")
        buf.write("\u0219\5I%\2\u0217\u0219\5K&\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0217\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021d\3\2\2\2")
        buf.write("\u021a\u021e\5\5\3\2\u021b\u021e\5\7\4\2\u021c\u021e\5")
        buf.write("\t\5\2\u021d\u021a\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u008e\3\2\2\2\u021f\u0222\5I%\2\u0220\u0222")
        buf.write("\5K&\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2\u0221\u0222")
        buf.write("\3\2\2\2\u0222\u0243\3\2\2\2\u0223\u0225\5\3\2\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229\5")
        buf.write("\u008bF\2\u0229\u022a\5\r\7\2\u022a\u0244\3\2\2\2\u022b")
        buf.write("\u022d\5\3\2\2\u022c\u022b\3\2\2\2\u022d\u022e\3\2\2\2")
        buf.write("\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022f\u0230\3")
        buf.write("\2\2\2\u0230\u0231\5\r\7\2\u0231\u0244\3\2\2\2\u0232\u0234")
        buf.write("\5\3\2\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u0241\5\u008bF\2\u0239\u023b")
        buf.write("\5\3\2\2\u023a\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c")
        buf.write("\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023f\3\2\2\2")
        buf.write("\u023e\u0240\5\r\7\2\u023f\u023e\3\2\2\2\u023f\u0240\3")
        buf.write("\2\2\2\u0240\u0242\3\2\2\2\u0241\u023a\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242\u0244\3\2\2\2\u0243\u0224\3\2\2\2\u0243")
        buf.write("\u022c\3\2\2\2\u0243\u0235\3\2\2\2\u0244\u0090\3\2\2\2")
        buf.write("\u0245\u0248\5\67\34\2\u0246\u0248\59\35\2\u0247\u0245")
        buf.write("\3\2\2\2\u0247\u0246\3\2\2\2\u0248\u0092\3\2\2\2\u0249")
        buf.write("\u024d\7$\2\2\u024a\u024c\5\u0095K\2\u024b\u024a\3\2\2")
        buf.write("\2\u024c\u024f\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e")
        buf.write("\3\2\2\2\u024e\u0250\3\2\2\2\u024f\u024d\3\2\2\2\u0250")
        buf.write("\u0251\7$\2\2\u0251\u0094\3\2\2\2\u0252\u0253\n\t\2\2")
        buf.write("\u0253\u0096\3\2\2\2\u0254\u0258\t\n\2\2\u0255\u0257\t")
        buf.write("\13\2\2\u0256\u0255\3\2\2\2\u0257\u025a\3\2\2\2\u0258")
        buf.write("\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u0098\3\2\2\2")
        buf.write("\u025a\u0258\3\2\2\2\u025b\u025c\13\2\2\2\u025c\u009a")
        buf.write("\3\2\2\2\u025d\u025e\13\2\2\2\u025e\u009c\3\2\2\2\u025f")
        buf.write("\u0260\13\2\2\2\u0260\u009e\3\2\2\2\u0261\u0262\13\2\2")
        buf.write("\2\u0262\u00a0\3\2\2\2\u0263\u0264\t\f\2\2\u0264\u00a2")
        buf.write("\3\2\2\2\u0265\u0266\t\r\2\2\u0266\u00a4\3\2\2\2\u0267")
        buf.write("\u0268\t\16\2\2\u0268\u00a6\3\2\2\2\u0269\u026a\t\17\2")
        buf.write("\2\u026a\u00a8\3\2\2\2\u026b\u026c\t\6\2\2\u026c\u00aa")
        buf.write("\3\2\2\2\u026d\u026e\t\20\2\2\u026e\u00ac\3\2\2\2\u026f")
        buf.write("\u0270\t\21\2\2\u0270\u00ae\3\2\2\2\u0271\u0272\t\22\2")
        buf.write("\2\u0272\u00b0\3\2\2\2\u0273\u0274\t\23\2\2\u0274\u00b2")
        buf.write("\3\2\2\2\u0275\u0276\t\24\2\2\u0276\u00b4\3\2\2\2\u0277")
        buf.write("\u0278\t\25\2\2\u0278\u00b6\3\2\2\2\u0279\u027a\t\26\2")
        buf.write("\2\u027a\u00b8\3\2\2\2\u027b\u027c\t\27\2\2\u027c\u00ba")
        buf.write("\3\2\2\2\u027d\u027e\t\30\2\2\u027e\u00bc\3\2\2\2\u027f")
        buf.write("\u0280\t\31\2\2\u0280\u00be\3\2\2\2\u0281\u0282\t\32\2")
        buf.write("\2\u0282\u00c0\3\2\2\2\u0283\u0284\t\33\2\2\u0284\u00c2")
        buf.write("\3\2\2\2\u0285\u0286\t\34\2\2\u0286\u00c4\3\2\2\2\u0287")
        buf.write("\u0288\t\35\2\2\u0288\u00c6\3\2\2\2\u0289\u028a\t\36\2")
        buf.write("\2\u028a\u00c8\3\2\2\2\u028b\u028c\t\37\2\2\u028c\u00ca")
        buf.write("\3\2\2\2\u028d\u028e\t \2\2\u028e\u00cc\3\2\2\2\u028f")
        buf.write("\u0290\t!\2\2\u0290\u00ce\3\2\2\2\u0291\u0292\t\"\2\2")
        buf.write("\u0292\u00d0\3\2\2\2\u0293\u0294\t#\2\2\u0294\u00d2\3")
        buf.write("\2\2\2\u0295\u0296\t$\2\2\u0296\u00d4\3\2\2\2 \2\u00dc")
        buf.write("\u00df\u00e5\u00ea\u00f0\u00f5\u00fb\u0100\u0105\u010f")
        buf.write("\u019c\u01a1\u01b4\u01ce\u01d6\u01ef\u0218\u021d\u0221")
        buf.write("\u0226\u022e\u0235\u023c\u023f\u0241\u0243\u0247\u024d")
        buf.write("\u0258\3\b\2\2")
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
                  "STRINGLIT", "STRCHAR", "ID", "ERROR_CHAR", "UNCLOSE_STRING", 
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


