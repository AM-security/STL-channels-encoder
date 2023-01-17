from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'An encoder package for STL files'
LONG_DESCRIPTION = 'A package that makes it easy to encode data into covert channels of STL files'

setup(
    name="stl_covert_channels",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Aleksandr Dolgavin",
    author_email="sanya554455@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='encoder',
    classifiers= [
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)