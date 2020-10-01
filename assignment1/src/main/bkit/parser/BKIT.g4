grammar BKIT;

//Student ID 1710165;
@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

//program  : VAR COLON ID SEMI EOF ;
program: main EOF;

main: VAR COLON ID SEMI;

fragment DIGIT: [0-9];
fragment DEC:   [1-9] DIGIT+;
fragment HEX:   ('0x'|'0X')[0-9A-F]+;
fragment OCT:   ('0o'|'0O')[0-7]+;
fragment EXP:   [eE];
fragment DOT:   '.';
fragment EXPONENT: EXP [+-]? DEC;

SEMI:       ';' ;
COLON:      ':' ;

VAR:        'Var' ;

WS:         [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

//KEYWORD:    'Body'|'Break'|'Continue'|'Do'
//            |'Else'|'ElseIf'|'EndBody'|'EndIf'
//            |'EndFor'|'EndWhile'|'For'|'Function'
//            |'If'|'Parameter'|'Return'|'Then'
//            |'Var'|'While'|'True'|'False'
//            |'EndDo';

BODY: 'Body'

OPERATOR:   '+'|'+.'|'-'|'-.'
            |'*'|'*.'|'\\'|'\\.'
            |'%'|'!'|'&&'|'||'
            |'=='|'!='|'<'|'>'
            |'<='|'>='|'=/='|'<.'
            |'>.'|'<=.'|'>=.';

//SEPARATOR:  '('|')'|'['|']'|':'|'.'|','|';'|'{'|'}';

ID: [a-z][a-zA-Z0-9]* ;

INT: DEC|HEX|OCT;

FLOAT: DEC EXPONENT;


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
