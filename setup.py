from distutils.core import setup
from setuptools import find_packages

setup(
    name="Math_Quiz",
    version="1.0",
    author="Besir",
    packages=find_packages(),
    install_requires=["numpy", "random"],
)
