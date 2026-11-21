"""
Módulo: controlador.py
Descripción: Capa del Controlador (Patrón MVC).
Coordina las interacciones entre el Modelo (lógica matemática) y la Vista (interfaz por consola).
"""

from typing import List
from modelo import CalculadoraModelo
from vista import CalculadoraVista


class CalculadoraControlador:
    """Controlador principal de la aplicación."""

    def __init__(self) -> None:
        self.modelo = CalculadoraModelo
        self.vista = CalculadoraVista

    def iniciar(self) -> None:
        """Bucle principal del programa."""
        while True:
            self.vista.limpiar_pantalla()
            self.vista.mostrar_menu_principal()
            opcion = self.vista.pedir_opcion(["1", "2", "3", "4", "0"])

            if opcion == "1":
                self.gestionar_categoria_aritmetica()
            elif opcion == "2":
                self.gestionar_categoria_algebra()
            elif opcion == "3":
                self.gestionar_categoria_teoria_numeros()
            elif opcion == "4":
                self.gestionar_categoria_trigonometria()
            elif opcion == "0":
                self.vista.limpiar_pantalla()
                self.vista.despedida()
                break

    # =========================================================================
    # GESTIÓN DE CATEGORÍAS (SUBMENÚS)
    # =========================================================================

    def gestionar_categoria_aritmetica(self) -> None:
        """Controlador de la categoría de Aritmética y Estadística."""
        while True:
            self.vista.limpiar_pantalla()
            self.vista.mostrar_menu_aritmetica()
            opcion = self.vista.pedir_opcion(["1", "2", "3", "4", "5", "0"])

            if opcion == "0":
                break

            try:
                if opcion == "1":
                    self._operacion_suma()
                elif opcion == "2":
                    self._operacion_resta()
                elif opcion == "3":
                    self._operacion_multiplicacion()
                elif opcion == "4":
                    self._operacion_division()
                elif opcion == "5":
                    self._operacion_media()
            except Exception as e:
                self.vista.mostrar_error(str(e))

            self.vista.pausar()

    def gestionar_categoria_algebra(self) -> None:
        """Controlador de la categoría de Álgebra y Análisis."""
        while True:
            self.vista.limpiar_pantalla()
            self.vista.mostrar_menu_algebra()
            opcion = self.vista.pedir_opcion(["1", "2", "3", "4", "0"])

            if opcion == "0":
                break

            try:
                if opcion == "1":
                    self._operacion_potencia()
                elif opcion == "2":
                    self._operacion_raiz()
                elif opcion == "3":
                    self._operacion_logaritmo()
                elif opcion == "4":
                    self._operacion_cuadratica()
            except Exception as e:
                self.vista.mostrar_error(str(e))

            self.vista.pausar()

    def gestionar_categoria_teoria_numeros(self) -> None:
        """Controlador de la categoría de Teoría de Números y Secuencias."""
        while True:
            self.vista.limpiar_pantalla()
            self.vista.mostrar_menu_teoria_numeros()
            opcion = self.vista.pedir_opcion(["1", "2", "3", "4", "5", "0"])

            if opcion == "0":
                break

            try:
                if opcion == "1":
                    self._operacion_factorial()
                elif opcion == "2":
                    self._operacion_primo()
                elif opcion == "3":
                    self._operacion_mcm()
                elif opcion == "4":
                    self._operacion_mcd()
                elif opcion == "5":
                    self._operacion_fibonacci()
            except Exception as e:
                self.vista.mostrar_error(str(e))

            self.vista.pausar()

    def gestionar_categoria_trigonometria(self) -> None:
        """Controlador de la categoría de Trigonometría."""
        while True:
            self.vista.limpiar_pantalla()
            self.vista.mostrar_menu_trigonometria()
            opcion = self.vista.pedir_opcion(["1", "2", "3", "0"])

            if opcion == "0":
                break

            try:
                en_grados = self.vista.pedir_unidad_angular()
                unidad_txt = "grados (°)" if en_grados else "radianes (rad)"
                angulo = self.vista.pedir_flotante(f"Ingrese el valor del ángulo en {unidad_txt}: ")

                if opcion == "1":
                    res = self.modelo.seno(angulo, en_grados)
                    self.vista.mostrar_resultado(f"Seno de {angulo} {unidad_txt}", res)
                elif opcion == "2":
                    res = self.modelo.coseno(angulo, en_grados)
                    self.vista.mostrar_resultado(f"Coseno de {angulo} {unidad_txt}", res)
                elif opcion == "3":
                    res = self.modelo.tangente(angulo, en_grados)
                    self.vista.mostrar_resultado(f"Tangente de {angulo} {unidad_txt}", res)
            except Exception as e:
                self.vista.mostrar_error(str(e))

            self.vista.pausar()

    # =========================================================================
    # IMPLEMENTACIÓN DE ACCIONES ESPECÍFICAS
    # =========================================================================

    # --- ARITMÉTICA ---
    def _operacion_suma(self) -> None:
        print("\n¿Desea sumar 2 números o una serie de números?")
        print("  [1] Sumar 2 números")
        print("  [2] Sumar múltiples números")
        modo = self.vista.pedir_opcion(["1", "2"], "Seleccione modo [1/2]: ")

        if modo == "1":
            a = self.vista.pedir_flotante("Primer sumando (a): ")
            b = self.vista.pedir_flotante("Segundo sumando (b): ")
            res = self.modelo.suma(a, b)
            self.vista.mostrar_resultado(f"{a} + {b}", res)
        else:
            numeros = self.vista.pedir_lista_flotantes("Ingrese los números a sumar", min_elementos=2)
            res = self.modelo.suma_multiple(numeros)
            expresion = " + ".join(str(n) for n in numeros)
            self.vista.mostrar_resultado(f"Suma de serie: {expresion}", res)

    def _operacion_resta(self) -> None:
        a = self.vista.pedir_flotante("Minuendo (a): ")
        b = self.vista.pedir_flotante("Sustraendo (b): ")
        res = self.modelo.resta(a, b)
        self.vista.mostrar_resultado(f"{a} - {b}", res)

    def _operacion_multiplicacion(self) -> None:
        print("\n¿Desea multiplicar 2 números o una serie de números?")
        print("  [1] Multiplicar 2 números")
        print("  [2] Multiplicar múltiples números")
        modo = self.vista.pedir_opcion(["1", "2"], "Seleccione modo [1/2]: ")

        if modo == "1":
            a = self.vista.pedir_flotante("Primer factor (a): ")
            b = self.vista.pedir_flotante("Segundo factor (b): ")
            res = self.modelo.multiplicacion(a, b)
            self.vista.mostrar_resultado(f"{a} × {b}", res)
        else:
            numeros = self.vista.pedir_lista_flotantes("Ingrese los números a multiplicar", min_elementos=2)
            res = self.modelo.multiplicacion_multiple(numeros)
            expresion = " × ".join(str(n) for n in numeros)
            self.vista.mostrar_resultado(f"Multiplicación de serie: {expresion}", res)

    def _operacion_division(self) -> None:
        a = self.vista.pedir_flotante("Dividendo (a): ")
        b = self.vista.pedir_flotante("Divisor (b): ")
        res = self.modelo.division(a, b)
        self.vista.mostrar_resultado(f"{a} ÷ {b}", res)

    def _operacion_media(self) -> None:
        numeros = self.vista.pedir_lista_flotantes("Ingrese los valores para calcular la media aritmética", min_elementos=1)
        res = self.modelo.media_aritmetica(numeros)
        detalle = f"Total de datos ingresados: {len(numeros)} | Suma acumulada: {sum(numeros)}"
        self.vista.mostrar_resultado("Media Aritmética (Promedio)", res, detalle=detalle)

    # --- ÁLGEBRA ---
    def _operacion_potencia(self) -> None:
        base = self.vista.pedir_flotante("Base: ")
        exponente = self.vista.pedir_flotante("Exponente: ")
        res = self.modelo.potencia(base, exponente)
        self.vista.mostrar_resultado(f"{base} ^ ({exponente})", res)

    def _operacion_raiz(self) -> None:
        radicando = self.vista.pedir_flotante("Radicando (número dentro de la raíz): ")
        print("\nTipo de raíz:")
        print("  [1] Raíz cuadrada (índice 2)")
        print("  [2] Raíz enésima personalizada")
        opc = self.vista.pedir_opcion(["1", "2"], "Seleccione opción [1/2]: ")

        if opc == "1":
            indice = 2.0
        else:
            indice = self.vista.pedir_flotante("Índice de la raíz: ")

        res = self.modelo.raiz(radicando, indice)
        etiqueta = f"√({radicando})" if indice == 2 else f"Raíz {indice}-ésima de {radicando}"
        self.vista.mostrar_resultado(etiqueta, res)

    def _operacion_logaritmo(self) -> None:
        print("\nSeleccione el tipo de logaritmo:")
        print("  [1] Logaritmo Natural (ln, base e)")
        print("  [2] Logaritmo Decimal (log₁₀, base 10)")
        print("  [3] Logaritmo en base personalizada (log_b)")
        opc = self.vista.pedir_opcion(["1", "2", "3"], "Seleccione opción [1/2/3]: ")

        numero = self.vista.pedir_flotante("Ingrese el argumento del logaritmo (x > 0): ")

        if opc == "1":
            res = self.modelo.logaritmo(numero, base=None)
            self.vista.mostrar_resultado(f"ln({numero})", res)
        elif opc == "2":
            res = self.modelo.logaritmo(numero, base=10)
            self.vista.mostrar_resultado(f"log₁₀({numero})", res)
        else:
            base = self.vista.pedir_flotante("Ingrese la base (b > 0 y b ≠ 1): ")
            res = self.modelo.logaritmo(numero, base=base)
            self.vista.mostrar_resultado(f"log_{base}({numero})", res)

    def _operacion_cuadratica(self) -> None:
        print("\nForma general: ax² + bx + c = 0")
        a = self.vista.pedir_flotante("Coeficiente cuadrático (a): ")
        b = self.vista.pedir_flotante("Coeficiente lineal (b): ")
        c = self.vista.pedir_flotante("Término independiente (c): ")

        datos = self.modelo.resolver_cuadratica(a, b, c)
        self.vista.mostrar_resultado_cuadratica(datos, a, b, c)

    # --- TEORÍA DE NÚMEROS ---
    def _operacion_factorial(self) -> None:
        n = self.vista.pedir_entero("Ingrese un número entero no negativo (n ≥ 0): ", minimo=0)
        res = self.modelo.factorial(n)
        self.vista.mostrar_resultado(f"Factorial de {n} ({n}!)", res)

    def _operacion_primo(self) -> None:
        n = self.vista.pedir_entero("Ingrese un número entero para verificar si es primo: ")
        es_primo, explicacion = self.modelo.es_primo(n)
        estado = "SÍ ES PRIMO" if es_primo else "NO ES PRIMO"
        self.vista.mostrar_resultado(f"Verificación de primalidad para {n}", estado, detalle=explicacion)

    def _operacion_mcm(self) -> None:
        print("\n¿Desea calcular el MCM de 2 números o de una serie?")
        print("  [1] 2 números")
        print("  [2] Lista de 3 o más números")
        modo = self.vista.pedir_opcion(["1", "2"], "Seleccione modo [1/2]: ")

        if modo == "1":
            a = self.vista.pedir_entero("Primer número entero: ")
            b = self.vista.pedir_entero("Segundo número entero: ")
            res = self.modelo.mcm(a, b)
            self.vista.mostrar_resultado(f"MCM({a}, {b})", res)
        else:
            numeros = self.vista.pedir_lista_enteros("Ingrese los números enteros", min_elementos=2)
            res = self.modelo.mcm_multiple(numeros)
            self.vista.mostrar_resultado(f"MCM({', '.join(str(x) for x in numeros)})", res)

    def _operacion_mcd(self) -> None:
        print("\n¿Desea calcular el MCD de 2 números o de una serie?")
        print("  [1] 2 números")
        print("  [2] Lista de 3 o más números")
        modo = self.vista.pedir_opcion(["1", "2"], "Seleccione modo [1/2]: ")

        if modo == "1":
            a = self.vista.pedir_entero("Primer número entero: ")
            b = self.vista.pedir_entero("Segundo número entero: ")
            res = self.modelo.mcd(a, b)
            self.vista.mostrar_resultado(f"MCD({a}, {b})", res)
        else:
            numeros = self.vista.pedir_lista_enteros("Ingrese los números enteros", min_elementos=2)
            res = self.modelo.mcd_multiple(numeros)
            self.vista.mostrar_resultado(f"MCD({', '.join(str(x) for x in numeros)})", res)

    def _operacion_fibonacci(self) -> None:
        n = self.vista.pedir_entero(
            "Ingrese la cantidad de términos que desea generar de la serie (ej: 10): ",
            minimo=1
        )
        serie = self.modelo.fibonacci(n)
        self.vista.mostrar_serie_fibonacci(n, serie)
