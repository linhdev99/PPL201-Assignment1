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

main: stmt*;
var_declare_stmt: var_single
                | var_list;

var_single: var_normal SEMI;
          //( var_declare_normal
          //| var_normal
          //) SEMI;

var_list: VAR COLON var_vt SEMI BODY COLON var_single+ ENDBODY DOT;

//var_declare_normal: VAR COLON var_normal;
var_normal: (VAR COLON)? var_vt (EQ var_vp (COMMA var_vp)*)?;

var_vt: array_vt (COMMA array_vt)*;
var_vp: list_value
      | array_vp;
list_value: var_vp_int
          | var_vp_float
          | var_vp_string
          | array_vt;
list_value_sb: var_vp_int
             | array_vt
             | ID LP list_value RP;

var_vp_int: INTLIT;
var_vp_float: FLOATLIT;
var_vp_string: STRINGLIT;

array_vt: ID sb_value*;
array_vp: (cb_value | LCB cb_value (COMMA cb_value)+ RCB);

sb_value: LSB list_value_sb (COMMA list_value_sb)* RSB;
cb_value: LCB var_vp (COMMA var_vp)* RCB;

func_declare: FUNCTION COLON ID parameter_func body_declare;
parameter_func: PARAMETER COLON var_parameter (COMMA var_parameter)*;
var_parameter: ID sb_value?;

/**
 * 6 Statements and Control Flow
 */
stmt: var_declare_stmt
    | func_declare;

body_declare: BODY COLON stmt* ENDBODY DOT;

fragment DIGIT: [0-9];
fragment DEC:   '0' | [1-9] DIGIT*;
fragment HEX:   ('0x'|'0X')[0-9A-F]+;
fragment OCT:   ('0o'|'0O')[0-7]+;
fragment EXP:   [eE];
fragment EXPONENT: EXP [+-]? DIGIT+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
BCMT: ('**' .*? '**') -> skip; // Block comment

// 3.3.2 Keywords
//keywords: BODY | BREAK | CONTINUE | DO | ELSE | ELSEIF | ENDBODY
//        | ENDIF | ENDFOR | ENDWHILE | FOR | FUNCTION | IF | PARAMETER
//        | RETURN | THEN | VAR | WHILE | TRUE | FALSE | ENDDO;

//Method
FUNCTION: 'F' U N C T I O N;
PARAMETER: 'P' A R A M E T E R;
//Scope
BODY: 'B' O D Y;
ENDBODY: 'E' N D B O D Y;
//Flow Statement
IF: 'I' F;
THEN: 'T' H E N;
ELSEIF: 'E' L S E I F;
ELSE: 'E' L S E;
ENDIF: 'E' N D I F;
//Loop Statement
FOR: 'F' O R;
ENDFOR: 'E' N D F O R;
DO: 'D' O;
ENDDO: 'E' N D D O;
WHILE: 'W' H I L E;
ENDWHILE: 'E' N D W H I L E;
//Stop Statement
RETURN: 'R' E T U R N;
BREAK: 'B' R E A K;
CONTINUE: 'C' O N T I N U E;
//Value
TRUE: 'T' R U E;
FALSE: 'F' A L S E;
//Others
VAR: 'V' A R;

/**
// 3.3.3 Operator
*/

//OPERATORRRR: BOOL_OPERATOR | ARITHMETIC_OPERATOR | RELATIONAL_OPERATOR;

// Boolean operators
//BOOL_OPERATOR: NOT | AND | OR;

NOT: '!';
AND: '&&';
OR: '||';

// Arithmetic operators
//ARITHMETIC_OPERATOR: ADD | SUB | MUL | DIV | MOD | ADDDOT | SUBDOT | MULDOT | DIVDOT;
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
//RELATIONAL_OPERATOR: RELATIONAL_OPERATOR_INT | RELATIONAL_OPERATOR_FLOAT;

// Integer
//RELATIONAL_OPERATOR_INT: EQINT | NEQINT | LTINT | LTEINT | GTINT | GTEINT;
EQ: '=';

EQINT: EQ EQ;
NEQINT: NOT EQ;
LTINT : '<' ;
LTEINT: LTINT EQ;
GTINT : '>' ;
GTEINT: GTINT EQ;

// Float
//RELATIONAL_OPERATOR_FLOAT: NEQF | LTF | LTEF | GTF| GTEF;

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
DOT: '.';

// 3.3.5 Literals

// Integer
INTLIT: (ADD|SUB)? (DEC | HEX | OCT);

// FLoat
FLOATLIT:   (ADD|SUB)?
        (   DIGIT+ DOT EXPONENT
        |   DIGIT+ EXPONENT
        |   DIGIT* DOT (DIGIT+ EXPONENT?)?
        );

// Bool
BOOLEANLIT: TRUE | FALSE;

// 3.3.1 Identifiers
ID: [a-z][a-zA-Z0-9]* ;

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;
ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		value = str(self.text)
		raise IllegalEscape(value[1:])
	}
	;
UNCLOSE_STRING: '"' STR_CHAR* ([\n] | EOF)
	{
		value = str(self.text)
		possible = ['\n']
		if value[-1] in possible:
			raise UncloseString(value[1:-1])
		else:
			raise UncloseString(value[1:])
	}
	;
UNTERMINATED_COMMENT: '**' UNT_CMT* '*'?
    {
        raise UnterminatedComment()
    };

// String
STRINGLIT: '"' STR_CHAR* '"'
    {
		value = str(self.text)
		self.text = value[1:-1]
	};

fragment STR_CHAR: ~[\b\f\r\n\t"'\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"' ;
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\];
fragment UNT_CMT: ~[*] ;

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
