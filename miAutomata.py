import re

# Palabras reservadas del lenguaje basado en tu PDF
palabras_reservadas = {
    "HOLA", "ADÍOS", "entero", "booleano", "cadena", "si", "sino",
    "mientras", "para", "caso", "segun", "romper", "leer", "escribir",
    "funcion", "retornar", "verdadero", "falso", "entonces", "hacer", "defecto"
}

# Operadores
operadores = {
    "+", "-", "*", "/", "=", "==", "<", ">"
}

# Delimitadores y símbolos
simbolos = {
    "(", ")", "{", "}", ";", ",", "\""
}

# Patrones regex para tokens
regex_token = {
    "numero_entero": r"^-?\d+$",
    "cadena": r'^".*"$',
    "identificador": r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ][a-zA-Z0-9áéíóúÁÉÍÓÚñÑ]*$"
}

def clasificar_token(token):
    if token in palabras_reservadas:
        return "Palabra reservada"
    elif token in operadores:
        return "Operador"
    elif token in simbolos:
        return "Delimitador"
    elif re.match(regex_token["numero_entero"], token):
        return "Número entero"
    elif re.match(regex_token["cadena"], token):
        return "Cadena"
    elif re.match(regex_token["identificador"], token):
        return "Identificador"
    else:
        return "Error léxico"

def analizar_archivo():
    with open('ejemplo.txt', 'r', encoding='utf-8') as archivo:
        linea_n = 0
        total_tokens = 0
        errores = 0

        print(" ANALIZADOR LÉXICO - Lenguaje de Jean")
        print("=" * 50)

        for linea in archivo:
            linea_n += 1

            # Regex para extraer todos los tokens, ahora soporta tildes y ñ
            tokens = re.findall(
                r'//.*|".*?"|[a-zA-ZáéíóúÁÉÍÓÚñÑ][a-zA-Z0-9áéíóúÁÉÍÓÚñÑ]*|-?\d+|==|[+\-*/=<>;{},()]',
                linea)

            if tokens:
                print(f"\nLínea {linea_n}: {linea.strip()}")

                for token in tokens:
                    total_tokens += 1

                    # Detectar comentarios
                    if token.startswith('//'):
                        print(f"   {token:<20} ➜ Comentario")
                    else:
                        tipo = clasificar_token(token)
                        if tipo != "Error léxico":
                            print(f"   {token:<20} ➜ {tipo}")
                        else:
                            print(f"   {token:<20} ➜ Error léxico")
                            errores += 1

        # Resumen
        print("=" * 50)
        print(f" Total tokens analizados: {total_tokens}")
        print(f" Tokens válidos: {total_tokens - errores}")
        print(f" Errores léxicos: {errores}")

        if errores == 0:
            print(" ¡Análisis completado sin errores!")

# Ejecutar análisis
analizar_archivo()
