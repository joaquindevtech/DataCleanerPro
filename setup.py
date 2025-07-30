#setup.py es el archivo de configuración principal de un proyecto de Python cuando quieres que sea:
#Instalado como un paquete (pip install)
#Compartido públicamente en PyPI
#Usado como una librería desde otros proyectos
#Ejecutado como una herramienta de la terminal (CLI)

from setuptools import setup, find_packages

setup(
    name="datacleanerpro",
    version="0.1.0",
    description="Librería de limpieza de datos automática con CLI",
    author="Tu Nombre",
    author_email="tu@email.com",
    packages=find_packages(),  # Busca automáticamente todos los módulos
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "typer"
    ],
    entry_points={
        'console_scripts': [
            'datacleanerpro=datacleanerpro.cli:app',  # CLI (la crearemos en otro sprint)
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
