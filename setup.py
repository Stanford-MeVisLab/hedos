from setuptools import setup, find_packages

setup(
    name='hedos',
    version='1.0.0',
    packages=find_packages(),
    install_requires=open("requirements.txt").readlines(),  # List of dependencies
)
