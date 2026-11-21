# Calculadora Cientifica en Python (Arquitectura MVC)

Una calculadora de consola potente, robusta y modular desarrollada en Python. Disenada siguiendo las mejores practicas de ingenieria de software bajo el patron arquitectonico **Modelo - Vista - Controlador (MVC)**, con tipado estatico (`typing`), validacion exhaustiva de entradas y cobertura con pruebas unitarias (`unittest`).

---

## Caracteristicas y Operaciones Incluidas

La calculadora clasifica sus operaciones en 4 categorias tematicas para una experiencia de usuario clara e intuitiva:

### 1. Aritmetica y Estadistica Basica
- **Suma:** Suma directa de dos numeros o calculo acumulado de una serie de numeros.
- **Resta:** Diferencia precisa entre dos numeros (a - b).
- **Multiplicacion:** Producto de dos numeros o de una serie completa.
- **Division:** Cociente con validacion preventiva contra division por cero.
- **Media Aritmetica:** Promedio exacto a partir de una lista de datos numericos ingresados.

### 2. Algebra y Analisis Funcional
- **Potencia:** Exponenciacion base^exponente con soporte para exponentes decimales y negativos.
- **Raiz:** Calculo de raiz cuadrada y raiz enesima personalizada, con soporte para raices impares reales de radicandos negativos y raices pares en el plano complejo.
- **Logaritmos:**
  - Logaritmo Natural (ln, base e).
  - Logaritmo Decimal (log10, base 10).
  - Logaritmo en base personalizada (log_b, con validacion de x > 0, b > 0 y b != 1).
- **Ecuaciones Cuadraticas (ax^2 + bx + c = 0):**
  - Analisis de discriminante (Delta = b^2 - 4ac).
  - Dos soluciones reales distintas (Delta > 0).
  - Raiz doble (Delta = 0).
  - Soluciones complejas conjugadas con notacion estandar a +- bi (Delta < 0).
  - Manejo de casos lineales (a = 0).

### 3. Teoria de Numeros y Secuencias
- **Factorial (n!):** Para cualquier entero no negativo.
- **Verificador de Numeros Primos:** Algoritmo optimizado O(sqrt(n)) con explicacion detallada y deteccion de divisores.
- **Minimo Comun Multiplo (MCM):** Para 2 numeros o series de 3 o mas enteros.
- **Maximo Comun Divisor (MCD):** Algoritmo de Euclides para 2 o multiples enteros.
- **Serie / Secuencia de Fibonacci:** Genera exactamente la cantidad n de terminos especificada (ej: para n = 10, genera [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]).

### 4. Trigonometria
- **Seno (sin), Coseno (cos) y Tangente (tan):**
  - Soporte seleccionable para **Grados Sexagesimales (deg)** o **Radianes (rad)**.
  - Correccion de precision de punto flotante para valores trigonometricos limite (como sin(180) = 0 y cos(90) = 0).
  - Deteccion de indeterminaciones y asintotas en la tangente (ej: 90 deg, 270 deg).

---

## Estructura del Proyecto (Arquitectura MVC)

El proyecto separa responsabilidades de acuerdo al patron de diseno **MVC**:

```text
Calculadora_py/
|
|-- modelo.py             # Logica matematica pura, algoritmos y reglas de negocio.
|-- vista.py              # Interfaz de usuario por consola, captura de datos y renderizado.
|-- controlador.py        # Orquestador del flujo del programa y manejo de eventos.
|-- main.py               # Punto de entrada de la aplicacion.
|-- test_calculadora.py   # Suite de pruebas unitarias automatizadas (unittest).
`-- README.md             # Documentacion tecnica del proyecto.
```

- **`modelo.py`**: No contiene `print()` ni `input()`. Es 100% reutilizable en interfaces graficas o APIs.
- **`vista.py`**: Aisla la interaccion con el usuario en terminal, validando formatos numericos y tipos de datos. Puede ejecutarse directamente para mostrar los menus.
- **`controlador.py`**: Captura las decisiones del usuario, solicita calculos al modelo y entrega los resultados formateados a la vista.

---

## Como Ejecutar la Aplicacion

Puedes iniciar la aplicacion tanto desde `main.py` como directamente desde `vista.py`:

```bash
python main.py
```
o bien:
```bash
python vista.py
```

---

## Pruebas Unitarias

Para verificar la integridad matematica de cada algoritmo, ejecuta la suite de pruebas:

```bash
python -m unittest test_calculadora.py
```

---

## Ejemplo de Uso en Consola

```text
================================================================
                CALCULADORA CIENTIFICA EN PYTHON                
                    Seleccione una categoria                    
================================================================
  [1] Aritmetica y Estadistica Basica
  [2] Algebra y Analisis Funcional
  [3] Teoria de Numeros y Secuencias
  [4] Trigonometria
  [0] Salir del Programa
----------------------------------------------------------------
> Seleccione una opcion: 3

================================================================
             CATEGORIA: TEORIA DE NUMEROS Y SECUENCIAS          
================================================================
  [1] Factorial (n!)
  [2] Verificador de Numeros Primos
  [3] Minimo Comun Multiplo (MCM)
  [4] Maximo Comun Divisor (MCD)
  [5] Serie / Secuencia de Fibonacci
  [0] Volver al Menu Principal
----------------------------------------------------------------
> Seleccione una opcion: 5
> Ingrese la cantidad de terminos que desea generar de la serie (ej: 10): 10

----------------------------------------------------------------
[SERIE DE FIBONACCI] Primeros 10 terminos:
----------------------------------------------------------------
  [1]: 0   [2]: 1   [3]: 1   [4]: 2   [5]: 3   [6]: 5   [7]: 8   [8]: 13   [9]: 21   [10]: 34
----------------------------------------------------------------
  Lista completa: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
----------------------------------------------------------------
```
