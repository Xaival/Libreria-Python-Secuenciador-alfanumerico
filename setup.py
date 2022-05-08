from setuptools import setup

readme = open("./README.md", "r")

setup (
    name="Secuenciador alfanumérico",
    packages=['ConvertDicc'], # Este debe ser el mismo que el nombre de la carpeta
    version="2022.05.08",
    description="Convierte de un número o números a un grupo de caracteres y viceversa",
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author="Xaival",
    author_email="xaival.dark@gmail.com",
    url='https://github.com/Xaival/Libreria-Python-Secuenciador-alfanumerico', # Usar la URL del repositorio de github
    keywords=['conversions', 'sequence', 'alphanumeric', 'binary'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)