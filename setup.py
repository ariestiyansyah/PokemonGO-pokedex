from distutils.core import setup
from setuptools import find_packages

setup(
    name='PokemonGO-pokedex',
    version='1.0.0',
    scripts=['PokemonGO-pokedex'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Get Pokemon GO name based on Pokedex number',
    long_description='Get Pokemon GO name based on Pokedex number',
    install_requires=['requests','json'],
    url='http://github.com/ariestiyansyah/PokemonGO-pokedex',
    author='Rizky Ariestiyansyah',
    author_email='ariestiyansyah.rizky@gmail.com'
)
