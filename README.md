#  Mi Lenguaje de Programación — Especificación Léxica

Este lenguaje es un lenguaje de programación diseñado para aprender los fundamentos de la programación estructurada. Usa una sintaxis sencilla con palabras reservadas claras como `HOLA` para abrir el programa y `ADÍOS` para cerrarlo. Permite trabajar con variables, condicionales, ciclos, funciones y estructuras comunes.

##  Estructura general del lenguaje

* El programa comienza con la palabra reservada `HOLA` y finaliza con `ADÍOS`.
* Las declaraciones y sentencias usan palabras clave simples (`si`, `sino`, `mientras`, `para`...).
* Los bloques de código se delimitan con llaves `{}` o mediante la estructura propia de cada sentencia.
* El punto y coma `;` no es obligatorio.
* Los comentarios se indican con `//`.

##  Reglas para nombres de variables

* Se usan palabras clave para declarar el tipo de variable (`entero`, `booleano`, `cadena`).
* Los nombres de variables pueden ser simples (ej. `x`, `y`, `nombre`).
* No se permiten caracteres especiales en los nombres de variables.

 Ejemplos válidos:

```plaintext
entero = x
booleano = esMayor
cadena = nombre
```

 Ejemplos inválidos:

```plaintext
_entero
x-nombre
@dato
```

##  Tipos de datos permitidos

| Tipo     | Ejemplo          |
| -------- | ---------------- |
| Entero   | 10, -3, 100      |
| Booleano | verdadero, falso |
| Cadena   | "Jean", "Hola"   |

##  Operadores

### Aritméticos

| Operador | Descripción    |
| -------- | -------------- |
| +        | Suma           |
| -        | Resta          |
| \*       | Multiplicación |
| /        | División       |

### Relacionales

| Operador | Descripción |
| -------- | ----------- |
| <        | Menor que   |
| >        | Mayor que   |
| ==       | Igual a     |

##  Condicionales y ciclos

### Condicionales

```plaintext
si (x < y) entonces {
    esMayor = falso;
} sino {
    esMayor = verdadero;
}
```

### Ciclo `mientras`

```plaintext
mientras (x < y) {
    x = x + 1;
}
```

### Ciclo `para`

```plaintext
para (entero i = 0; i < 5; i = i + 1) {
    escribir("i = ", i);
}
```

### Switch-Case

```plaintext
segun (x) hacer {
    caso 1:
        escribir("x es 1");
        romper;
    defecto:
        escribir("otro valor");
        romper;
}
```

##  Funciones definidas por el usuario

```plaintext
funcion entero doble(entero n) {
    retornar n * 2;
}
```

##  Comentarios

| Forma    | Tipo                |
| -------- | ------------------- |
| // texto | Comentario de línea |

##  Palabras reservadas

No se pueden usar como nombres de variables:

`HOLA`, `ADÍOS`, `si`, `sino`, `mientras`, `para`, `segun`, `caso`, `romper`, `funcion`, `retornar`, `escribir`, `leer`, `verdadero`, `falso`

## ⚠ Advertencias comunes

| Situación                             | Resultado           |
| ------------------------------------- | ------------------- |
| No usar `HOLA` al inicio              | Error               |
| No usar `ADÍOS` al final              | Error               |
| Variables sin declarar                | Error               |
| Bloques sin llaves claros             | Error de estructura |
| Uso incorrecto de palabras reservadas | Error               |

##  Errores comunes

| Error                  | Descripción                                                                   |
| ---------------------- | ----------------------------------------------------------------------------- |
| entero = \_x           | Nombres de variables no pueden iniciar con guion bajo o caracteres especiales |
| si x < y               | Falta de paréntesis en condiciones                                            |
| segun (x)              | Sin casos definidos                                                           |
| Falta `HOLA` o `ADÍOS` | Programa no válido                                                            |

