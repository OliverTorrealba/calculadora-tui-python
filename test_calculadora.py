"""
Módulo: test_calculadora.py
Descripción: Suite de pruebas unitarias para CalculadoraModelo usando unittest.
Garantiza la confiabilidad, precisión matemática y robustez del código.
"""

import unittest
import math
from modelo import CalculadoraModelo


class TestCalculadoraModelo(unittest.TestCase):
    """Pruebas unitarias para las funciones de CalculadoraModelo."""

    # =========================================================================
    # 1. PRUEBAS DE ARITMÉTICA Y ESTADÍSTICA
    # =========================================================================

    def test_suma(self):
        self.assertEqual(CalculadoraModelo.suma(5, 3), 8)
        self.assertEqual(CalculadoraModelo.suma(-5, 5), 0)
        self.assertAlmostEqual(CalculadoraModelo.suma(0.1, 0.2), 0.3, places=7)

    def test_suma_multiple(self):
        self.assertEqual(CalculadoraModelo.suma_multiple([1, 2, 3, 4, 5]), 15)
        self.assertEqual(CalculadoraModelo.suma_multiple([10.5, -2.5, 2]), 10.0)
        with self.assertRaises(ValueError):
            CalculadoraModelo.suma_multiple([])

    def test_resta(self):
        self.assertEqual(CalculadoraModelo.resta(10, 4), 6)
        self.assertEqual(CalculadoraModelo.resta(4, 10), -6)
        self.assertEqual(CalculadoraModelo.resta(-5, -5), 0)

    def test_multiplicacion(self):
        self.assertEqual(CalculadoraModelo.multiplicacion(6, 7), 42)
        self.assertEqual(CalculadoraModelo.multiplicacion(-3, 4), -12)
        self.assertEqual(CalculadoraModelo.multiplicacion(0, 100), 0)

    def test_multiplicacion_multiple(self):
        self.assertEqual(CalculadoraModelo.multiplicacion_multiple([2, 3, 4]), 24)
        self.assertEqual(CalculadoraModelo.multiplicacion_multiple([5, 0, 10]), 0)
        with self.assertRaises(ValueError):
            CalculadoraModelo.multiplicacion_multiple([])

    def test_division(self):
        self.assertEqual(CalculadoraModelo.division(10, 2), 5.0)
        self.assertEqual(CalculadoraModelo.division(-9, 3), -3.0)
        with self.assertRaises(ZeroDivisionError):
            CalculadoraModelo.division(10, 0)

    def test_media_aritmetica(self):
        self.assertEqual(CalculadoraModelo.media_aritmetica([10, 20, 30]), 20.0)
        self.assertEqual(CalculadoraModelo.media_aritmetica([5]), 5.0)
        self.assertAlmostEqual(CalculadoraModelo.media_aritmetica([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            CalculadoraModelo.media_aritmetica([])

    # =========================================================================
    # 2. PRUEBAS DE ÁLGEBRA Y ANÁLISIS
    # =========================================================================

    def test_potencia(self):
        self.assertEqual(CalculadoraModelo.potencia(2, 3), 8.0)
        self.assertEqual(CalculadoraModelo.potencia(5, 0), 1.0)
        self.assertEqual(CalculadoraModelo.potencia(2, -1), 0.5)

    def test_raiz(self):
        self.assertEqual(CalculadoraModelo.raiz(16, 2), 4.0)
        self.assertEqual(CalculadoraModelo.raiz(27, 3), 3.0)
        # Raíz impar de número negativo (solución real negativa)
        self.assertAlmostEqual(CalculadoraModelo.raiz(-8, 3), -2.0)
        # Raíz par de número negativo (solución en números complejos)
        res_comp = CalculadoraModelo.raiz(-4, 2)
        self.assertIsInstance(res_comp, complex)
        self.assertAlmostEqual(res_comp.imag, 2.0)
        with self.assertRaises(ValueError):
            CalculadoraModelo.raiz(16, 0)

    def test_logaritmo(self):
        self.assertAlmostEqual(CalculadoraModelo.logaritmo(math.e), 1.0)
        self.assertAlmostEqual(CalculadoraModelo.logaritmo(100, base=10), 2.0)
        self.assertAlmostEqual(CalculadoraModelo.logaritmo(8, base=2), 3.0)
        with self.assertRaises(ValueError):
            CalculadoraModelo.logaritmo(-5)
        with self.assertRaises(ValueError):
            CalculadoraModelo.logaritmo(10, base=1)
        with self.assertRaises(ValueError):
            CalculadoraModelo.logaritmo(10, base=-2)

    def test_resolver_cuadratica(self):
        # Dos raíces reales: x² - 5x + 6 = 0 -> x1=3, x2=2
        res1 = CalculadoraModelo.resolver_cuadratica(1, -5, 6)
        self.assertEqual(res1["tipo"], "dos_reales")
        self.assertIn(3.0, res1["soluciones"])
        self.assertIn(2.0, res1["soluciones"])

        # Raíz doble: x² - 4x + 4 = 0 -> x = 2
        res2 = CalculadoraModelo.resolver_cuadratica(1, -4, 4)
        self.assertEqual(res2["tipo"], "raiz_doble")
        self.assertEqual(res2["soluciones"][0], 2.0)

        # Raíces complejas: x² + 1 = 0 -> x = ± i
        res3 = CalculadoraModelo.resolver_cuadratica(1, 0, 1)
        self.assertEqual(res3["tipo"], "complejas")
        self.assertAlmostEqual(res3["soluciones"][0].imag, 1.0)
        self.assertAlmostEqual(res3["soluciones"][1].imag, -1.0)

        # Caso lineal: 2x - 4 = 0 -> x = 2
        res4 = CalculadoraModelo.resolver_cuadratica(0, 2, -4)
        self.assertEqual(res4["tipo"], "lineal")
        self.assertEqual(res4["soluciones"][0], 2.0)

    # =========================================================================
    # 3. PRUEBAS DE TEORÍA DE NÚMEROS Y SECUENCIAS
    # =========================================================================

    def test_factorial(self):
        self.assertEqual(CalculadoraModelo.factorial(0), 1)
        self.assertEqual(CalculadoraModelo.factorial(1), 1)
        self.assertEqual(CalculadoraModelo.factorial(5), 120)
        with self.assertRaises(ValueError):
            CalculadoraModelo.factorial(-1)

    def test_es_primo(self):
        self.assertFalse(CalculadoraModelo.es_primo(0)[0])
        self.assertFalse(CalculadoraModelo.es_primo(1)[0])
        self.assertTrue(CalculadoraModelo.es_primo(2)[0])
        self.assertTrue(CalculadoraModelo.es_primo(3)[0])
        self.assertFalse(CalculadoraModelo.es_primo(4)[0])
        self.assertTrue(CalculadoraModelo.es_primo(17)[0])
        self.assertTrue(CalculadoraModelo.es_primo(97)[0])
        self.assertFalse(CalculadoraModelo.es_primo(100)[0])

    def test_mcd(self):
        self.assertEqual(CalculadoraModelo.mcd(48, 18), 6)
        self.assertEqual(CalculadoraModelo.mcd(101, 103), 1)
        self.assertEqual(CalculadoraModelo.mcd_multiple([24, 36, 60]), 12)

    def test_mcm(self):
        self.assertEqual(CalculadoraModelo.mcm(12, 18), 36)
        self.assertEqual(CalculadoraModelo.mcm(5, 7), 35)
        self.assertEqual(CalculadoraModelo.mcm(0, 5), 0)
        self.assertEqual(CalculadoraModelo.mcm_multiple([4, 6, 8]), 24)

    def test_fibonacci(self):
        self.assertEqual(CalculadoraModelo.fibonacci(1), [0])
        self.assertEqual(CalculadoraModelo.fibonacci(2), [0, 1])
        self.assertEqual(CalculadoraModelo.fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(
            CalculadoraModelo.fibonacci(10),
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        )
        with self.assertRaises(ValueError):
            CalculadoraModelo.fibonacci(0)
        with self.assertRaises(ValueError):
            CalculadoraModelo.fibonacci(-3)

    # =========================================================================
    # 4. PRUEBAS DE TRIGONOMETRÍA
    # =========================================================================

    def test_seno(self):
        self.assertAlmostEqual(CalculadoraModelo.seno(0, en_grados=True), 0.0)
        self.assertAlmostEqual(CalculadoraModelo.seno(90, en_grados=True), 1.0)
        self.assertAlmostEqual(CalculadoraModelo.seno(180, en_grados=True), 0.0)
        self.assertAlmostEqual(CalculadoraModelo.seno(math.pi / 2, en_grados=False), 1.0)

    def test_coseno(self):
        self.assertAlmostEqual(CalculadoraModelo.coseno(0, en_grados=True), 1.0)
        self.assertAlmostEqual(CalculadoraModelo.coseno(90, en_grados=True), 0.0)
        self.assertAlmostEqual(CalculadoraModelo.coseno(180, en_grados=True), -1.0)

    def test_tangente(self):
        self.assertAlmostEqual(CalculadoraModelo.tangente(0, en_grados=True), 0.0)
        self.assertAlmostEqual(CalculadoraModelo.tangente(45, en_grados=True), 1.0)
        # Indeterminación en 90°
        with self.assertRaises(ValueError):
            CalculadoraModelo.tangente(90, en_grados=True)
        with self.assertRaises(ValueError):
            CalculadoraModelo.tangente(270, en_grados=True)


if __name__ == "__main__":
    unittest.main()
