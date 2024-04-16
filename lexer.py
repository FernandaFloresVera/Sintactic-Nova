import ply.lex as lex

tokens = [
    'PUNTO_Y_C', 'DOS_P',
    'INT', 'STRING', 
    'LLAVE_I', 'LLAVE_D', 'PARENTESIS_I', 'PARENTESIS_D', 'PM', 'IDENTIFICADOR', 
    'OPERADOR', 'IGUAL',
    'SCREEN', 'RN', 'FN', 'WHEN', 'SO', 'CYCLE', 'VARIABLE', 'TYPE',
]

t_PUNTO_Y_C = r';'
t_DOS_P = r'\:'
t_LLAVE_I = r'\{'
t_LLAVE_D = r'\}'
t_PARENTESIS_I = r'\('
t_PARENTESIS_D = r'\)'
t_IGUAL = r'='
t_OPERADOR = r'\>=|>'
t_SCREEN = r'\bscreen\b'
t_RN = r'\brun\b'
t_FN = r'\bfn\b'
t_WHEN = r'\bwhen\b'
t_SO = r'\bso\b'
t_CYCLE = r'\bcycle\b'
t_TYPE = r'\b(int|string)\b'
t_PM = r'\+\+|--'

def t_VARIABLE(t): 
    r'_[a-zA-Z_][a-zA-Z0-9]*'
    return t

def t_STRING(t):
    r'"([^;()\[\]{}]|\\")*"'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = { 
        'int': 'TYPE',  'string': 'TYPE', 
        'screen': 'SCREEN', 'run': 'RN', 'fn': 'FN', 'when': 'WHEN', 'so': 'SO',
        'cycle': 'CYCLE'
    }
    t.type = keywords.get(t.value, 'IDENTIFICADOR')
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()