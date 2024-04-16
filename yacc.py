import ply.yacc as yacc
from lexer import lexer, tokens

def p_start(p):
    'start : structures'
    p[0] = p[1]

def p_structures(p):
    '''structures : structures structure
                  | structure'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_structure(p):
    '''structure : var_decl
                 | func_decl
                 | cycle_decl
                 | when_decl
                 | statement'''
    p[0] = p[1]

def p_declaracion_variable(p):
    'var_decl : VARIABLE DOS_P TYPE IGUAL value PUNTO_Y_C'
    p[0] = {'type': 'var_decl', 'var_type': p[3], 'identifier': p[1], 'value': p[5]}
    
    if p[2] == "int" and not isinstance(p[5], int):
        raise SyntaxError(f"Se esperaba un entero en la variable")
    elif p[2] == "string" and not (p[5].startswith('"') and p[5].endswith('"')):
        raise SyntaxError(f"Se esperaba una cadena en la variable")

def p_funcion_declaracion(p):
    'func_decl : RN IDENTIFICADOR PARENTESIS_I PARENTESIS_D LLAVE_I statements LLAVE_D'
    p[0] = {'type': 'func_decl', 'name': p[2], 'body': p[6]}
    print(f"run: {p[6]}")
    #func test() {imprimir("esto es una funcion");}

def p_cycle_funcion(p):
    'cycle_decl : FN IDENTIFICADOR PARENTESIS_I PARENTESIS_D LLAVE_I CYCLE PARENTESIS_I var_decl condicion PUNTO_Y_C incremento PARENTESIS_D LLAVE_I statements LLAVE_D LLAVE_D'
    p[0] = {'type': 'cycle_decl', 'init': p[8], 'cond': p[9], 'inc': p[11], 'body': p[14]}
#   fn saludo() { cycle (_i: int = 0; i > 10; i++) { screen("hola" + _nombre); }}

def p_when_funcion(p):
    'when_decl : FN IDENTIFICADOR PARENTESIS_I PARENTESIS_D LLAVE_I WHEN PARENTESIS_I condicion PARENTESIS_D LLAVE_I statements LLAVE_D so_decl LLAVE_D'
    p[0] = {'type': 'when_decl', 'condicion': p[8], 'body': p[11], 'so': p[13]}

    
def p_so_decl(p):
    'so_decl : SO LLAVE_I statements LLAVE_D'
    p[0] = {'type': 'so_decl', 'body': p[3]}
    

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_impresion(p):
    '''statement : SCREEN PARENTESIS_I STRING PARENTESIS_D PUNTO_Y_C
                 | SCREEN PARENTESIS_I IDENTIFICADOR PARENTESIS_D PUNTO_Y_C'''
    p[0] = {'type': 'print_stmt', 'value': p[3]}

def p_value(p):
    '''value : INT
             | STRING
    '''
    p[0] = p[1]

def p_condicion(p):
    '''condicion : IDENTIFICADOR OPERADOR value
                 | IDENTIFICADOR OPERADOR IDENTIFICADOR
                 | VARIABLE OPERADOR value
    '''
    p[0] = ('condicion', p[1], p[2], p[3])

def p_incremento(p):
    'incremento : IDENTIFICADOR PM'
    p[0] = ('incremento', p[1], p[2])

def p_error(p):
    if p:
        raise Exception(f"Error sintáctico {p.type} ('{p.value}') at position {p.lexpos}")
    else:
        raise Exception("Se esperaba más sintaxis")

parser = yacc.yacc()

def parse(data):
    lexer.input(data)
    result = parser.parse(lexer=lexer)
    return result