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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\u0188\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\3\7\3U\n\3\f\3\16\3X\13")
        buf.write("\3\3\4\3\4\5\4\\\n\4\3\5\3\5\3\5\3\6\3\6\3\6\7\6d\n\6")
        buf.write("\f\6\16\6g\13\6\3\6\3\6\3\6\3\7\3\7\5\7n\n\7\3\7\3\7\3")
        buf.write("\7\7\7s\n\7\f\7\16\7v\13\7\3\b\3\b\5\bz\n\b\3\t\3\t\3")
        buf.write("\t\5\t\177\n\t\3\n\3\n\3\n\3\n\7\n\u0085\n\n\f\n\16\n")
        buf.write("\u0088\13\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\5\13\u0096\n\13\3\f\3\f\3\f\7\f\u009b")
        buf.write("\n\f\f\f\16\f\u009e\13\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u00ab\n\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\7\17\u00b4\n\17\f\17\16\17\u00b7\13\17")
        buf.write("\3\20\3\20\3\20\3\20\7\20\u00bd\n\20\f\20\16\20\u00c0")
        buf.write("\13\20\3\20\7\20\u00c3\n\20\f\20\16\20\u00c6\13\20\3\20")
        buf.write("\5\20\u00c9\n\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\7")
        buf.write("\21\u00d2\n\21\f\21\16\21\u00d5\13\21\3\22\3\22\7\22\u00d9")
        buf.write("\n\22\f\22\16\22\u00dc\13\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00ea\n\23\f")
        buf.write("\23\16\23\u00ed\13\23\3\23\3\23\3\23\3\24\3\24\7\24\u00f4")
        buf.write("\n\24\f\24\16\24\u00f7\13\24\3\25\3\25\3\25\6\25\u00fc")
        buf.write("\n\25\r\25\16\25\u00fd\3\25\3\25\3\26\3\26\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\7\30\u010a\n\30\f\30\16\30\u010d\13")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\7\31\u0114\n\31\f\31\16\31")
        buf.write("\u0117\13\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\5\34\u0128\n\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\7\35\u0131\n\35\f\35\16")
        buf.write("\35\u0134\13\35\5\35\u0136\n\35\3\35\3\35\3\36\3\36\3")
        buf.write("\36\3\37\3\37\3\37\3\37\3\37\5\37\u0142\n\37\3 \3 \3 ")
        buf.write("\3 \3 \3 \7 \u014a\n \f \16 \u014d\13 \3!\3!\3!\3!\3!")
        buf.write("\3!\7!\u0155\n!\f!\16!\u0158\13!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\7\"\u0160\n\"\f\"\16\"\u0163\13\"\3#\3#\3#\5#\u0168")
        buf.write("\n#\3$\3$\3$\5$\u016d\n$\3%\3%\3%\3%\3%\7%\u0174\n%\f")
        buf.write("%\16%\u0177\13%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\5\'\u0184\n\'\3(\3(\3(\2\6>@BH)\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLN\2")
        buf.write("\7\3\2\36\37\4\2 !%&\4\2\"$\'(\4\2!!&&\5\2\32\33?@EE\2")
        buf.write("\u018f\2P\3\2\2\2\4V\3\2\2\2\6[\3\2\2\2\b]\3\2\2\2\n`")
        buf.write("\3\2\2\2\fm\3\2\2\2\16y\3\2\2\2\20~\3\2\2\2\22\u0080\3")
        buf.write("\2\2\2\24\u0095\3\2\2\2\26\u0097\3\2\2\2\30\u00a2\3\2")
        buf.write("\2\2\32\u00a6\3\2\2\2\34\u00ae\3\2\2\2\36\u00b8\3\2\2")
        buf.write("\2 \u00cd\3\2\2\2\"\u00d6\3\2\2\2$\u00dd\3\2\2\2&\u00f1")
        buf.write("\3\2\2\2(\u00f8\3\2\2\2*\u0101\3\2\2\2,\u0103\3\2\2\2")
        buf.write(".\u0105\3\2\2\2\60\u0111\3\2\2\2\62\u011d\3\2\2\2\64\u0120")
        buf.write("\3\2\2\2\66\u0123\3\2\2\28\u012b\3\2\2\2:\u0139\3\2\2")
        buf.write("\2<\u0141\3\2\2\2>\u0143\3\2\2\2@\u014e\3\2\2\2B\u0159")
        buf.write("\3\2\2\2D\u0167\3\2\2\2F\u016c\3\2\2\2H\u016e\3\2\2\2")
        buf.write("J\u0178\3\2\2\2L\u0183\3\2\2\2N\u0185\3\2\2\2PQ\5\4\3")
        buf.write("\2QR\7\2\2\3R\3\3\2\2\2SU\5\24\13\2TS\3\2\2\2UX\3\2\2")
        buf.write("\2VT\3\2\2\2VW\3\2\2\2W\5\3\2\2\2XV\3\2\2\2Y\\\5\b\5\2")
        buf.write("Z\\\5\n\6\2[Y\3\2\2\2[Z\3\2\2\2\\\7\3\2\2\2]^\5\f\7\2")
        buf.write("^_\7;\2\2_\t\3\2\2\2`a\7\n\2\2ae\7<\2\2bd\5\24\13\2cb")
        buf.write("\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2\2fh\3\2\2\2ge\3\2")
        buf.write("\2\2hi\7\13\2\2ij\7>\2\2j\13\3\2\2\2kl\7\34\2\2ln\7<\2")
        buf.write("\2mk\3\2\2\2mn\3\2\2\2no\3\2\2\2ot\5\16\b\2pq\7=\2\2q")
        buf.write("s\5\16\b\2rp\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2u\r")
        buf.write("\3\2\2\2vt\3\2\2\2wz\5&\24\2xz\5\30\r\2yw\3\2\2\2yx\3")
        buf.write("\2\2\2z\17\3\2\2\2{\177\5\22\n\2|\177\5&\24\2}\177\5<")
        buf.write("\37\2~{\3\2\2\2~|\3\2\2\2~}\3\2\2\2\177\21\3\2\2\2\u0080")
        buf.write("\u0081\7\67\2\2\u0081\u0086\5\20\t\2\u0082\u0083\7=\2")
        buf.write("\2\u0083\u0085\5\20\t\2\u0084\u0082\3\2\2\2\u0085\u0088")
        buf.write("\3\2\2\2\u0086\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0089\3\2\2\2\u0088\u0086\3\2\2\2\u0089\u008a\78\2\2")
        buf.write("\u008a\23\3\2\2\2\u008b\u0096\5\6\4\2\u008c\u0096\5\32")
        buf.write("\16\2\u008d\u0096\5:\36\2\u008e\u0096\5\36\20\2\u008f")
        buf.write("\u0096\5$\23\2\u0090\u0096\5.\30\2\u0091\u0096\5\60\31")
        buf.write("\2\u0092\u0096\5\62\32\2\u0093\u0096\5\64\33\2\u0094\u0096")
        buf.write("\5\66\34\2\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2\2\u0095")
        buf.write("\u008d\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3\2\2\2")
        buf.write("\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0095\u0092\3")
        buf.write("\2\2\2\u0095\u0093\3\2\2\2\u0095\u0094\3\2\2\2\u0096\25")
        buf.write("\3\2\2\2\u0097\u0098\7\n\2\2\u0098\u009c\7<\2\2\u0099")
        buf.write("\u009b\5\24\13\2\u009a\u0099\3\2\2\2\u009b\u009e\3\2\2")
        buf.write("\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009f")
        buf.write("\3\2\2\2\u009e\u009c\3\2\2\2\u009f\u00a0\7\13\2\2\u00a0")
        buf.write("\u00a1\7>\2\2\u00a1\27\3\2\2\2\u00a2\u00a3\5&\24\2\u00a3")
        buf.write("\u00a4\7)\2\2\u00a4\u00a5\5\20\t\2\u00a5\31\3\2\2\2\u00a6")
        buf.write("\u00a7\7\b\2\2\u00a7\u00a8\7<\2\2\u00a8\u00aa\7A\2\2\u00a9")
        buf.write("\u00ab\5\34\17\2\u00aa\u00a9\3\2\2\2\u00aa\u00ab\3\2\2")
        buf.write("\2\u00ab\u00ac\3\2\2\2\u00ac\u00ad\5\26\f\2\u00ad\33\3")
        buf.write("\2\2\2\u00ae\u00af\7\t\2\2\u00af\u00b0\7<\2\2\u00b0\u00b5")
        buf.write("\5\16\b\2\u00b1\u00b2\7=\2\2\u00b2\u00b4\5\16\b\2\u00b3")
        buf.write("\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2")
        buf.write("\u00b5\u00b6\3\2\2\2\u00b6\35\3\2\2\2\u00b7\u00b5\3\2")
        buf.write("\2\2\u00b8\u00b9\7\f\2\2\u00b9\u00ba\5<\37\2\u00ba\u00be")
        buf.write("\7\r\2\2\u00bb\u00bd\5\24\13\2\u00bc\u00bb\3\2\2\2\u00bd")
        buf.write("\u00c0\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2")
        buf.write("\u00bf\u00c4\3\2\2\2\u00c0\u00be\3\2\2\2\u00c1\u00c3\5")
        buf.write(" \21\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6\3\2\2\2\u00c4\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c7\u00c9\5\"\22\2\u00c8\u00c7\3\2\2")
        buf.write("\2\u00c8\u00c9\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb")
        buf.write("\7\20\2\2\u00cb\u00cc\7>\2\2\u00cc\37\3\2\2\2\u00cd\u00ce")
        buf.write("\7\16\2\2\u00ce\u00cf\5<\37\2\u00cf\u00d3\7\r\2\2\u00d0")
        buf.write("\u00d2\5\24\13\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2")
        buf.write("\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4!\3\2")
        buf.write("\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00da\7\17\2\2\u00d7\u00d9")
        buf.write("\5\24\13\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da")
        buf.write("\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db#\3\2\2\2\u00dc")
        buf.write("\u00da\3\2\2\2\u00dd\u00de\7\21\2\2\u00de\u00df\7\65\2")
        buf.write("\2\u00df\u00e0\5&\24\2\u00e0\u00e1\7)\2\2\u00e1\u00e2")
        buf.write("\5<\37\2\u00e2\u00e3\7=\2\2\u00e3\u00e4\5*\26\2\u00e4")
        buf.write("\u00e5\7=\2\2\u00e5\u00e6\5,\27\2\u00e6\u00e7\7\66\2\2")
        buf.write("\u00e7\u00eb\7\23\2\2\u00e8\u00ea\5\24\13\2\u00e9\u00e8")
        buf.write("\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3\2\2\2")
        buf.write("\u00ee\u00ef\7\22\2\2\u00ef\u00f0\7>\2\2\u00f0%\3\2\2")
        buf.write("\2\u00f1\u00f5\7A\2\2\u00f2\u00f4\5(\25\2\u00f3\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\'\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f8")
        buf.write("\u00fb\79\2\2\u00f9\u00fc\5&\24\2\u00fa\u00fc\5<\37\2")
        buf.write("\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0100\7:\2\2\u0100)\3\2\2\2\u0101\u0102")
        buf.write("\5<\37\2\u0102+\3\2\2\2\u0103\u0104\5<\37\2\u0104-\3\2")
        buf.write("\2\2\u0105\u0106\7\25\2\2\u0106\u0107\5<\37\2\u0107\u010b")
        buf.write("\7\23\2\2\u0108\u010a\5\24\13\2\u0109\u0108\3\2\2\2\u010a")
        buf.write("\u010d\3\2\2\2\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010e\3\2\2\2\u010d\u010b\3\2\2\2\u010e\u010f\7")
        buf.write("\26\2\2\u010f\u0110\7>\2\2\u0110/\3\2\2\2\u0111\u0115")
        buf.write("\7\23\2\2\u0112\u0114\5\24\13\2\u0113\u0112\3\2\2\2\u0114")
        buf.write("\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3\2\2\2")
        buf.write("\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119\7")
        buf.write("\25\2\2\u0119\u011a\5<\37\2\u011a\u011b\7\24\2\2\u011b")
        buf.write("\u011c\7>\2\2\u011c\61\3\2\2\2\u011d\u011e\7\30\2\2\u011e")
        buf.write("\u011f\7;\2\2\u011f\63\3\2\2\2\u0120\u0121\7\31\2\2\u0121")
        buf.write("\u0122\7;\2\2\u0122\65\3\2\2\2\u0123\u0127\7\27\2\2\u0124")
        buf.write("\u0128\5&\24\2\u0125\u0128\5N(\2\u0126\u0128\5<\37\2\u0127")
        buf.write("\u0124\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7")
        buf.write(";\2\2\u012a\67\3\2\2\2\u012b\u012c\7A\2\2\u012c\u0135")
        buf.write("\7\65\2\2\u012d\u0132\5<\37\2\u012e\u012f\7=\2\2\u012f")
        buf.write("\u0131\5<\37\2\u0130\u012e\3\2\2\2\u0131\u0134\3\2\2\2")
        buf.write("\u0132\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0136\3")
        buf.write("\2\2\2\u0134\u0132\3\2\2\2\u0135\u012d\3\2\2\2\u0135\u0136")
        buf.write("\3\2\2\2\u0136\u0137\3\2\2\2\u0137\u0138\7\66\2\2\u0138")
        buf.write("9\3\2\2\2\u0139\u013a\58\35\2\u013a\u013b\7;\2\2\u013b")
        buf.write(";\3\2\2\2\u013c\u013d\5> \2\u013d\u013e\7\3\2\2\u013e")
        buf.write("\u013f\5> \2\u013f\u0142\3\2\2\2\u0140\u0142\5> \2\u0141")
        buf.write("\u013c\3\2\2\2\u0141\u0140\3\2\2\2\u0142=\3\2\2\2\u0143")
        buf.write("\u0144\b \1\2\u0144\u0145\5@!\2\u0145\u014b\3\2\2\2\u0146")
        buf.write("\u0147\f\4\2\2\u0147\u0148\t\2\2\2\u0148\u014a\5@!\2\u0149")
        buf.write("\u0146\3\2\2\2\u014a\u014d\3\2\2\2\u014b\u0149\3\2\2\2")
        buf.write("\u014b\u014c\3\2\2\2\u014c?\3\2\2\2\u014d\u014b\3\2\2")
        buf.write("\2\u014e\u014f\b!\1\2\u014f\u0150\5B\"\2\u0150\u0156\3")
        buf.write("\2\2\2\u0151\u0152\f\4\2\2\u0152\u0153\t\3\2\2\u0153\u0155")
        buf.write("\5B\"\2\u0154\u0151\3\2\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157A\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0159\u015a\b\"\1\2\u015a\u015b\5D#\2\u015b")
        buf.write("\u0161\3\2\2\2\u015c\u015d\f\4\2\2\u015d\u015e\t\4\2\2")
        buf.write("\u015e\u0160\5D#\2\u015f\u015c\3\2\2\2\u0160\u0163\3\2")
        buf.write("\2\2\u0161\u015f\3\2\2\2\u0161\u0162\3\2\2\2\u0162C\3")
        buf.write("\2\2\2\u0163\u0161\3\2\2\2\u0164\u0165\7\35\2\2\u0165")
        buf.write("\u0168\5D#\2\u0166\u0168\5F$\2\u0167\u0164\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168E\3\2\2\2\u0169\u016a\t\5\2\2\u016a")
        buf.write("\u016d\5F$\2\u016b\u016d\5H%\2\u016c\u0169\3\2\2\2\u016c")
        buf.write("\u016b\3\2\2\2\u016dG\3\2\2\2\u016e\u016f\b%\1\2\u016f")
        buf.write("\u0170\5L\'\2\u0170\u0175\3\2\2\2\u0171\u0172\f\4\2\2")
        buf.write("\u0172\u0174\5J&\2\u0173\u0171\3\2\2\2\u0174\u0177\3\2")
        buf.write("\2\2\u0175\u0173\3\2\2\2\u0175\u0176\3\2\2\2\u0176I\3")
        buf.write("\2\2\2\u0177\u0175\3\2\2\2\u0178\u0179\79\2\2\u0179\u017a")
        buf.write("\5<\37\2\u017a\u017b\7:\2\2\u017bK\3\2\2\2\u017c\u017d")
        buf.write("\7\65\2\2\u017d\u017e\5<\37\2\u017e\u017f\7\66\2\2\u017f")
        buf.write("\u0184\3\2\2\2\u0180\u0184\58\35\2\u0181\u0184\5N(\2\u0182")
        buf.write("\u0184\7A\2\2\u0183\u017c\3\2\2\2\u0183\u0180\3\2\2\2")
        buf.write("\u0183\u0181\3\2\2\2\u0183\u0182\3\2\2\2\u0184M\3\2\2")
        buf.write("\2\u0185\u0186\t\6\2\2\u0186O\3\2\2\2$V[emty~\u0086\u0095")
        buf.write("\u009c\u00aa\u00b5\u00be\u00c4\u00c8\u00d3\u00da\u00eb")
        buf.write("\u00f5\u00fb\u00fd\u010b\u0115\u0127\u0132\u0135\u0141")
        buf.write("\u014b\u0156\u0161\u0167\u016c\u0175\u0183")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Function'", "'Parameter'", 
                     "'Body'", "'EndBody'", "'If'", "'Then'", "'ElseIf'", 
                     "'Else'", "'EndIf'", "'For'", "'EndFor'", "'Do'", "'EndDo'", 
                     "'While'", "'EndWhile'", "'Return'", "'Break'", "'Continue'", 
                     "'True'", "'False'", "'Var'", "'!'", "'&&'", "'||'", 
                     "'+'", "'-'", "'*'", "'\\'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "<INVALID>", "<INVALID>", 
                     "'<'", "<INVALID>", "'>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "RELATIONAL", "RELATIONAL_INT", "RELATIONAL_FLOAT", 
                      "WS", "BCMT", "FUNCTION", "PARAMETER", "BODY", "ENDBODY", 
                      "IF", "THEN", "ELSEIF", "ELSE", "ENDIF", "FOR", "ENDFOR", 
                      "DO", "ENDDO", "WHILE", "ENDWHILE", "RETURN", "BREAK", 
                      "CONTINUE", "TRUE", "FALSE", "VAR", "NOT", "AND", 
                      "OR", "ADD", "SUB", "MUL", "DIV", "MOD", "ADDDOT", 
                      "SUBDOT", "MULDOT", "DIVDOT", "EQ", "EQINT", "NEQINT", 
                      "LTINT", "LTEINT", "GTINT", "GTEINT", "NEQF", "LTF", 
                      "LTEF", "GTF", "GTEF", "LP", "RP", "LCB", "RCB", "LSB", 
                      "RSB", "SEMI", "COLON", "COMMA", "DOT", "INTLIT", 
                      "FLOATLIT", "ID", "ILLEGAL_ESCAPE", "UNCLOSE_STRING", 
                      "UNTERMINATED_COMMENT", "STRINGLIT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_main = 1
    RULE_var_declare_stmt = 2
    RULE_var_single = 3
    RULE_var_list = 4
    RULE_var_normal = 5
    RULE_var_normal_list = 6
    RULE_var_vp = 7
    RULE_array_vp = 8
    RULE_stmt = 9
    RULE_body_declare = 10
    RULE_assign_stmt = 11
    RULE_func_declare = 12
    RULE_parameter_func = 13
    RULE_if_stmt = 14
    RULE_elseif_stmt = 15
    RULE_else_stmt = 16
    RULE_for_stmt = 17
    RULE_scalar_var = 18
    RULE_index_var = 19
    RULE_conditionExpr = 20
    RULE_updateExpr = 21
    RULE_while_stmt = 22
    RULE_doWhile_stmt = 23
    RULE_break_stmt = 24
    RULE_continue_stmt = 25
    RULE_return_stmt = 26
    RULE_func_call = 27
    RULE_call_stmt = 28
    RULE_exp = 29
    RULE_exp1 = 30
    RULE_exp2 = 31
    RULE_exp3 = 32
    RULE_exp4 = 33
    RULE_exp5 = 34
    RULE_exp6 = 35
    RULE_op_index = 36
    RULE_operands = 37
    RULE_all_lit = 38

    ruleNames =  [ "program", "main", "var_declare_stmt", "var_single", 
                   "var_list", "var_normal", "var_normal_list", "var_vp", 
                   "array_vp", "stmt", "body_declare", "assign_stmt", "func_declare", 
                   "parameter_func", "if_stmt", "elseif_stmt", "else_stmt", 
                   "for_stmt", "scalar_var", "index_var", "conditionExpr", 
                   "updateExpr", "while_stmt", "doWhile_stmt", "break_stmt", 
                   "continue_stmt", "return_stmt", "func_call", "call_stmt", 
                   "exp", "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", 
                   "op_index", "operands", "all_lit" ]

    EOF = Token.EOF
    RELATIONAL=1
    RELATIONAL_INT=2
    RELATIONAL_FLOAT=3
    WS=4
    BCMT=5
    FUNCTION=6
    PARAMETER=7
    BODY=8
    ENDBODY=9
    IF=10
    THEN=11
    ELSEIF=12
    ELSE=13
    ENDIF=14
    FOR=15
    ENDFOR=16
    DO=17
    ENDDO=18
    WHILE=19
    ENDWHILE=20
    RETURN=21
    BREAK=22
    CONTINUE=23
    TRUE=24
    FALSE=25
    VAR=26
    NOT=27
    AND=28
    OR=29
    ADD=30
    SUB=31
    MUL=32
    DIV=33
    MOD=34
    ADDDOT=35
    SUBDOT=36
    MULDOT=37
    DIVDOT=38
    EQ=39
    EQINT=40
    NEQINT=41
    LTINT=42
    LTEINT=43
    GTINT=44
    GTEINT=45
    NEQF=46
    LTF=47
    LTEF=48
    GTF=49
    GTEF=50
    LP=51
    RP=52
    LCB=53
    RCB=54
    LSB=55
    RSB=56
    SEMI=57
    COLON=58
    COMMA=59
    DOT=60
    INTLIT=61
    FLOATLIT=62
    ID=63
    ILLEGAL_ESCAPE=64
    UNCLOSE_STRING=65
    UNTERMINATED_COMMENT=66
    STRINGLIT=67
    ERROR_CHAR=68

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
            self.state = 78
            self.main()
            self.state = 79
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

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 81
                self.stmt()
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_single(self):
            return self.getTypedRuleContext(BKITParser.Var_singleContext,0)


        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_declare_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_stmt" ):
                return visitor.visitVar_declare_stmt(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_stmt(self):

        localctx = BKITParser.Var_declare_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_declare_stmt)
        try:
            self.state = 89
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR, BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.var_single()
                pass
            elif token in [BKITParser.BODY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.var_list()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_singleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_normal(self):
            return self.getTypedRuleContext(BKITParser.Var_normalContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_var_single

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_single" ):
                return visitor.visitVar_single(self)
            else:
                return visitor.visitChildren(self)




    def var_single(self):

        localctx = BKITParser.Var_singleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_single)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.var_normal()
            self.state = 92
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_list" ):
                return visitor.visitVar_list(self)
            else:
                return visitor.visitChildren(self)




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(BKITParser.BODY)
            self.state = 95
            self.match(BKITParser.COLON)
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 96
                self.stmt()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 102
            self.match(BKITParser.ENDBODY)
            self.state = 103
            self.match(BKITParser.DOT)
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

        def var_normal_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_normal_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_normal_listContext,i)


        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_var_normal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal" ):
                return visitor.visitVar_normal(self)
            else:
                return visitor.visitChildren(self)




    def var_normal(self):

        localctx = BKITParser.Var_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.VAR:
                self.state = 105
                self.match(BKITParser.VAR)
                self.state = 106
                self.match(BKITParser.COLON)


            self.state = 109
            self.var_normal_list()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 110
                self.match(BKITParser.COMMA)
                self.state = 111
                self.var_normal_list()
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_normal_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_normal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal_list" ):
                return visitor.visitVar_normal_list(self)
            else:
                return visitor.visitChildren(self)




    def var_normal_list(self):

        localctx = BKITParser.Var_normal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_normal_list)
        try:
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.scalar_var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.assign_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_vpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_vp(self):
            return self.getTypedRuleContext(BKITParser.Array_vpContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_vp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_vp" ):
                return visitor.visitVar_vp(self)
            else:
                return visitor.visitChildren(self)




    def var_vp(self):

        localctx = BKITParser.Var_vpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_vp)
        try:
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.array_vp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.scalar_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 123
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_vpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def var_vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vpContext,i)


        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_vp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_vp" ):
                return visitor.visitArray_vp(self)
            else:
                return visitor.visitChildren(self)




    def array_vp(self):

        localctx = BKITParser.Array_vpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_vp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(BKITParser.LCB)
            self.state = 127
            self.var_vp()
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 128
                self.match(BKITParser.COMMA)
                self.state = 129
                self.var_vp()
                self.state = 134
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 135
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def doWhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.DoWhile_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_stmt)
        try:
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.var_declare_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.func_declare()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.call_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.if_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.for_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.doWhile_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 144
                self.break_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 145
                self.continue_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 146
                self.return_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Body_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_body_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody_declare" ):
                return visitor.visitBody_declare(self)
            else:
                return visitor.visitChildren(self)




    def body_declare(self):

        localctx = BKITParser.Body_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKITParser.BODY)
            self.state = 150
            self.match(BKITParser.COLON)
            self.state = 154
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 151
                self.stmt()
                self.state = 156
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 157
            self.match(BKITParser.ENDBODY)
            self.state = 158
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def var_vp(self):
            return self.getTypedRuleContext(BKITParser.Var_vpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assign_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.scalar_var()
            self.state = 161
            self.match(BKITParser.EQ)
            self.state = 162
            self.var_vp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def body_declare(self):
            return self.getTypedRuleContext(BKITParser.Body_declareContext,0)


        def parameter_func(self):
            return self.getTypedRuleContext(BKITParser.Parameter_funcContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_declare" ):
                return visitor.visitFunc_declare(self)
            else:
                return visitor.visitChildren(self)




    def func_declare(self):

        localctx = BKITParser.Func_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(BKITParser.FUNCTION)
            self.state = 165
            self.match(BKITParser.COLON)
            self.state = 166
            self.match(BKITParser.ID)
            self.state = 168
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 167
                self.parameter_func()


            self.state = 170
            self.body_declare()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parameter_funcContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_normal_list(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_normal_listContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_normal_listContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_parameter_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter_func" ):
                return visitor.visitParameter_func(self)
            else:
                return visitor.visitChildren(self)




    def parameter_func(self):

        localctx = BKITParser.Parameter_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_parameter_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(BKITParser.PARAMETER)
            self.state = 173
            self.match(BKITParser.COLON)
            self.state = 174
            self.var_normal_list()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 175
                self.match(BKITParser.COMMA)
                self.state = 176
                self.var_normal_list()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def elseif_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Elseif_stmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.Elseif_stmtContext,i)


        def else_stmt(self):
            return self.getTypedRuleContext(BKITParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_if_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_stmt" ):
                return visitor.visitIf_stmt(self)
            else:
                return visitor.visitChildren(self)




    def if_stmt(self):

        localctx = BKITParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BKITParser.IF)
            self.state = 183
            self.exp()
            self.state = 184
            self.match(BKITParser.THEN)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 185
                self.stmt()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 191
                self.elseif_stmt()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 197
                self.else_stmt()


            self.state = 200
            self.match(BKITParser.ENDIF)
            self.state = 201
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_elseif_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_stmt" ):
                return visitor.visitElseif_stmt(self)
            else:
                return visitor.visitChildren(self)




    def elseif_stmt(self):

        localctx = BKITParser.Elseif_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_elseif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BKITParser.ELSEIF)
            self.state = 204
            self.exp()
            self.state = 205
            self.match(BKITParser.THEN)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 206
                self.stmt()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_else_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_stmt" ):
                return visitor.visitElse_stmt(self)
            else:
                return visitor.visitChildren(self)




    def else_stmt(self):

        localctx = BKITParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BKITParser.ELSE)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 213
                self.stmt()
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def conditionExpr(self):
            return self.getTypedRuleContext(BKITParser.ConditionExprContext,0)


        def updateExpr(self):
            return self.getTypedRuleContext(BKITParser.UpdateExprContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_for_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_stmt" ):
                return visitor.visitFor_stmt(self)
            else:
                return visitor.visitChildren(self)




    def for_stmt(self):

        localctx = BKITParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BKITParser.FOR)
            self.state = 220
            self.match(BKITParser.LP)
            self.state = 221
            self.scalar_var()
            self.state = 222
            self.match(BKITParser.EQ)
            self.state = 223
            self.exp()
            self.state = 224
            self.match(BKITParser.COMMA)
            self.state = 225
            self.conditionExpr()
            self.state = 226
            self.match(BKITParser.COMMA)
            self.state = 227
            self.updateExpr()
            self.state = 228
            self.match(BKITParser.RP)
            self.state = 229
            self.match(BKITParser.DO)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 230
                self.stmt()
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 236
            self.match(BKITParser.ENDFOR)
            self.state = 237
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_varContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var" ):
                return visitor.visitScalar_var(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_scalar_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BKITParser.ID)
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 240
                self.index_var()
                self.state = 245
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def scalar_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_varContext,i)


        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_index_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_var" ):
                return visitor.visitIndex_var(self)
            else:
                return visitor.visitChildren(self)




    def index_var(self):

        localctx = BKITParser.Index_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_index_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(BKITParser.LSB)
            self.state = 249 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 249
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 247
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 248
                    self.exp()
                    pass


                self.state = 251 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0)):
                    break

            self.state = 253
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_conditionExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionExpr" ):
                return visitor.visitConditionExpr(self)
            else:
                return visitor.visitChildren(self)




    def conditionExpr(self):

        localctx = BKITParser.ConditionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_updateExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateExpr" ):
                return visitor.visitUpdateExpr(self)
            else:
                return visitor.visitChildren(self)




    def updateExpr(self):

        localctx = BKITParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_while_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_stmt" ):
                return visitor.visitWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def while_stmt(self):

        localctx = BKITParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(BKITParser.WHILE)
            self.state = 260
            self.exp()
            self.state = 261
            self.match(BKITParser.DO)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.FUNCTION) | (1 << BKITParser.BODY) | (1 << BKITParser.IF) | (1 << BKITParser.FOR) | (1 << BKITParser.DO) | (1 << BKITParser.WHILE) | (1 << BKITParser.RETURN) | (1 << BKITParser.BREAK) | (1 << BKITParser.CONTINUE) | (1 << BKITParser.VAR) | (1 << BKITParser.ID))) != 0):
                self.state = 262
                self.stmt()
                self.state = 267
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 268
            self.match(BKITParser.ENDWHILE)
            self.state = 269
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_doWhile_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDoWhile_stmt" ):
                return visitor.visitDoWhile_stmt(self)
            else:
                return visitor.visitChildren(self)




    def doWhile_stmt(self):

        localctx = BKITParser.DoWhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_doWhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(BKITParser.DO)
            self.state = 275
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.stmt() 
                self.state = 277
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 278
            self.match(BKITParser.WHILE)
            self.state = 279
            self.exp()
            self.state = 280
            self.match(BKITParser.ENDDO)
            self.state = 281
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_break_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_stmt" ):
                return visitor.visitBreak_stmt(self)
            else:
                return visitor.visitChildren(self)




    def break_stmt(self):

        localctx = BKITParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.match(BKITParser.BREAK)
            self.state = 284
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continue_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_stmt" ):
                return visitor.visitContinue_stmt(self)
            else:
                return visitor.visitChildren(self)




    def continue_stmt(self):

        localctx = BKITParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(BKITParser.CONTINUE)
            self.state = 287
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_return_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_stmt" ):
                return visitor.visitReturn_stmt(self)
            else:
                return visitor.visitChildren(self)




    def return_stmt(self):

        localctx = BKITParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(BKITParser.RETURN)
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 290
                self.scalar_var()

            elif la_ == 2:
                self.state = 291
                self.all_lit()

            elif la_ == 3:
                self.state = 292
                self.exp()


            self.state = 295
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ExpContext)
            else:
                return self.getTypedRuleContext(BKITParser.ExpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_func_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = BKITParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(BKITParser.ID)
            self.state = 298
            self.match(BKITParser.LP)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 299
                self.exp()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 300
                    self.match(BKITParser.COMMA)
                    self.state = 301
                    self.exp()
                    self.state = 306
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 309
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_call_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_stmt" ):
                return visitor.visitCall_stmt(self)
            else:
                return visitor.visitChildren(self)




    def call_stmt(self):

        localctx = BKITParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.func_call()
            self.state = 312
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def RELATIONAL(self):
            return self.getToken(BKITParser.RELATIONAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp)
        try:
            self.state = 319
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.exp1(0)
                self.state = 315
                self.match(BKITParser.RELATIONAL)
                self.state = 316
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 318
                self.exp1(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp1" ):
                return visitor.visitExp1(self)
            else:
                return visitor.visitChildren(self)



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 329
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 324
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 325
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 326
                    self.exp2(0) 
                self.state = 331
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def ADDDOT(self):
            return self.getToken(BKITParser.ADDDOT, 0)

        def SUBDOT(self):
            return self.getToken(BKITParser.SUBDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp2" ):
                return visitor.visitExp2(self)
            else:
                return visitor.visitChildren(self)



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 340
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 335
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 336
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDDOT) | (1 << BKITParser.SUBDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 337
                    self.exp3(0) 
                self.state = 342
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def MULDOT(self):
            return self.getToken(BKITParser.MULDOT, 0)

        def DIVDOT(self):
            return self.getToken(BKITParser.DIVDOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp3" ):
                return visitor.visitExp3(self)
            else:
                return visitor.visitChildren(self)



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 351
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 346
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 347
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.MULDOT) | (1 << BKITParser.DIVDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 348
                    self.exp4() 
                self.state = 353
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp4" ):
                return visitor.visitExp4(self)
            else:
                return visitor.visitChildren(self)




    def exp4(self):

        localctx = BKITParser.Exp4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_exp4)
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.match(BKITParser.NOT)
                self.state = 355
                self.exp4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBDOT, BKITParser.LP, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.exp5()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def SUBDOT(self):
            return self.getToken(BKITParser.SUBDOT, 0)

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp5" ):
                return visitor.visitExp5(self)
            else:
                return visitor.visitChildren(self)




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 362
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBDOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 360
                self.exp5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
                self.exp6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def op_index(self):
            return self.getTypedRuleContext(BKITParser.Op_indexContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp6" ):
                return visitor.visitExp6(self)
            else:
                return visitor.visitChildren(self)



    def exp6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.operands()
            self._ctx.stop = self._input.LT(-1)
            self.state = 371
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.op_index() 
                self.state = 373
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Op_indexContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_op_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp_index" ):
                return visitor.visitOp_index(self)
            else:
                return visitor.visitChildren(self)




    def op_index(self):

        localctx = BKITParser.Op_indexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_op_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(BKITParser.LSB)
            self.state = 375
            self.exp()
            self.state = 376
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperands" ):
                return visitor.visitOperands(self)
            else:
                return visitor.visitChildren(self)




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_operands)
        try:
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.match(BKITParser.LP)
                self.state = 379
                self.exp()
                self.state = 380
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 383
                self.all_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 384
                self.match(BKITParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(BKITParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def TRUE(self):
            return self.getToken(BKITParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(BKITParser.FALSE, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_all_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_lit" ):
                return visitor.visitAll_lit(self)
            else:
                return visitor.visitChildren(self)




    def all_lit(self):

        localctx = BKITParser.All_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_all_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            _la = self._input.LA(1)
            if not(((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[30] = self.exp1_sempred
        self._predicates[31] = self.exp2_sempred
        self._predicates[32] = self.exp3_sempred
        self._predicates[35] = self.exp6_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exp6_sempred(self, localctx:Exp6Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




