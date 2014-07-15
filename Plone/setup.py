from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='Plone',
      version=version,
      description="Ejercicio de conjuntos Plone",
      long_description="""\
Ejemplos de conjuntos basados en Plone, para demostrar como crear un paquete Egg Python.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='package python Egg conjuntos Plone',
      author='Jesus Linares',
      author_email='jesuslinares307@gmail.com',
      url='https://github.com/je',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
