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
        buf.write("\u01c9\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\3")
        buf.write("\2\3\2\3\2\3\3\7\3a\n\3\f\3\16\3d\13\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\6\7\6p\n\6\f\6\16\6s\13\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7{\n\7\5\7}\n\7\3\b\3\b\3\b\5\b\u0082")
        buf.write("\n\b\3\t\3\t\3\t\3\t\7\t\u0088\n\t\f\t\16\t\u008b\13\t")
        buf.write("\5\t\u008d\n\t\3\t\3\t\3\n\3\n\3\n\5\n\u0094\n\n\3\13")
        buf.write("\3\13\3\13\3\13\7\13\u009a\n\13\f\13\16\13\u009d\13\13")
        buf.write("\5\13\u009f\n\13\3\13\3\13\3\f\3\f\5\f\u00a5\n\f\3\r\3")
        buf.write("\r\5\r\u00a9\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00b0\n")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00b9\n\17")
        buf.write("\3\20\3\20\3\20\7\20\u00be\n\20\f\20\16\20\u00c1\13\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u00ca\n\21\5")
        buf.write("\21\u00cc\n\21\3\21\7\21\u00cf\n\21\f\21\16\21\u00d2\13")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u00db\n\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u00e4\n\23\f")
        buf.write("\23\16\23\u00e7\13\23\3\24\3\24\3\24\3\24\7\24\u00ed\n")
        buf.write("\24\f\24\16\24\u00f0\13\24\3\24\7\24\u00f3\n\24\f\24\16")
        buf.write("\24\u00f6\13\24\3\24\5\24\u00f9\n\24\3\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\7\25\u0102\n\25\f\25\16\25\u0105\13")
        buf.write("\25\3\26\3\26\7\26\u0109\n\26\f\26\16\26\u010c\13\26\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\7\27\u011a\n\27\f\27\16\27\u011d\13\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\7\30\u0124\n\30\f\30\16\30\u0127\13\30")
        buf.write("\3\31\3\31\3\31\6\31\u012c\n\31\r\31\16\31\u012d\3\31")
        buf.write("\3\31\3\32\3\32\7\32\u0134\n\32\f\32\16\32\u0137\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\7\36\u0145\n\36\f\36\16\36\u0148\13\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\7\37\u014f\n\37\f\37\16\37\u0152\13\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\5\"\u0163\n\"\3\"\3\"\3#\3#\3#\3#\5#\u016b\n#\3")
        buf.write("#\3#\3#\5#\u0170\n#\7#\u0172\n#\f#\16#\u0175\13#\5#\u0177")
        buf.write("\n#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\5%\u0183\n%\3&\3&\3")
        buf.write("&\3&\3&\3&\7&\u018b\n&\f&\16&\u018e\13&\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\7\'\u0196\n\'\f\'\16\'\u0199\13\'\3(\3(\3(")
        buf.write("\3(\3(\3(\7(\u01a1\n(\f(\16(\u01a4\13(\3)\3)\3)\5)\u01a9")
        buf.write("\n)\3*\3*\3*\5*\u01ae\n*\3+\3+\3+\3+\3+\7+\u01b5\n+\f")
        buf.write("+\16+\u01b8\13+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\5-\u01c5")
        buf.write("\n-\3.\3.\3.\2\6JLNT/\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\2\7\3\2")
        buf.write("\36\37\4\2 !%&\4\2\"$\'(\4\2!!&&\5\2\32\33?@EE\2\u01d7")
        buf.write("\2\\\3\2\2\2\4b\3\2\2\2\6e\3\2\2\2\bg\3\2\2\2\nj\3\2\2")
        buf.write("\2\ft\3\2\2\2\16\u0081\3\2\2\2\20\u0083\3\2\2\2\22\u0093")
        buf.write("\3\2\2\2\24\u0095\3\2\2\2\26\u00a4\3\2\2\2\30\u00a8\3")
        buf.write("\2\2\2\32\u00af\3\2\2\2\34\u00b8\3\2\2\2\36\u00ba\3\2")
        buf.write("\2\2 \u00cb\3\2\2\2\"\u00d6\3\2\2\2$\u00de\3\2\2\2&\u00e8")
        buf.write("\3\2\2\2(\u00fd\3\2\2\2*\u0106\3\2\2\2,\u010d\3\2\2\2")
        buf.write(".\u0121\3\2\2\2\60\u0128\3\2\2\2\62\u0131\3\2\2\2\64\u0138")
        buf.write("\3\2\2\2\66\u013c\3\2\2\28\u013e\3\2\2\2:\u0140\3\2\2")
        buf.write("\2<\u014c\3\2\2\2>\u0158\3\2\2\2@\u015b\3\2\2\2B\u015e")
        buf.write("\3\2\2\2D\u0166\3\2\2\2F\u017a\3\2\2\2H\u0182\3\2\2\2")
        buf.write("J\u0184\3\2\2\2L\u018f\3\2\2\2N\u019a\3\2\2\2P\u01a8\3")
        buf.write("\2\2\2R\u01ad\3\2\2\2T\u01af\3\2\2\2V\u01b9\3\2\2\2X\u01c4")
        buf.write("\3\2\2\2Z\u01c6\3\2\2\2\\]\5\4\3\2]^\7\2\2\3^\3\3\2\2")
        buf.write("\2_a\5\30\r\2`_\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3\2\2\2")
        buf.write("c\5\3\2\2\2db\3\2\2\2ef\5\b\5\2f\7\3\2\2\2gh\5\n\6\2h")
        buf.write("i\7;\2\2i\t\3\2\2\2jk\7\34\2\2kl\7<\2\2lq\5\f\7\2mn\7")
        buf.write("=\2\2np\5\f\7\2om\3\2\2\2ps\3\2\2\2qo\3\2\2\2qr\3\2\2")
        buf.write("\2r\13\3\2\2\2sq\3\2\2\2t|\5\62\32\2uz\7)\2\2v{\5\24\13")
        buf.write("\2w{\5\62\32\2x{\5Z.\2y{\5D#\2zv\3\2\2\2zw\3\2\2\2zx\3")
        buf.write("\2\2\2zy\3\2\2\2{}\3\2\2\2|u\3\2\2\2|}\3\2\2\2}\r\3\2")
        buf.write("\2\2~\u0082\5\20\t\2\177\u0082\5.\30\2\u0080\u0082\5H")
        buf.write("%\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3\2\2")
        buf.write("\2\u0082\17\3\2\2\2\u0083\u008c\7\67\2\2\u0084\u0089\5")
        buf.write("\16\b\2\u0085\u0086\7=\2\2\u0086\u0088\5\16\b\2\u0087")
        buf.write("\u0085\3\2\2\2\u0088\u008b\3\2\2\2\u0089\u0087\3\2\2\2")
        buf.write("\u0089\u008a\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3")
        buf.write("\2\2\2\u008c\u0084\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008e")
        buf.write("\3\2\2\2\u008e\u008f\78\2\2\u008f\21\3\2\2\2\u0090\u0094")
        buf.write("\5\24\13\2\u0091\u0094\5.\30\2\u0092\u0094\5Z.\2\u0093")
        buf.write("\u0090\3\2\2\2\u0093\u0091\3\2\2\2\u0093\u0092\3\2\2\2")
        buf.write("\u0094\23\3\2\2\2\u0095\u009e\7\67\2\2\u0096\u009b\5\22")
        buf.write("\n\2\u0097\u0098\7=\2\2\u0098\u009a\5\22\n\2\u0099\u0097")
        buf.write("\3\2\2\2\u009a\u009d\3\2\2\2\u009b\u0099\3\2\2\2\u009b")
        buf.write("\u009c\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009e\u0096\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0\3")
        buf.write("\2\2\2\u00a0\u00a1\78\2\2\u00a1\25\3\2\2\2\u00a2\u00a5")
        buf.write("\5\32\16\2\u00a3\u00a5\5\34\17\2\u00a4\u00a2\3\2\2\2\u00a4")
        buf.write("\u00a3\3\2\2\2\u00a5\27\3\2\2\2\u00a6\u00a9\5\6\4\2\u00a7")
        buf.write("\u00a9\5\"\22\2\u00a8\u00a6\3\2\2\2\u00a8\u00a7\3\2\2")
        buf.write("\2\u00a9\31\3\2\2\2\u00aa\u00b0\5\6\4\2\u00ab\u00b0\5")
        buf.write("&\24\2\u00ac\u00b0\5,\27\2\u00ad\u00b0\5:\36\2\u00ae\u00b0")
        buf.write("\5<\37\2\u00af\u00aa\3\2\2\2\u00af\u00ab\3\2\2\2\u00af")
        buf.write("\u00ac\3\2\2\2\u00af\u00ad\3\2\2\2\u00af\u00ae\3\2\2\2")
        buf.write("\u00b0\33\3\2\2\2\u00b1\u00b2\5 \21\2\u00b2\u00b3\7;\2")
        buf.write("\2\u00b3\u00b9\3\2\2\2\u00b4\u00b9\5> \2\u00b5\u00b9\5")
        buf.write("@!\2\u00b6\u00b9\5B\"\2\u00b7\u00b9\5F$\2\u00b8\u00b1")
        buf.write("\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\35\3\2\2\2\u00ba")
        buf.write("\u00bb\7\n\2\2\u00bb\u00bf\7<\2\2\u00bc\u00be\5\26\f\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00be\u00c1\3\2\2\2\u00bf\u00bd\3")
        buf.write("\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c3\7\13\2\2\u00c3\u00c4\7>\2\2\u00c4")
        buf.write("\37\3\2\2\2\u00c5\u00cc\5.\30\2\u00c6\u00ca\5D#\2\u00c7")
        buf.write("\u00ca\7E\2\2\u00c8\u00ca\5\20\t\2\u00c9\u00c6\3\2\2\2")
        buf.write("\u00c9\u00c7\3\2\2\2\u00c9\u00c8\3\2\2\2\u00ca\u00cc\3")
        buf.write("\2\2\2\u00cb\u00c5\3\2\2\2\u00cb\u00c9\3\2\2\2\u00cc\u00d0")
        buf.write("\3\2\2\2\u00cd\u00cf\5\60\31\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\u00d2\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2")
        buf.write("\u00d1\u00d3\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d3\u00d4\7")
        buf.write(")\2\2\u00d4\u00d5\5\16\b\2\u00d5!\3\2\2\2\u00d6\u00d7")
        buf.write("\7\b\2\2\u00d7\u00d8\7<\2\2\u00d8\u00da\7A\2\2\u00d9\u00db")
        buf.write("\5$\23\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dc\3\2\2\2\u00dc\u00dd\5\36\20\2\u00dd#\3\2\2\2\u00de")
        buf.write("\u00df\7\t\2\2\u00df\u00e0\7<\2\2\u00e0\u00e5\5\62\32")
        buf.write("\2\u00e1\u00e2\7=\2\2\u00e2\u00e4\5\62\32\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e4\u00e7\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6%\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e8")
        buf.write("\u00e9\7\f\2\2\u00e9\u00ea\5H%\2\u00ea\u00ee\7\r\2\2\u00eb")
        buf.write("\u00ed\5\26\f\2\u00ec\u00eb\3\2\2\2\u00ed\u00f0\3\2\2")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f4")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f1\u00f3\5(\25\2\u00f2")
        buf.write("\u00f1\3\2\2\2\u00f3\u00f6\3\2\2\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f5\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f7\u00f9\5*\26\2\u00f8\u00f7\3\2\2\2\u00f8\u00f9")
        buf.write("\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\7\20\2\2\u00fb")
        buf.write("\u00fc\7>\2\2\u00fc\'\3\2\2\2\u00fd\u00fe\7\16\2\2\u00fe")
        buf.write("\u00ff\5H%\2\u00ff\u0103\7\r\2\2\u0100\u0102\5\26\f\2")
        buf.write("\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3")
        buf.write("\2\2\2\u0103\u0104\3\2\2\2\u0104)\3\2\2\2\u0105\u0103")
        buf.write("\3\2\2\2\u0106\u010a\7\17\2\2\u0107\u0109\5\26\f\2\u0108")
        buf.write("\u0107\3\2\2\2\u0109\u010c\3\2\2\2\u010a\u0108\3\2\2\2")
        buf.write("\u010a\u010b\3\2\2\2\u010b+\3\2\2\2\u010c\u010a\3\2\2")
        buf.write("\2\u010d\u010e\7\21\2\2\u010e\u010f\7\65\2\2\u010f\u0110")
        buf.write("\7A\2\2\u0110\u0111\7)\2\2\u0111\u0112\5H%\2\u0112\u0113")
        buf.write("\7=\2\2\u0113\u0114\5\66\34\2\u0114\u0115\7=\2\2\u0115")
        buf.write("\u0116\58\35\2\u0116\u0117\7\66\2\2\u0117\u011b\7\23\2")
        buf.write("\2\u0118\u011a\5\26\f\2\u0119\u0118\3\2\2\2\u011a\u011d")
        buf.write("\3\2\2\2\u011b\u0119\3\2\2\2\u011b\u011c\3\2\2\2\u011c")
        buf.write("\u011e\3\2\2\2\u011d\u011b\3\2\2\2\u011e\u011f\7\22\2")
        buf.write("\2\u011f\u0120\7>\2\2\u0120-\3\2\2\2\u0121\u0125\7A\2")
        buf.write("\2\u0122\u0124\5\60\31\2\u0123\u0122\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("/\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012b\79\2\2\u0129")
        buf.write("\u012c\5.\30\2\u012a\u012c\5H%\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012d\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u0130\7")
        buf.write(":\2\2\u0130\61\3\2\2\2\u0131\u0135\7A\2\2\u0132\u0134")
        buf.write("\5\64\33\2\u0133\u0132\3\2\2\2\u0134\u0137\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0135\u0136\3\2\2\2\u0136\63\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0138\u0139\79\2\2\u0139\u013a\7?\2\2\u013a")
        buf.write("\u013b\7:\2\2\u013b\65\3\2\2\2\u013c\u013d\5H%\2\u013d")
        buf.write("\67\3\2\2\2\u013e\u013f\5H%\2\u013f9\3\2\2\2\u0140\u0141")
        buf.write("\7\25\2\2\u0141\u0142\5H%\2\u0142\u0146\7\23\2\2\u0143")
        buf.write("\u0145\5\26\f\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2")
        buf.write("\2\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0149")
        buf.write("\3\2\2\2\u0148\u0146\3\2\2\2\u0149\u014a\7\26\2\2\u014a")
        buf.write("\u014b\7>\2\2\u014b;\3\2\2\2\u014c\u0150\7\23\2\2\u014d")
        buf.write("\u014f\5\26\f\2\u014e\u014d\3\2\2\2\u014f\u0152\3\2\2")
        buf.write("\2\u0150\u014e\3\2\2\2\u0150\u0151\3\2\2\2\u0151\u0153")
        buf.write("\3\2\2\2\u0152\u0150\3\2\2\2\u0153\u0154\7\25\2\2\u0154")
        buf.write("\u0155\5H%\2\u0155\u0156\7\24\2\2\u0156\u0157\7>\2\2\u0157")
        buf.write("=\3\2\2\2\u0158\u0159\7\30\2\2\u0159\u015a\7;\2\2\u015a")
        buf.write("?\3\2\2\2\u015b\u015c\7\31\2\2\u015c\u015d\7;\2\2\u015d")
        buf.write("A\3\2\2\2\u015e\u0162\7\27\2\2\u015f\u0163\5.\30\2\u0160")
        buf.write("\u0163\5Z.\2\u0161\u0163\5H%\2\u0162\u015f\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0162\u0161\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0164\3\2\2\2\u0164\u0165\7;\2\2\u0165C\3\2\2\2")
        buf.write("\u0166\u0167\7A\2\2\u0167\u0176\7\65\2\2\u0168\u016b\5")
        buf.write("H%\2\u0169\u016b\5\16\b\2\u016a\u0168\3\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016b\u0173\3\2\2\2\u016c\u016f\7=\2\2\u016d")
        buf.write("\u0170\5H%\2\u016e\u0170\5\16\b\2\u016f\u016d\3\2\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170\u0172\3\2\2\2\u0171\u016c\3")
        buf.write("\2\2\2\u0172\u0175\3\2\2\2\u0173\u0171\3\2\2\2\u0173\u0174")
        buf.write("\3\2\2\2\u0174\u0177\3\2\2\2\u0175\u0173\3\2\2\2\u0176")
        buf.write("\u016a\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u0178\3\2\2\2")
        buf.write("\u0178\u0179\7\66\2\2\u0179E\3\2\2\2\u017a\u017b\5D#\2")
        buf.write("\u017b\u017c\7;\2\2\u017cG\3\2\2\2\u017d\u017e\5J&\2\u017e")
        buf.write("\u017f\7\3\2\2\u017f\u0180\5J&\2\u0180\u0183\3\2\2\2\u0181")
        buf.write("\u0183\5J&\2\u0182\u017d\3\2\2\2\u0182\u0181\3\2\2\2\u0183")
        buf.write("I\3\2\2\2\u0184\u0185\b&\1\2\u0185\u0186\5L\'\2\u0186")
        buf.write("\u018c\3\2\2\2\u0187\u0188\f\4\2\2\u0188\u0189\t\2\2\2")
        buf.write("\u0189\u018b\5L\'\2\u018a\u0187\3\2\2\2\u018b\u018e\3")
        buf.write("\2\2\2\u018c\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dK")
        buf.write("\3\2\2\2\u018e\u018c\3\2\2\2\u018f\u0190\b\'\1\2\u0190")
        buf.write("\u0191\5N(\2\u0191\u0197\3\2\2\2\u0192\u0193\f\4\2\2\u0193")
        buf.write("\u0194\t\3\2\2\u0194\u0196\5N(\2\u0195\u0192\3\2\2\2\u0196")
        buf.write("\u0199\3\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2")
        buf.write("\u0198M\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\b(\1\2")
        buf.write("\u019b\u019c\5P)\2\u019c\u01a2\3\2\2\2\u019d\u019e\f\4")
        buf.write("\2\2\u019e\u019f\t\4\2\2\u019f\u01a1\5P)\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2")
        buf.write("\u01a3\3\2\2\2\u01a3O\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5")
        buf.write("\u01a6\7\35\2\2\u01a6\u01a9\5P)\2\u01a7\u01a9\5R*\2\u01a8")
        buf.write("\u01a5\3\2\2\2\u01a8\u01a7\3\2\2\2\u01a9Q\3\2\2\2\u01aa")
        buf.write("\u01ab\t\5\2\2\u01ab\u01ae\5R*\2\u01ac\u01ae\5T+\2\u01ad")
        buf.write("\u01aa\3\2\2\2\u01ad\u01ac\3\2\2\2\u01aeS\3\2\2\2\u01af")
        buf.write("\u01b0\b+\1\2\u01b0\u01b1\5X-\2\u01b1\u01b6\3\2\2\2\u01b2")
        buf.write("\u01b3\f\4\2\2\u01b3\u01b5\5V,\2\u01b4\u01b2\3\2\2\2\u01b5")
        buf.write("\u01b8\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2")
        buf.write("\u01b7U\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b9\u01ba\79\2\2")
        buf.write("\u01ba\u01bb\5H%\2\u01bb\u01bc\7:\2\2\u01bcW\3\2\2\2\u01bd")
        buf.write("\u01be\7\65\2\2\u01be\u01bf\5H%\2\u01bf\u01c0\7\66\2\2")
        buf.write("\u01c0\u01c5\3\2\2\2\u01c1\u01c5\5D#\2\u01c2\u01c5\5Z")
        buf.write(".\2\u01c3\u01c5\7A\2\2\u01c4\u01bd\3\2\2\2\u01c4\u01c1")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("Y\3\2\2\2\u01c6\u01c7\t\6\2\2\u01c7[\3\2\2\2/bqz|\u0081")
        buf.write("\u0089\u008c\u0093\u009b\u009e\u00a4\u00a8\u00af\u00b8")
        buf.write("\u00bf\u00c9\u00cb\u00d0\u00da\u00e5\u00ee\u00f4\u00f8")
        buf.write("\u0103\u010a\u011b\u0125\u012b\u012d\u0135\u0146\u0150")
        buf.write("\u0162\u016a\u016f\u0173\u0176\u0182\u018c\u0197\u01a2")
        buf.write("\u01a8\u01ad\u01b6\u01c4")
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
    RULE_var_normal = 4
    RULE_var_normal_list = 5
    RULE_var_vp = 6
    RULE_array_vp = 7
    RULE_var_vp_noexp = 8
    RULE_array_vp_noexp = 9
    RULE_stmt = 10
    RULE_stmt_decl = 11
    RULE_stmt_notfunc = 12
    RULE_stmt_spe = 13
    RULE_body_declare = 14
    RULE_assign_stmt = 15
    RULE_func_declare = 16
    RULE_parameter_func = 17
    RULE_if_stmt = 18
    RULE_elseif_stmt = 19
    RULE_else_stmt = 20
    RULE_for_stmt = 21
    RULE_scalar_var = 22
    RULE_index_var = 23
    RULE_scalar_var_int = 24
    RULE_index_var_int = 25
    RULE_conditionExpr = 26
    RULE_updateExpr = 27
    RULE_while_stmt = 28
    RULE_doWhile_stmt = 29
    RULE_break_stmt = 30
    RULE_continue_stmt = 31
    RULE_return_stmt = 32
    RULE_func_call = 33
    RULE_call_stmt = 34
    RULE_exp = 35
    RULE_exp1 = 36
    RULE_exp2 = 37
    RULE_exp3 = 38
    RULE_exp4 = 39
    RULE_exp5 = 40
    RULE_exp6 = 41
    RULE_op_index = 42
    RULE_operands = 43
    RULE_all_lit = 44

    ruleNames =  [ "program", "main", "var_declare_stmt", "var_single", 
                   "var_normal", "var_normal_list", "var_vp", "array_vp", 
                   "var_vp_noexp", "array_vp_noexp", "stmt", "stmt_decl", 
                   "stmt_notfunc", "stmt_spe", "body_declare", "assign_stmt", 
                   "func_declare", "parameter_func", "if_stmt", "elseif_stmt", 
                   "else_stmt", "for_stmt", "scalar_var", "index_var", "scalar_var_int", 
                   "index_var_int", "conditionExpr", "updateExpr", "while_stmt", 
                   "doWhile_stmt", "break_stmt", "continue_stmt", "return_stmt", 
                   "func_call", "call_stmt", "exp", "exp1", "exp2", "exp3", 
                   "exp4", "exp5", "exp6", "op_index", "operands", "all_lit" ]

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
            self.state = 90
            self.main()
            self.state = 91
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

        def stmt_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Stmt_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Stmt_declContext,i)


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
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION or _la==BKITParser.VAR:
                self.state = 93
                self.stmt_decl()
                self.state = 98
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
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.var_single()
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
            self.state = 101
            self.var_normal()
            self.state = 102
            self.match(BKITParser.SEMI)
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
            return BKITParser.RULE_var_normal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal" ):
                return visitor.visitVar_normal(self)
            else:
                return visitor.visitChildren(self)




    def var_normal(self):

        localctx = BKITParser.Var_normalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_normal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BKITParser.VAR)
            self.state = 105
            self.match(BKITParser.COLON)
            self.state = 106
            self.var_normal_list()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 107
                self.match(BKITParser.COMMA)
                self.state = 108
                self.var_normal_list()
                self.state = 113
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

        def scalar_var_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_var_intContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_var_intContext,i)


        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def array_vp_noexp(self):
            return self.getTypedRuleContext(BKITParser.Array_vp_noexpContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_normal_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_normal_list" ):
                return visitor.visitVar_normal_list(self)
            else:
                return visitor.visitChildren(self)




    def var_normal_list(self):

        localctx = BKITParser.Var_normal_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_normal_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.scalar_var_int()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.EQ:
                self.state = 115
                self.match(BKITParser.EQ)
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 116
                    self.array_vp_noexp()
                    pass

                elif la_ == 2:
                    self.state = 117
                    self.scalar_var_int()
                    pass

                elif la_ == 3:
                    self.state = 118
                    self.all_lit()
                    pass

                elif la_ == 4:
                    self.state = 119
                    self.func_call()
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
        self.enterRule(localctx, 12, self.RULE_var_vp)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.array_vp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.scalar_var()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
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

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def var_vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vpContext,i)


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
        self.enterRule(localctx, 14, self.RULE_array_vp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.LCB)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 130
                self.var_vp()
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 131
                    self.match(BKITParser.COMMA)
                    self.state = 132
                    self.var_vp()
                    self.state = 137
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 140
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_vp_noexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_vp_noexp(self):
            return self.getTypedRuleContext(BKITParser.Array_vp_noexpContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def all_lit(self):
            return self.getTypedRuleContext(BKITParser.All_litContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_vp_noexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_vp_noexp" ):
                return visitor.visitVar_vp_noexp(self)
            else:
                return visitor.visitChildren(self)




    def var_vp_noexp(self):

        localctx = BKITParser.Var_vp_noexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_vp_noexp)
        try:
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.array_vp_noexp()
                pass
            elif token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.scalar_var()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 144
                self.all_lit()
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


    class Array_vp_noexpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def var_vp_noexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vp_noexpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vp_noexpContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_vp_noexp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_vp_noexp" ):
                return visitor.visitArray_vp_noexp(self)
            else:
                return visitor.visitChildren(self)




    def array_vp_noexp(self):

        localctx = BKITParser.Array_vp_noexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_vp_noexp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(BKITParser.LCB)
            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 148
                self.var_vp_noexp()
                self.state = 153
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 149
                    self.match(BKITParser.COMMA)
                    self.state = 150
                    self.var_vp_noexp()
                    self.state = 155
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 158
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

        def stmt_notfunc(self):
            return self.getTypedRuleContext(BKITParser.Stmt_notfuncContext,0)


        def stmt_spe(self):
            return self.getTypedRuleContext(BKITParser.Stmt_speContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stmt)
        try:
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.IF, BKITParser.FOR, BKITParser.DO, BKITParser.WHILE, BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.stmt_notfunc()
                pass
            elif token in [BKITParser.RETURN, BKITParser.BREAK, BKITParser.CONTINUE, BKITParser.LCB, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.stmt_spe()
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


    class Stmt_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,0)


        def func_declare(self):
            return self.getTypedRuleContext(BKITParser.Func_declareContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_decl" ):
                return visitor.visitStmt_decl(self)
            else:
                return visitor.visitChildren(self)




    def stmt_decl(self):

        localctx = BKITParser.Stmt_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt_decl)
        try:
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.var_declare_stmt()
                pass
            elif token in [BKITParser.FUNCTION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 165
                self.func_declare()
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


    class Stmt_notfuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_declare_stmt(self):
            return self.getTypedRuleContext(BKITParser.Var_declare_stmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(BKITParser.If_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(BKITParser.For_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(BKITParser.While_stmtContext,0)


        def doWhile_stmt(self):
            return self.getTypedRuleContext(BKITParser.DoWhile_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_notfunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_notfunc" ):
                return visitor.visitStmt_notfunc(self)
            else:
                return visitor.visitChildren(self)




    def stmt_notfunc(self):

        localctx = BKITParser.Stmt_notfuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt_notfunc)
        try:
            self.state = 173
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.var_declare_stmt()
                pass
            elif token in [BKITParser.IF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.if_stmt()
                pass
            elif token in [BKITParser.FOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.for_stmt()
                pass
            elif token in [BKITParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.while_stmt()
                pass
            elif token in [BKITParser.DO]:
                self.enterOuterAlt(localctx, 5)
                self.state = 172
                self.doWhile_stmt()
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


    class Stmt_speContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_stmt(self):
            return self.getTypedRuleContext(BKITParser.Assign_stmtContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def break_stmt(self):
            return self.getTypedRuleContext(BKITParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(BKITParser.Continue_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKITParser.Return_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKITParser.Call_stmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt_spe

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_spe" ):
                return visitor.visitStmt_spe(self)
            else:
                return visitor.visitChildren(self)




    def stmt_spe(self):

        localctx = BKITParser.Stmt_speContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_spe)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                self.assign_stmt()
                self.state = 176
                self.match(BKITParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.break_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.continue_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.return_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.call_stmt()
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
        self.enterRule(localctx, 28, self.RULE_body_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(BKITParser.BODY)
            self.state = 185
            self.match(BKITParser.COLON)
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 186
                self.stmt()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 192
            self.match(BKITParser.ENDBODY)
            self.state = 193
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

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def var_vp(self):
            return self.getTypedRuleContext(BKITParser.Var_vpContext,0)


        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def index_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_varContext,i)


        def func_call(self):
            return self.getTypedRuleContext(BKITParser.Func_callContext,0)


        def STRINGLIT(self):
            return self.getToken(BKITParser.STRINGLIT, 0)

        def array_vp(self):
            return self.getTypedRuleContext(BKITParser.Array_vpContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = BKITParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 195
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 199
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.ID]:
                    self.state = 196
                    self.func_call()
                    pass
                elif token in [BKITParser.STRINGLIT]:
                    self.state = 197
                    self.match(BKITParser.STRINGLIT)
                    pass
                elif token in [BKITParser.LCB]:
                    self.state = 198
                    self.array_vp()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 203
                self.index_var()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 209
            self.match(BKITParser.EQ)
            self.state = 210
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
        self.enterRule(localctx, 32, self.RULE_func_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BKITParser.FUNCTION)
            self.state = 213
            self.match(BKITParser.COLON)
            self.state = 214
            self.match(BKITParser.ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 215
                self.parameter_func()


            self.state = 218
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

        def scalar_var_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_var_intContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_var_intContext,i)


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
        self.enterRule(localctx, 34, self.RULE_parameter_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BKITParser.PARAMETER)
            self.state = 221
            self.match(BKITParser.COLON)
            self.state = 222
            self.scalar_var_int()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 223
                self.match(BKITParser.COMMA)
                self.state = 224
                self.scalar_var_int()
                self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(BKITParser.IF)
            self.state = 231
            self.exp()
            self.state = 232
            self.match(BKITParser.THEN)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 233
                self.stmt()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 239
                self.elseif_stmt()
                self.state = 244
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 245
                self.else_stmt()


            self.state = 248
            self.match(BKITParser.ENDIF)
            self.state = 249
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
        self.enterRule(localctx, 38, self.RULE_elseif_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(BKITParser.ELSEIF)
            self.state = 252
            self.exp()
            self.state = 253
            self.match(BKITParser.THEN)
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 254
                self.stmt()
                self.state = 259
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
        self.enterRule(localctx, 40, self.RULE_else_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(BKITParser.ELSE)
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 261
                self.stmt()
                self.state = 266
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

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

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
        self.enterRule(localctx, 42, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(BKITParser.FOR)
            self.state = 268
            self.match(BKITParser.LP)
            self.state = 269
            self.match(BKITParser.ID)
            self.state = 270
            self.match(BKITParser.EQ)
            self.state = 271
            self.exp()
            self.state = 272
            self.match(BKITParser.COMMA)
            self.state = 273
            self.conditionExpr()
            self.state = 274
            self.match(BKITParser.COMMA)
            self.state = 275
            self.updateExpr()
            self.state = 276
            self.match(BKITParser.RP)
            self.state = 277
            self.match(BKITParser.DO)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 278
                self.stmt()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.match(BKITParser.ENDFOR)
            self.state = 285
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
        self.enterRule(localctx, 44, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(BKITParser.ID)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 288
                    self.index_var() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 46, self.RULE_index_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.match(BKITParser.LSB)
            self.state = 297 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 297
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 295
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 296
                    self.exp()
                    pass


                self.state = 299 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0)):
                    break

            self.state = 301
            self.match(BKITParser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_var_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_var_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Index_var_intContext)
            else:
                return self.getTypedRuleContext(BKITParser.Index_var_intContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar_var_int" ):
                return visitor.visitScalar_var_int(self)
            else:
                return visitor.visitChildren(self)




    def scalar_var_int(self):

        localctx = BKITParser.Scalar_var_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_scalar_var_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.match(BKITParser.ID)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 304
                self.index_var_int()
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_var_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(BKITParser.LSB, 0)

        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def RSB(self):
            return self.getToken(BKITParser.RSB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_index_var_int

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_var_int" ):
                return visitor.visitIndex_var_int(self)
            else:
                return visitor.visitChildren(self)




    def index_var_int(self):

        localctx = BKITParser.Index_var_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_index_var_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.match(BKITParser.LSB)
            self.state = 311
            self.match(BKITParser.INTLIT)
            self.state = 312
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
        self.enterRule(localctx, 52, self.RULE_conditionExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
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
        self.enterRule(localctx, 54, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
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
        self.enterRule(localctx, 56, self.RULE_while_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(BKITParser.WHILE)
            self.state = 319
            self.exp()
            self.state = 320
            self.match(BKITParser.DO)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & ((1 << (BKITParser.IF - 10)) | (1 << (BKITParser.FOR - 10)) | (1 << (BKITParser.DO - 10)) | (1 << (BKITParser.WHILE - 10)) | (1 << (BKITParser.RETURN - 10)) | (1 << (BKITParser.BREAK - 10)) | (1 << (BKITParser.CONTINUE - 10)) | (1 << (BKITParser.VAR - 10)) | (1 << (BKITParser.LCB - 10)) | (1 << (BKITParser.ID - 10)) | (1 << (BKITParser.STRINGLIT - 10)))) != 0):
                self.state = 321
                self.stmt()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 327
            self.match(BKITParser.ENDWHILE)
            self.state = 328
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
        self.enterRule(localctx, 58, self.RULE_doWhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(BKITParser.DO)
            self.state = 334
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 331
                    self.stmt() 
                self.state = 336
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 337
            self.match(BKITParser.WHILE)
            self.state = 338
            self.exp()
            self.state = 339
            self.match(BKITParser.ENDDO)
            self.state = 340
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
        self.enterRule(localctx, 60, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(BKITParser.BREAK)
            self.state = 343
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
        self.enterRule(localctx, 62, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BKITParser.CONTINUE)
            self.state = 346
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
        self.enterRule(localctx, 64, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BKITParser.RETURN)
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 349
                self.scalar_var()

            elif la_ == 2:
                self.state = 350
                self.all_lit()

            elif la_ == 3:
                self.state = 351
                self.exp()


            self.state = 354
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


        def var_vp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_vpContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_vpContext,i)


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
        self.enterRule(localctx, 66, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(BKITParser.ID)
            self.state = 357
            self.match(BKITParser.LP)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 24)) & ~0x3f) == 0 and ((1 << (_la - 24)) & ((1 << (BKITParser.TRUE - 24)) | (1 << (BKITParser.FALSE - 24)) | (1 << (BKITParser.NOT - 24)) | (1 << (BKITParser.SUB - 24)) | (1 << (BKITParser.SUBDOT - 24)) | (1 << (BKITParser.LP - 24)) | (1 << (BKITParser.LCB - 24)) | (1 << (BKITParser.INTLIT - 24)) | (1 << (BKITParser.FLOATLIT - 24)) | (1 << (BKITParser.ID - 24)) | (1 << (BKITParser.STRINGLIT - 24)))) != 0):
                self.state = 360
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 358
                    self.exp()
                    pass

                elif la_ == 2:
                    self.state = 359
                    self.var_vp()
                    pass


                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 362
                    self.match(BKITParser.COMMA)
                    self.state = 365
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                    if la_ == 1:
                        self.state = 363
                        self.exp()
                        pass

                    elif la_ == 2:
                        self.state = 364
                        self.var_vp()
                        pass


                    self.state = 371
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 374
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
        self.enterRule(localctx, 68, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.func_call()
            self.state = 377
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
        self.enterRule(localctx, 70, self.RULE_exp)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.exp1(0)
                self.state = 380
                self.match(BKITParser.RELATIONAL)
                self.state = 381
                self.exp1(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 383
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
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.exp2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.exp2(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.ADDDOT) | (1 << BKITParser.SUBDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.exp3(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exp4()
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.MULDOT) | (1 << BKITParser.DIVDOT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.exp4() 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 78, self.RULE_exp4)
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.match(BKITParser.NOT)
                self.state = 420
                self.exp4()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.SUB, BKITParser.SUBDOT, BKITParser.LP, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
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
        self.enterRule(localctx, 80, self.RULE_exp5)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.SUBDOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.SUBDOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 425
                self.exp5()
                pass
            elif token in [BKITParser.TRUE, BKITParser.FALSE, BKITParser.LP, BKITParser.INTLIT, BKITParser.FLOATLIT, BKITParser.ID, BKITParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exp6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.operands()
            self._ctx.stop = self._input.LT(-1)
            self.state = 436
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp6)
                    self.state = 432
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 433
                    self.op_index() 
                self.state = 438
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_op_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(BKITParser.LSB)
            self.state = 440
            self.exp()
            self.state = 441
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
        self.enterRule(localctx, 86, self.RULE_operands)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(BKITParser.LP)
                self.state = 444
                self.exp()
                self.state = 445
                self.match(BKITParser.RP)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.func_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 448
                self.all_lit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
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
        self.enterRule(localctx, 88, self.RULE_all_lit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
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
        self._predicates[36] = self.exp1_sempred
        self._predicates[37] = self.exp2_sempred
        self._predicates[38] = self.exp3_sempred
        self._predicates[41] = self.exp6_sempred
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
         




