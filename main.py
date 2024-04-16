import interpreter
from yacc import parse
from lexer import lexer

def execute_parser(script):
    try:
        result = parse(script)
        if result is not None:
            print("Análisis sintáctico completado sin errores. Mostrando tokens:\n")
            lexer.input(script)
            tokens = [(tok.type, ":",tok.value) for tok in lexer]
            return tokens
        else:
            return "Error de sintaxis: No se pudo procesar la entrada correctamente."
    except Exception as e:
        print(f"Error al analizar la entrada: {e}")
        return []

def execute_python(script):
    parse_result = parse(script)
    output_obj = interpreter.generate_code(parse_result)
    return output_obj
