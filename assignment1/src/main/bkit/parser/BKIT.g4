/**
    Student ID 1710165;
*/
grammar BKIT;


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

main: var_declare;
var_declare: (var_normal | var_array)*?;

var_normal: VAR COLON ID (EQ (INTLIT | FLOATLIT | STRINGLIT)+)? SEMI;
var_array: VAR COLON ID array_vt+ EQ (array_vp | LCB array_vp (COMMA array_vp)+ RCB) SEMI; //Chưa làm được
array_vt: LSB INTLIT (COMMA INTLIT)* RSB;
array_vp: LCB INTLIT (COMMA INTLIT)* RCB;

fragment DIGIT: [0-9];
fragment DEC:   '0' | [1-9] DIGIT*;
fragment HEX:   ('0x'|'0X')[0-9A-F]+;
fragment OCT:   ('0o'|'0O')[0-7]+;
fragment EXP:   [eE];
fragment EXPONENT: EXP [+-]? DIGIT+;
WS: [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines
BCMT: ('**' .*? '**') -> skip; // Block comment

// 3.3.2 Keywords
//keywords: BODY | BREAK | CONTINUE | DO | ELSE | ELSEIF | ENDBODY
//        | ENDIF | ENDFOR | ENDWHILE | FOR | FUNCTION | IF | PARAMETER
//        | RETURN | THEN | VAR | WHILE | TRUE | FALSE | ENDDO;

BODY: 'B' O D Y;
BREAK: 'B' R E A K;
CONTINUE: 'C' O N T I N U E;
DO: 'D' O;
ELSE: 'E' L S E;
ELSEIF: 'E' L S E I F;
ENDBODY: 'E' N D B O D Y;
ENDIF: 'E' N D I F;
ENDFOR: 'E' N D F O R;
ENDWHILE: 'E' N D W H I L E;
FOR: 'F' O R;
FUNCTION: 'F' U N C T I O N;
IF: 'I' F;
PARAMETER: 'P' A R A M E T E R;
RETURN: 'R' E T U R N;
THEN: 'T' H E N;
VAR: 'V' A R;
WHILE: 'W' H I L E;
TRUE: 'T' R U E;
FALSE: 'F' A L S E;
ENDDO: 'E' N D D O;

/**
// 3.3.3 Operator
*/

OPERATOR: BOOL_OPERATOR | ARITHMETIC_OPERATOR | RELATIONAL_OPERATOR;

// Boolean operators
BOOL_OPERATOR: NOT | AND | OR;

NOT: '!';
AND: '&&';
OR: '||';

// Arithmetic operators
ARITHMETIC_OPERATOR: ADD | SUB | MUL | DIV | MOD | ADDDOT | SUBDOT | MULDOT | DIVDOT;
// Integer

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';

// Float

ADDDOT: ADD DOT;
SUBDOT: SUB DOT;
MULDOT: MUL DOT;
DIVDOT: DIV DOT;

// Relational operators
RELATIONAL_OPERATOR: RELATIONAL_OPERATOR_INT | RELATIONAL_OPERATOR_FLOAT;

// Integer
RELATIONAL_OPERATOR_INT: EQINT | NEQINT | LTINT | LTEINT | GTINT | GTEINT;
EQ: '=';

EQINT: EQ EQ;
NEQINT: NOT EQ;
LTINT : '<' ;
LTEINT: LTINT EQ;
GTINT : '>' ;
GTEINT: GTINT EQ;

// Float
RELATIONAL_OPERATOR_FLOAT: NEQF | LTF | LTEF | GTF| GTEF;

NEQF: EQ '/' EQ;
LTF: LTINT DOT;
LTEF: LTINT EQ DOT;
GTF: GTINT DOT;
GTEF: GTF EQ;

// 3.3.4 SEPARATOR:  '('|')'|'['|']'|':'|'.'|','|';'|'{'|'}';
LP: '('; // Left Parenthesis
RP: ')'; // Right Parenthesis
LCB: '{'; // Left Curly Bracket
RCB: '}'; // Right Curly Bracket
LSB: '['; // Left Square Bracket
RSB: ']'; // Right Square Bracket
SEMI: ';' ;
COLON: ':' ;
COMMA: ',';
fragment DOT: '.';

// 3.3.5 Literals

// Integer
INTLIT: DEC | HEX | OCT;

// FLoat
FLOATLIT:   DIGIT+ DOT EXPONENT
        |   DIGIT+ EXPONENT
        |   DIGIT* DOT (DIGIT+ EXPONENT?)?;

// Bool
BOOLEANLIT: TRUE | FALSE;

// String
STRINGLIT: '"' STRCHAR* ( [\b\t\n\f\r"'\\] | EOF )'"';
fragment STRCHAR: ~[\t\f\r\n"];

// 3.3.1 Identifiers
ID: [a-z][a-zA-Z0-9]* ;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];
