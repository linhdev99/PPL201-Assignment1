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

program: main EOF;

main: stmt*;
var_declare_stmt: var_single
                | var_list;
var_single: var_normal SEMI;
var_list: VAR COLON var_vt SEMI BODY COLON var_single+ ENDBODY DOT;
var_normal: (VAR COLON)? var_normal_list (COMMA var_normal_list)*;
var_normal_list: var_vt (EQ var_vp)?;
var_vt: scalar_var (COMMA scalar_var)*;
var_vp: array_vp
      | scalar_var
      | exp;
array_vp: LCB var_vp (COMMA var_vp)* RCB;

/**
 * 6 Statements and Control Flow
 */
stmt: var_declare_stmt
    | func_declare
    | call_stmt
    | exp
    | if_stmt
    | for_stmt
    | while_stmt
    | doWhile_stmt
    | break_stmt
    | continue_stmt
    | return_stmt
    ;

// body declare
body_declare: BODY COLON stmt* ENDBODY DOT;

// function declare
func_declare: FUNCTION COLON ID parameter_func? body_declare;

// parameter declare
parameter_func: PARAMETER COLON scalar_var (COMMA scalar_var)*;

// if-elseif-else statement
if_stmt: IF exp THEN stmt* elseif_stmt* else_stmt? ENDIF DOT;
elseif_stmt: ELSEIF exp THEN stmt*;
else_stmt: ELSE stmt*;

// for statement
for_stmt: FOR LP scalar_var EQ exp COMMA conditionExpr COMMA updateExpr RP DO stmt* ENDFOR DOT;

//scalar-variable
scalar_var: ID index_var*;
index_var: LSB (scalar_var | exp)+ RSB;

//condition expression
conditionExpr: exp;

//update expression
updateExpr: exp;

// while statement
while_stmt: WHILE exp DO stmt* ENDWHILE DOT;

// Do-while statement
doWhile_stmt: DO stmt* WHILE exp ENDDO DOT;

//Break statement
break_stmt: BREAK SEMI;

//Continue statement
continue_stmt: CONTINUE SEMI;

//Return statement
return_stmt: RETURN (scalar_var | all_lit | exp)? SEMI;

//Call statment
func_call: ID LP (exp (COMMA exp)*)? RP;
call_stmt: func_call SEMI;

//expression
exp: exp1 RELATIONAL exp1 | exp1 ;
exp1: exp1 ( AND | OR ) exp2 | exp2;
exp2: exp2 (ADD | SUB | ADDDOT | SUBDOT) exp3 | exp3;
exp3: exp3 ( MUL | DIV | MOD) exp4 | exp4;
exp4: (NOT) exp4 | exp5;
exp5: (SUB) exp5 | exp6;
exp6: exp6 op_index | operands;
op_index: LSB exp RSB;
operands: LP exp RP
        | func_call
        | all_lit
        | ID
        ;

//operand: all_literal | func_call_exp | var_id | LP expression RP ;
all_lit: INTLIT | FLOATLIT | STRINGLIT | BOOLEANLIT;

RELATIONAL: RELATIONAL_FLOAT | RELATIONAL_INT;
RELATIONAL_INT:  EQINT | NEQINT | GTINT | LTINT | GTEINT | LTEINT ;
RELATIONAL_FLOAT: EQINT | NEQF | GTF | LTF | GTEF | LTEF ;

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
FUNCTION: 'Function';// 'F' U N C T I O N;
PARAMETER: 'Parameter';//'P' A R A M E T E R;
//Scope
BODY: 'Body';//'B' O D Y;
ENDBODY: 'EndBody';//'E' N D B O D Y;
//Flow Statement
IF: 'If';//'I' F;
THEN: 'Then';//'T' H E N;
ELSEIF: 'ElseIf';//'E' L S E I F;
ELSE: 'Else';//'E' L S E;
ENDIF: 'EndIf';//'E' N D I F;
//Loop Statement
FOR: 'For';//'F' O R;
ENDFOR: 'EndFor';//'E' N D F O R;
DO: 'Do';//'D' O;
ENDDO: 'EndDo';//'E' N D D O;
WHILE: 'While';//'W' H I L E;
ENDWHILE: 'EndWhile';//'E' N D W H I L E;
//Stop Statement
RETURN: 'Return';//'R' E T U R N;
BREAK: 'Break';//'B' R E A K;
CONTINUE: 'Continue';//'C' O N T I N U E;
//Value
TRUE: 'True';//'T' R U E;
FALSE: 'False';//'F' A L S E;
//Others
VAR: 'Var';//'V' A R;

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
GTEF: GTINT EQ DOT;

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
INTLIT: DEC | HEX | OCT;

// FLoat
FLOATLIT: DEC DOT (EXPONENT | DIGIT+ EXPONENT?)?
        | DEC EXPONENT
        ;

// Bool
BOOLEANLIT: TRUE | FALSE;

// 3.3.1 Identifiers
ID: [a-z][_a-zA-Z0-9]* ;


ILLEGAL_ESCAPE: '"' STR_CHAR* ESC_ILLEGAL
	{
		value = str(self.text)
		raise IllegalEscape(value[1:])
	}
	;
UNCLOSE_STRING: '"' STR_CHAR* ([\n\f\r\b\t\\] | '\'"' | EOF)
	{
		value = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\'"', '\\']
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

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	}
	;

fragment STR_CHAR: ~[\b\f\r\n\t'"\\] | ESC_SEQ ;
fragment ESC_SEQ: '\\' [bfrnt'\\] | '\'"' ;
fragment ESC_ILLEGAL: '\\' ~[bfrnt'\\] | '\'' | '\'' ~["];
fragment UNT_CMT: ~[*] ;

//fragment A: [aA];
//fragment B: [bB];
//fragment C: [cC];
//fragment D: [dD];
//fragment E: [eE];
//fragment F: [fF];
//fragment G: [gG];
//fragment H: [hH];
//fragment I: [iI];
//fragment J: [jJ];
//fragment K: [kK];
//fragment L: [lL];
//fragment M: [mM];
//fragment N: [nN];
//fragment O: [oO];
//fragment P: [pP];
//fragment Q: [qQ];
//fragment R: [rR];
//fragment S: [sS];
//fragment T: [tT];
//fragment U: [uU];
//fragment V: [vV];
//fragment W: [wW];
//fragment X: [xX];
//fragment Y: [yY];
//fragment Z: [zZ];
