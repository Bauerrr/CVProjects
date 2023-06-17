from setuptools import find_packages, setup

setup(
    name='Algorithms',
    packages=find_packages(include=['hash_table']),
    version='0.1.0',
    description='python library with algorithms',
    author='Grzegorz Bauer',
    license='MIT',
    install_requires=['numpy'],
)