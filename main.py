"""
Modulo: main.py
Descripcion: Punto de entrada de la Calculadora Cientifica en Python.
Arquitectura: Modelo - Vista - Controlador (MVC).
"""

from controlador import CalculadoraControlador


def main() -> None:
    """Inicializa el controlador y arranca la aplicacion."""
    try:
        app = CalculadoraControlador()
        app.iniciar()
    except KeyboardInterrupt:
        print("\n\n[INFO] Programa interrumpido por el usuario. Hasta luego.")


if __name__ == "__main__":
    main()
