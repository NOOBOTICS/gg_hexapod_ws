from setuptools import find_packages
from setuptools import setup

setup(
    name='arm_utils_pkg',
    version='0.0.0',
    packages=find_packages(
        include=('arm_utils_pkg', 'arm_utils_pkg.*')),
)
