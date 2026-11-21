"""
Módulo: modelo.py
Descripción: Capa de lógica matemática y de negocio (Patrón MVC).
Contiene todas las operaciones matemáticas y algoritmos sin dependencias de entrada/salida.
"""

import math
import cmath
from typing import List, Tuple, Union, Optional, Dict, Any


class CalculadoraModelo:
    """Clase que encapsula todas las operaciones matemáticas de la calculadora."""

    # =========================================================================
    # 1. ARITMÉTICA Y ESTADÍSTICA
    # =========================================================================

    @staticmethod
    def suma(a: float, b: float) -> float:
        """Calcula la suma de dos números."""
        return a + b

    @staticmethod
    def suma_multiple(numeros: List[float]) -> float:
        """Calcula la suma de una lista de números."""
        if not numeros:
            raise ValueError("La lista de números no puede estar vacía.")
        return sum(numeros)

    @staticmethod
    def resta(a: float, b: float) -> float:
        """Calcula la resta de dos números (a - b)."""
        return a - b

    @staticmethod
    def multiplicacion(a: float, b: float) -> float:
        """Calcula la multiplicación de dos números."""
        return a * b

    @staticmethod
    def multiplicacion_multiple(numeros: List[float]) -> float:
        """Calcula el producto de una lista de números."""
        if not numeros:
            raise ValueError("La lista de números no puede estar vacía.")
        resultado = 1.0
        for num in numeros:
            resultado *= num
        return resultado

    @staticmethod
    def division(a: float, b: float) -> float:
        """
        Calcula la división de a entre b.
        Lanza ZeroDivisionError si b es 0.
        """
        if b == 0:
            raise ZeroDivisionError("No es posible dividir entre cero.")
        return a / b

    @staticmethod
    def media_aritmetica(numeros: List[float]) -> float:
        """
        Calcula la media aritmética (promedio) de una lista de números.
        Lanza ValueError si la lista está vacía.
        """
        if not numeros:
            raise ValueError("Debe ingresar al menos un número para calcular la media.")
        return sum(numeros) / len(numeros)

    # =========================================================================
    # 2. ÁLGEBRA Y FUNCIONES
    # =========================================================================

    @staticmethod
    def potencia(base: float, exponente: float) -> Union[float, complex]:
        """
        Calcula la potencia base^exponente.
        Soporta resultados complejos cuando la base es negativa y el exponente fraccionario.
        """
        try:
            # Caso especial: base negativa con exponente decimal
            if base < 0 and not exponente.is_integer():
                return complex(base) ** exponente
            return math.pow(base, exponente)
        except OverflowError:
            raise OverflowError("El resultado de la potencia es demasiado grande para ser representado.")
        except ValueError:
            # Si math.pow falla con base negativa, se calcula en el plano complejo
            return complex(base) ** exponente

    @staticmethod
    def raiz(radicando: float, indice: float = 2.0) -> Union[float, complex]:
        """
        Calcula la raíz enésima de un número (por defecto raíz cuadrada, índice=2).
        Soporta:
          - Raíces impares de números negativos en los números reales (ej: raíz cúbica de -8 = -2).
          - Raíces pares de números negativos en los números complejos (ej: raíz cuadrada de -4 = 2i).
        """
        if indice == 0:
            raise ValueError("El índice de la raíz no puede ser cero.")

        if radicando == 0:
            return 0.0

        if radicando > 0:
            return radicando ** (1.0 / indice)

        # Radicando negativo:
        # Si el índice es un entero impar, la solución real existe y es negativa
        if indice.is_integer() and int(indice) % 2 != 0:
            return -(abs(radicando) ** (1.0 / indice))

        # Si el índice es par o decimal, la solución está en los números complejos
        resultado_complejo = cmath.exp(cmath.log(radicando) / indice)
        # Redondear partes infinitesimales por precisión de punto flotante
        real = round(resultado_complejo.real, 10)
        imag = round(resultado_complejo.imag, 10)
        if imag == 0:
            return real
        if real == 0:
            return complex(0, imag)
        return complex(real, imag)

    @staticmethod
    def logaritmo(numero: float, base: Optional[float] = None) -> float:
        """
        Calcula el logaritmo de un número en una base dada.
        - Si base es None, calcula el logaritmo natural (ln, base e).
        - Si base es 10, calcula el logaritmo decimal.
        - Si se especifica otra base, calcula log_base(numero).
        Validaciones:
          - numero > 0
          - base > 0 y base != 1
        """
        if numero <= 0:
            raise ValueError("El argumento del logaritmo debe ser un número estrictamente positivo (x > 0).")

        if base is None:
            return math.log(numero)

        if base <= 0 or base == 1:
            raise ValueError("La base del logaritmo debe ser positiva y distinta de 1 (base > 0 y base ≠ 1).")

        if base == 10:
            return math.log10(numero)
        if base == 2:
            return math.log2(numero)

        return math.log(numero, base)

    @staticmethod
    def resolver_cuadratica(a: float, b: float, c: float) -> Dict[str, Any]:
        """
        Resuelve la ecuación cuadrática ax² + bx + c = 0.
        Retorna un diccionario con:
          - tipo: 'lineal', 'dos_reales', 'raiz_doble', 'complejas', 'infinitas' o 'sin_solucion'
          - discriminante: valor de Δ = b² - 4ac
          - soluciones: tupla con las raíces encontradas
          - descripcion: explicación legible del resultado
        """
        if a == 0:
            if b == 0:
                if c == 0:
                    return {
                        "tipo": "infinitas",
                        "discriminante": None,
                        "soluciones": (),
                        "descripcion": "0 = 0: La ecuación tiene infinitas soluciones (identidad)."
                    }
                else:
                    return {
                        "tipo": "sin_solucion",
                        "discriminante": None,
                        "soluciones": (),
                        "descripcion": f"{c} = 0: Contradicción, la ecuación no tiene solución."
                    }
            solucion_lineal = -c / b
            return {
                "tipo": "lineal",
                "discriminante": None,
                "soluciones": (solucion_lineal,),
                "descripcion": f"a = 0: Es una ecuación lineal (bx + c = 0). Solución única: x = {solucion_lineal}"
            }

        discriminante = (b ** 2) - (4 * a * c)

        if discriminante > 0:
            raiz_disc = math.sqrt(discriminante)
            x1 = (-b + raiz_disc) / (2 * a)
            x2 = (-b - raiz_disc) / (2 * a)
            return {
                "tipo": "dos_reales",
                "discriminante": discriminante,
                "soluciones": (x1, x2),
                "descripcion": f"Discriminante Δ = {discriminante:.4f} > 0: Dos soluciones reales distintas."
            }
        elif discriminante == 0:
            x = -b / (2 * a)
            return {
                "tipo": "raiz_doble",
                "discriminante": discriminante,
                "soluciones": (x,),
                "descripcion": f"Discriminante Δ = 0: Una raíz real doble: x = {x}"
            }
        else:
            # Raíces complejas conjugadas
            parte_real = -b / (2 * a)
            parte_imag = math.sqrt(-discriminante) / (2 * a)
            x1 = complex(parte_real, parte_imag)
            x2 = complex(parte_real, -parte_imag)
            return {
                "tipo": "complejas",
                "discriminante": discriminante,
                "soluciones": (x1, x2),
                "descripcion": f"Discriminante Δ = {discriminante:.4f} < 0: Dos soluciones complejas conjugadas."
            }

    # =========================================================================
    # 3. TEORÍA DE NÚMEROS Y SECUENCIAS
    # =========================================================================

    @staticmethod
    def factorial(n: int) -> int:
        """
        Calcula el factorial de un número entero no negativo n!.
        Lanza ValueError si n < 0 o si no es entero.
        """
        if not isinstance(n, int):
            raise ValueError("El factorial solo está definido para números enteros.")
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos.")
        return math.factorial(n)

    @staticmethod
    def es_primo(n: int) -> Tuple[bool, str]:
        """
        Verifica si un número entero es primo.
        Retorna una tupla: (es_primo: bool, explicacion: str)
        """
        if not isinstance(n, int):
            raise ValueError("La verificación de primalidad requiere un número entero.")

        if n <= 1:
            return False, f"{n} no es primo (los primos son enteros mayores que 1)."
        if n in (2, 3):
            return True, f"{n} es un número primo."
        if n % 2 == 0:
            return False, f"{n} no es primo (es divisible por 2)."
        if n % 3 == 0:
            return False, f"{n} no es primo (es divisible por 3)."

        limite = int(math.isqrt(n))
        for i in range(5, limite + 1, 6):
            if n % i == 0:
                return False, f"{n} no es primo (es divisible por {i})."
            if n % (i + 2) == 0:
                return False, f"{n} no es primo (es divisible por {i + 2})."

        return True, f"{n} es un número primo."

    @staticmethod
    def mcd(a: int, b: int) -> int:
        """
        Calcula el Máximo Común Divisor (MCD) entre dos enteros a y b.
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Ambos números deben ser enteros.")
        return math.gcd(a, b)

    @staticmethod
    def mcd_multiple(numeros: List[int]) -> int:
        """Calcula el MCD de una lista de enteros."""
        if not numeros:
            raise ValueError("Debe ingresar al menos un número.")
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado = math.gcd(resultado, num)
        return resultado

    @staticmethod
    def mcm(a: int, b: int) -> int:
        """
        Calcula el Mínimo Común Múltiplo (MCM) entre dos enteros a y b.
        """
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Ambos números deben ser enteros.")
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // math.gcd(a, b)

    @staticmethod
    def mcm_multiple(numeros: List[int]) -> int:
        """Calcula el MCM de una lista de enteros."""
        if not numeros:
            raise ValueError("Debe ingresar al menos un número.")
        resultado = numeros[0]
        for num in numeros[1:]:
            if resultado == 0 or num == 0:
                resultado = 0
            else:
                resultado = abs(resultado * num) // math.gcd(resultado, num)
        return resultado

    @staticmethod
    def fibonacci(n: int) -> List[int]:
        """
        Genera los primeros n términos de la serie de Fibonacci.
        Ejemplo: n = 10 -> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        Lanza ValueError si n <= 0 o no es entero.
        """
        if not isinstance(n, int):
            raise ValueError("La cantidad de términos debe ser un número entero.")
        if n <= 0:
            raise ValueError("La cantidad de términos debe ser mayor que cero (n > 0).")

        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        secuencia = [0, 1]
        for _ in range(2, n):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia

    # =========================================================================
    # 4. TRIGONOMETRÍA
    # =========================================================================

    @staticmethod
    def _ajustar_angulo(angulo: float, en_grados: bool) -> float:
        """Convierte a radianes si está en grados sexagesimales."""
        return math.radians(angulo) if en_grados else angulo

    @staticmethod
    def _limpiar_cero_flotante(valor: float, tolerancia: float = 1e-12) -> float:
        """Corrige imprecisiones de punto flotante cercanas a cero."""
        if abs(valor) < tolerancia:
            return 0.0
        return valor

    @classmethod
    def seno(cls, angulo: float, en_grados: bool = True) -> float:
        """
        Calcula el seno de un ángulo.
        - en_grados: True si el ángulo está en grados sexagesimales, False si está en radianes.
        """
        rad = cls._ajustar_angulo(angulo, en_grados)
        resultado = math.sin(rad)
        return cls._limpiar_cero_flotante(resultado)

    @classmethod
    def coseno(cls, angulo: float, en_grados: bool = True) -> float:
        """
        Calcula el coseno de un ángulo.
        - en_grados: True si el ángulo está en grados sexagesimales, False si está en radianes.
        """
        rad = cls._ajustar_angulo(angulo, en_grados)
        resultado = math.cos(rad)
        return cls._limpiar_cero_flotante(resultado)

    @classmethod
    def tangente(cls, angulo: float, en_grados: bool = True) -> float:
        """
        Calcula la tangente de un ángulo.
        Verifica indeterminaciones (asíntotas) donde cos(angulo) = 0 (ej: 90°, 270°, π/2, 3π/2).
        Lanza ValueError si la tangente no está definida.
        """
        rad = cls._ajustar_angulo(angulo, en_grados)
        cos_val = cls.coseno(angulo, en_grados)

        if abs(cos_val) < 1e-12:
            unidad = "grados" if en_grados else "rad"
            raise ValueError(f"La tangente no está definida para {angulo}° {unidad} (asíntota vertical, cos = 0).")

        resultado = math.tan(rad)
        return cls._limpiar_cero_flotante(resultado)
