for_out = []
variables = []
value_variable = []
out_pps = ""
func = []

def generate_code(parsers):
    global out_pps
    for parser in parsers:
        if parser['type'] == 'cycle_decl':
            if parser['init']['identifier'] not in variables:
                variables.append(parser['init']['identifier'])
                value_variable.append(parser['init']['value'])
            else:
                out_pps += f"YA DECLARADA\n"

            for i in range(parser['cond'][3]):
                value_variable[variables.index(parser['init']['identifier'])] += 1
                if parser['body'][0]['value'] in variables: #string| variable
                    for_out.append(value_variable[variables.index(parser['body'][0]['value'])])
                else:
                    for_out.append(parser['body'][0]['value']) #primer valor
            return for_out
        elif parser['type'] == 'print_stmt':
            if parser['value'] in variables: #string | identificador 
                out_pps += f"{value_variable[variables.index(parser['value'])]}\n"
            elif parser['value'][0] == '"':
                out_pps += f"{parser['value']}\n"
            else:
                out_pps += "VARIABLE NO DECLARADA"
        elif parser['type'] == 'var_decl':
            if parser['identifier'] not in variables:
                if parser['var_type'] == 'int':
                    if isinstance(parser['value'], int):
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"WARNING ERROR: Se esperaba un entero para la variable\n"

                elif parser['var_type'] == 'string':
                    if parser['value'].startswith('"') and parser['value'].endswith('"'):
                        variables.append(parser['identifier'])
                        value_variable.append(parser['value'])
                    else:
                        out_pps += f"WARNING ERROR: Se esperaba una cadena para la variable\n"

                else:
                    out_pps += f"Error de tipo: tipo de variable no reconocido\n"

            else:
                out_pps += f"YA DECLARADA\n"

        elif parser['type'] == 'when_decl':
            if parser['condicion'][1] in variables:
                validation = f"{value_variable[variables.index(parser['condicion'][1])]} {parser['condicion'][2]} {parser['condicion'][-1]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['so']['body'])
            elif parser['condicion'][-1] in variables:
                validation = f"{parser['condicion'][1]} {parser['condicion'][2]} {value_variable[variables.index(parser['condicion'][-1])]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['so']['body'])
            elif parser['condicion'][1] in variables and parser['condicion'][-1] in variables:
                validation = f"{value_variable[variables.index(parser['condicion'][1])]} {parser['condicion'][2]} {value_variable[variables.index(parser['condicion'][-1])]}"
                if eval(validation):
                    generate_code(parser['body'])
                else:
                    generate_code(parser['so']['body'])
        elif parser['type'] == 'func_decl':
            if parser['name'] not in func:
                func.append(parser['name'])
                generate_code(parser['body'])
            else:
                out_pps += f"YA DECLARADA\n"
    return out_pps