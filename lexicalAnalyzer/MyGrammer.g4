grammar MyGrammer;

expr   : left=expr op=(OPMUL | OPDIV) right=expr | left=expr op=(OPSOMA | OPSUB) right=expr | atom=number | AP expr FP ;

number : NUMBERINT | NUMBERREAL ;

OPMUL  : '*' ;

OPDIV  : '/' ;

OPSOMA : '+' ;

OPSUB  : '-' ;

AP     : '(' ;

FP     : ')' ;

NUMBERINT  : ('0'..'9')+ ;

NUMBERREAL : ('0'..'9')+ ('.' ('0'..'9')+)? ;

WS     : [ \r\n\t]+ -> skip ;