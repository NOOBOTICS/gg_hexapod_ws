from setuptools import find_packages
from setuptools import setup

setup(
    name='gg_hex_utils',
    version='0.0.0',
    packages=find_packages(
        include=('gg_hex_utils', 'gg_hex_utils.*')),
)
