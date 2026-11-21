"""
Modulo: vista.py
Descripcion: Capa de Interfaz de Usuario por Consola (Patron MVC).
Maneja la presentacion de menus, captura de entradas con validacion,
y formateo de resultados y errores (sin emojis para maxima compatibilidad).
"""

import os
from typing import List, Optional, Any, Dict


class CalculadoraVista:
    """Clase encargada de la interfaz y presentacion en consola."""

    ANCHO_LINEA = 64

    # =========================================================================
    # UTILIDADES DE PANTALLA Y FORMATEO
    # =========================================================================

    @staticmethod
    def limpiar_pantalla() -> None:
        """Limpia la terminal segun el sistema operativo."""
        os.system("cls" if os.name == "nt" else "clear")

    @classmethod
    def imprimir_encabezado(cls, titulo: str, subtitulo: Optional[str] = None) -> None:
        """Imprime un encabezado estilizado con caracteres estandar."""
        print("=" * cls.ANCHO_LINEA)
        print(titulo.center(cls.ANCHO_LINEA))
        if subtitulo:
            print(subtitulo.center(cls.ANCHO_LINEA))
        print("=" * cls.ANCHO_LINEA)

    @staticmethod
    def pausar() -> None:
        """Pausa la ejecucion hasta que el usuario presione Enter."""
        input("\nPresione [ENTER] para continuar...")

    # =========================================================================
    # MENUS PRINCIPALES Y CATEGORIAS
    # =========================================================================

    @classmethod
    def mostrar_menu_principal(cls) -> None:
        """Muestra el menu principal de categorias."""
        cls.imprimir_encabezado("CALCULADORA CIENTIFICA EN PYTHON", "Seleccione una categoria")
        print("  [1] Aritmetica y Estadistica Basica")
        print("  [2] Algebra y Analisis Funcional")
        print("  [3] Teoria de Numeros y Secuencias")
        print("  [4] Trigonometria")
        print("  [0] Salir del Programa")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_menu_aritmetica(cls) -> None:
        """Muestra el submenu de Aritmetica y Estadistica."""
        cls.imprimir_encabezado("CATEGORIA: ARITMETICA Y ESTADISTICA")
        print("  [1] Suma (dos numeros o serie de numeros)")
        print("  [2] Resta")
        print("  [3] Multiplicacion (dos numeros o serie de numeros)")
        print("  [4] Division")
        print("  [5] Media Aritmetica (Promedio de una lista)")
        print("  [0] Volver al Menu Principal")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_menu_algebra(cls) -> None:
        """Muestra el submenu de Algebra y Funciones."""
        cls.imprimir_encabezado("CATEGORIA: ALGEBRA Y ANALISIS")
        print("  [1] Potencia (base ^ exponente)")
        print("  [2] Raiz (cuadrada o enesima)")
        print("  [3] Logaritmos (natural, decimal o base personalizada)")
        print("  [4] Ecuacion Cuadratica (ax^2 + bx + c = 0)")
        print("  [0] Volver al Menu Principal")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_menu_teoria_numeros(cls) -> None:
        """Muestra el submenu de Teoria de Numeros y Secuencias."""
        cls.imprimir_encabezado("CATEGORIA: TEORIA DE NUMEROS Y SECUENCIAS")
        print("  [1] Factorial (n!)")
        print("  [2] Verificador de Numeros Primos")
        print("  [3] Minimo Comun Multiplo (MCM)")
        print("  [4] Maximo Comun Divisor (MCD)")
        print("  [5] Serie / Secuencia de Fibonacci")
        print("  [0] Volver al Menu Principal")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_menu_trigonometria(cls) -> None:
        """Muestra el submenu de Trigonometria."""
        cls.imprimir_encabezado("CATEGORIA: TRIGONOMETRIA")
        print("  [1] Seno (sin)")
        print("  [2] Coseno (cos)")
        print("  [3] Tangente (tan)")
        print("  [0] Volver al Menu Principal")
        print("-" * cls.ANCHO_LINEA)

    # =========================================================================
    # CAPTURA Y VALIDACION DE ENTRADAS DEL USUARIO
    # =========================================================================

    @staticmethod
    def pedir_opcion(opciones_validas: List[str], mensaje: str = "Seleccione una opcion: ") -> str:
        """Solicita y valida una opcion dentro de una lista permitida."""
        while True:
            entrada = input(f"> {mensaje}").strip()
            if entrada in opciones_validas:
                return entrada
            print(f"[!] Opcion invalida. Opciones validas: {', '.join(opciones_validas)}")

    @staticmethod
    def pedir_flotante(mensaje: str) -> float:
        """Solicita un numero de punto flotante validando que no haya errores de formato."""
        while True:
            entrada = input(f"> {mensaje}").strip().replace(",", ".")
            try:
                return float(entrada)
            except ValueError:
                print("[!] Error: Ingrese un valor numerico valido (ej: 5, -3.2, 0.75).")

    @staticmethod
    def pedir_entero(mensaje: str, minimo: Optional[int] = None, maximo: Optional[int] = None) -> int:
        """Solicita un numero entero, validando limites opcionales."""
        while True:
            entrada = input(f"> {mensaje}").strip()
            try:
                valor = int(entrada)
                if minimo is not None and valor < minimo:
                    print(f"[!] El valor debe ser mayor o igual a {minimo}.")
                    continue
                if maximo is not None and valor > maximo:
                    print(f"[!] El valor debe ser menor o igual a {maximo}.")
                    continue
                return valor
            except ValueError:
                print("[!] Error: Debe ingresar un numero entero valido (sin decimales).")

    @staticmethod
    def pedir_lista_flotantes(mensaje: str, min_elementos: int = 1) -> List[float]:
        """
        Solicita una lista de numeros separados por espacios o comas.
        Ejemplo: '4.5, 6, 8.2, 10' o '4.5 6 8.2 10'.
        """
        while True:
            entrada = input(f"> {mensaje}\n  (Separados por espacio o coma): ").strip()
            if not entrada:
                print("[!] No ingreso ningun dato.")
                continue

            partes = entrada.replace(",", " ").split()
            try:
                numeros = [float(p) for p in partes]
                if len(numeros) < min_elementos:
                    print(f"[!] Debe ingresar al menos {min_elementos} numero(s).")
                    continue
                return numeros
            except ValueError:
                print("[!] Error: Uno o mas valores no son numeros validos. Intente nuevamente.")

    @staticmethod
    def pedir_lista_enteros(mensaje: str, min_elementos: int = 2) -> List[int]:
        """Solicita una lista de numeros enteros separados por espacios o comas."""
        while True:
            entrada = input(f"> {mensaje}\n  (Separados por espacio o coma): ").strip()
            if not entrada:
                print("[!] No ingreso ningun dato.")
                continue

            partes = entrada.replace(",", " ").split()
            try:
                numeros = [int(p) for p in partes]
                if len(numeros) < min_elementos:
                    print(f"[!] Debe ingresar al menos {min_elementos} numero(s) entero(s).")
                    continue
                return numeros
            except ValueError:
                print("[!] Error: Todos los valores deben ser numeros enteros. Intente nuevamente.")

    @classmethod
    def pedir_unidad_angular(cls) -> bool:
        """
        Pregunta al usuario la unidad del angulo para funciones trigonometricas.
        Retorna True si es grados sexagesimales (deg), False si es radianes (rad).
        """
        print("\nEn que unidad desea ingresar el angulo?")
        print("  [1] Grados sexagesimales (deg)")
        print("  [2] Radianes (rad)")
        opcion = cls.pedir_opcion(["1", "2"], "Seleccione la unidad [1/2]: ")
        return opcion == "1"

    # =========================================================================
    # VISUALIZACION DE RESULTADOS Y ERRORES
    # =========================================================================

    @classmethod
    def mostrar_resultado(cls, operacion: str, valor: Any, detalle: Optional[str] = None) -> None:
        """Muestra el resultado formateado de manera clara."""
        print("\n" + "-" * cls.ANCHO_LINEA)
        print(f"[RESULTADO] {operacion.upper()}")
        print("-" * cls.ANCHO_LINEA)

        if isinstance(valor, float):
            if valor.is_integer():
                str_valor = f"{int(valor)}"
            else:
                str_valor = f"{valor:.6f}".rstrip("0").rstrip(".")
        elif isinstance(valor, complex):
            real = valor.real
            imag = valor.imag
            signo = "+" if imag >= 0 else "-"
            str_valor = f"{real:.4f} {signo} {abs(imag):.4f}i"
        elif isinstance(valor, list):
            str_valor = ", ".join(str(item) for item in valor)
        else:
            str_valor = str(valor)

        print(f"  Valor: {str_valor}")

        if detalle:
            print(f"  Detalle: {detalle}")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_resultado_cuadratica(cls, datos: Dict[str, Any], a: float, b: float, c: float) -> None:
        """Muestra el resultado completo de una ecuacion cuadratica."""
        print("\n" + "-" * cls.ANCHO_LINEA)
        print(f"[RESOLUCION] {a}x^2 + ({b})x + ({c}) = 0")
        print("-" * cls.ANCHO_LINEA)
        print(f"  Info: {datos['descripcion']}")

        tipo = datos["tipo"]
        soluciones = datos["soluciones"]

        if tipo == "dos_reales":
            print(f"  x1 = {soluciones[0]:.6f}".rstrip("0").rstrip("."))
            print(f"  x2 = {soluciones[1]:.6f}".rstrip("0").rstrip("."))
        elif tipo == "raiz_doble":
            print(f"  x = {soluciones[0]:.6f}".rstrip("0").rstrip("."))
        elif tipo == "complejas":
            x1, x2 = soluciones
            print(f"  x1 = {x1.real:.4f} + {x1.imag:.4f}i")
            print(f"  x2 = {x2.real:.4f} - {abs(x2.imag):.4f}i")
        elif tipo == "lineal":
            print(f"  x = {soluciones[0]:.6f}".rstrip("0").rstrip("."))

        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_serie_fibonacci(cls, n: int, serie: List[int]) -> None:
        """Muestra la serie de Fibonacci con formato legible."""
        print("\n" + "-" * cls.ANCHO_LINEA)
        print(f"[SERIE DE FIBONACCI] Primeros {n} terminos:")
        print("-" * cls.ANCHO_LINEA)

        linea = "  "
        for i, val in enumerate(serie, start=1):
            fragmento = f"[{i}]: {val}   "
            if len(linea) + len(fragmento) > cls.ANCHO_LINEA:
                print(linea)
                linea = "  " + fragmento
            else:
                linea += fragmento
        if linea.strip():
            print(linea)

        print("-" * cls.ANCHO_LINEA)
        print(f"  Lista completa: {serie}")
        print("-" * cls.ANCHO_LINEA)

    @classmethod
    def mostrar_error(cls, mensaje: str) -> None:
        """Muestra un mensaje de error destacado."""
        print("\n" + "!" * cls.ANCHO_LINEA)
        print(f"[ERROR] {mensaje}")
        print("!" * cls.ANCHO_LINEA)

    @classmethod
    def despedida(cls) -> None:
        """Muestra el mensaje de salida del sistema."""
        cls.imprimir_encabezado("GRACIAS POR USAR LA CALCULADORA", "Desarrollada en Python 3.11+")
        print("\nHasta pronto.\n")


# Permite ejecutar vista.py directamente mostrando el menu mediante el Controlador (MVC)
if __name__ == "__main__":
    from controlador import CalculadoraControlador
    app = CalculadoraControlador()
    app.iniciar()
